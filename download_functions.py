import requests
from datetime import datetime
from dateutil import parser
import re
from datetime import timedelta


def get_weather_data(start_date_str, end_date_str, station_code, save_location, variables, station_graph):
    # Convert date strings to datetime objects
    start_date = parser.parse(start_date_str)
    end_date = parser.parse(end_date_str)

    # Replace dashes with underscores
    start_date_str = start_date_str.replace('-', '_')
    end_date_str = end_date_str.replace('-', '_')

    # Construct the list of variables for the URL
    variables_str = '&'.join(f'var={var}' for var in variables)

    file_name = f'{start_date_str}_{end_date_str}_{station_code}.csv'

    full_save_path = f'{save_location}/{file_name}'  # Assuming save_location is a directory

    # Download data for the specified date range
    url = f'https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=IA_ASOS&stations={station_code}&year1={start_date.year}&month1={start_date.month}&day1={start_date.day}&year2={end_date.year}&month2={end_date.month}&day2={end_date.day}&{variables_str}&na=None&format=csv'
    response = requests.get(url)

    # speed fix:
    station_chain = {}
    station_graph.set_start(station_code)
    a = station_graph.next_nearest()
    url_st = f'https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=IA_ASOS&stations={a}&year1={start_date.year}&month1={start_date.month}&day1={start_date.day}&year2={end_date.year}&month2={end_date.month}&day2={end_date.day}&{variables_str}&na=None&format=csv'
    response_st = requests.get(url_st)
    station_chain[a] = (response_st.text.strip().split('\n'))
    while a is not None:
        a = station_graph.next_nearest()
        url_st = f'https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=IA_ASOS&stations={a}&year1={start_date.year}&month1={start_date.month}&day1={start_date.day}&year2={end_date.year}&month2={end_date.month}&day2={end_date.day}&{variables_str}&na=None&format=csv'
        response_st = requests.get(url_st)
        station_chain[a] = (response_st.text.strip().split('\n'))

    if response.status_code == 200:
        # Split the response text into lines
        lines = response.text.split('\n')
        # Initialize a list to store modified lines
        modified_lines = []
        # Lets assume that dates are always right in the first station row
        lines = lines[:-1]
        for line in lines:

            line_sub = line

            line_printed = False

            # Set the start station for the graph
            station_graph.set_start(station_code)

            while ("None" in line_sub or not line_sub):  # or station_graph.next_nearest() != None:

                if not line_printed:
                    print(line)
                    line_printed = True

                # Convert the date string to a datetime object
                date_str = line.split(',')[1]

                new_station = station_graph.next_nearest()
                if new_station == None:
                    break

                texty = station_chain[new_station]
                print(new_station)
                if len(texty) == 1:
                    continue
                    # Shit is hard when you are here
                match = re.search(r'\W', texty[1].split(',')[1])
                delimiter = match.group()
                match_ = re.search(r'\W', date_str)
                delimiter_ = match_.group()
                if delimiter == delimiter_:
                    for row in texty[1:]:
                        if date_str in row:
                            line_sub = row
                else:
                    date_str.replace(delimiter_, delimiter)
                    for row in texty[1:]:
                        if date_str in row:
                            row.replace(delimiter, delimiter_)
                            line_sub = row

                print(f"With line from station {new_station}: {line_sub} lens:{len(line_sub)}")

            if line_sub != None and "None" not in line_sub and len(line_sub) != 0:

                modified_lines.append(line_sub)
            else:
                modified_lines.append(line)

        # Save all modified lines to the CSV file
        with open(full_save_path, 'w') as file:
            file.writelines('\n'.join(modified_lines))

        print(f"CSV file saved successfully at: {full_save_path}")
    return file_name


def generate_dates(start_date_str, end_date_str, date_format='%m-%d-%y'):
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)

    current_date = start_date
    date_list = []

    while current_date <= end_date:
        date_list.append([current_date.strftime(date_format), current_date.strftime('%A')])  # Append [date_str, day_str]
        current_date += timedelta(days=1)

    return date_list


def download_files_on_days(start_date_str, end_date_str, url_template, save_folder, target_day='Saturday', date_format='%m-%d-%y'):
    date_list = generate_dates(start_date_str, end_date_str, date_format)
    names = []
    i = 0
    while i < len(date_list):
        current_date_str, current_day = date_list[i]
        file_url = url_template.format(current_date_str)
        save_path = f"{save_folder}/{current_date_str}.pdf"
        print(file_url)
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File saved successfully at: {save_path}")
            names.append(f"{current_date_str}.pdf")
            # Move to the next target day
            current_date = datetime.strptime(current_date_str, date_format)
            while current_date.strftime('%A') != target_day:
                current_date += timedelta(days=1)
            current_date_str = current_date.strftime(date_format)
            if current_date_str > end_date_str:
                break
            i = date_list.index([current_date_str, target_day])
            # Check if the current date is the end date
            if current_date_str == end_date_str:
                break
        else:
            print(f"Failed to download file for {current_date_str}. Status code: {response.status_code}")
        i += 1
    return names