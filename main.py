import json
import os
from station_graph import StationGraph
from download_functions import *


if __name__ == '__main__':
    state_stations = {}
    # ------------------------------------------------------------------
    # Northwest district
    station_graph_NW = StationGraph()
    station_graph_NW.add_station('SXK', 42.98583, -96.1614)
    station_graph_NW.add_station('ORC', 42.98949, -96.06059)
    station_graph_NW.add_station('SHL', 43.20816, -95.83531)
    station_graph_NW.add_station('SPW', 43.16822, -95.21009)
    station_graph_NW.add_station('EST', 43.40085, -94.74764)
    station_graph_NW.add_station('LRJ', 42.77538, -96.19225)
    station_graph_NW.add_station('CKP', 42.73042, -95.55378)
    station_graph_NW.add_station('SLB', 42.59723, -95.23992)
    station_graph_NW.calculate_distances()

    stations_NW = ["SHL", "SPW", "LRJ", "CKP"]

    state_stations['NW'] = [stations_NW, station_graph_NW]
    # ------------------------------------------------------------------
    # North Central district
    station_graph_NC = StationGraph()
    station_graph_NC.add_station('AXA', 43.07965, -94.27237)
    station_graph_NC.add_station('FXY', 43.23232, -93.62367)
    station_graph_NC.add_station('MCW', 43.15438, -93.3261)
    station_graph_NC.add_station('CCY', 43.07301, -92.61322)
    station_graph_NC.add_station('CAV', 42.74304, -93.75926)
    station_graph_NC.add_station('HPT', 42.71752, -93.22439)
    station_graph_NC.calculate_distances()

    stations_NC = ["AXA", "MCW", "CAV", "HPT"]

    state_stations['NC'] = [stations_NC, station_graph_NC]
    # ------------------------------------------------------------------
    # Northeast district
    station_graph_NE = StationGraph()
    station_graph_NE.add_station('CCY', 43.07301, -92.61322)
    station_graph_NE.add_station('DEH', 43.27552, -91.74331)
    station_graph_NE.add_station('ALO', 42.55437, -92.40129)
    station_graph_NE.add_station('OLZ', 42.68314, -91.97599)
    station_graph_NE.add_station('IIB', 42.45443, -91.9504)
    station_graph_NE.add_station('DBQ', 42.39835, -90.70914)
    station_graph_NE.calculate_distances()

    stations_NE = ["CCY", "DEH", "ALO", "IIB"]

    state_stations['NE'] = [stations_NE, station_graph_NE]
    # ------------------------------------------------------------------
    # West Central district
    station_graph_WC = StationGraph()
    station_graph_WC.add_station('SUX', 43.07301, -92.61322)
    station_graph_WC.add_station('DNS', 43.27552, -91.74331)
    station_graph_WC.add_station('CIN', 42.55437, -92.40129)
    station_graph_WC.add_station('HNR', 42.68314, -91.97599)
    station_graph_WC.add_station('ADU', 42.45443, -91.9504)
    station_graph_WC.calculate_distances()

    stations_WC = ["SUX", "DNS", "CIN", "HNR"]

    state_stations['WC'] = [stations_WC, station_graph_WC]
    # ------------------------------------------------------------------
    # Central district
    station_graph_C = StationGraph()
    station_graph_C.add_station('FOD', 42.54974, -94.2032)
    station_graph_C.add_station('EBS', 42.43923, -93.86908)
    station_graph_C.add_station('IFA', 42.4691, -93.26508)
    station_graph_C.add_station('BNW', 42.04857, -93.84858)
    station_graph_C.add_station('AMW', 41.99044, -93.61852)
    station_graph_C.add_station('MIW', 42.11061, -92.91632)
    station_graph_C.add_station('PRO', 41.82779, -94.16371)
    station_graph_C.add_station('IKV', 41.68781, -93.56948)
    station_graph_C.add_station('TNU', 41.67011, -93.01904)
    station_graph_C.add_station('TNU', 41.67011, -93.01904)
    station_graph_C.add_station('GGI', 41.70973, -92.7332)
    station_graph_C.add_station('DSM', 41.53395, -93.65311)
    station_graph_C.calculate_distances()

    stations_C = ["EBS", "AMW", "MIW", "TNU"]

    state_stations['C'] = [stations_C, station_graph_C]
    # ------------------------------------------------------------------
    # East Central district
    station_graph_EC = StationGraph()
    station_graph_EC.add_station('VTI', 42.21758, -92.02484)
    station_graph_EC.add_station('MXO', 42.22036, -91.16046)
    station_graph_EC.add_station('CID', 41.8829, -91.72459)
    station_graph_EC.add_station('CWI', 41.8295, -90.3328)
    station_graph_EC.add_station('IOW', 41.63939, -91.54454)
    station_graph_EC.add_station('DVN', 41.61333, -90.59483)
    station_graph_EC.add_station('MUT', 41.36699, -91.14058)
    station_graph_EC.calculate_distances()

    stations_EC = ["CID", "CWI", "IOW", "DVN"]

    state_stations['EC'] = [stations_EC, station_graph_EC]
    # ------------------------------------------------------------------
    # Southwest district
    station_graph_SW = StationGraph()
    station_graph_SW.add_station('CBF', 41.26111, -95.76041)
    station_graph_SW.add_station('AIO', 41.40588, -95.04653)
    station_graph_SW.add_station('RDK', 41.01065, -95.26241)
    station_graph_SW.add_station('SDA', 40.75328, -95.41123)
    station_graph_SW.add_station('ICL', 40.72415, -95.02227)
    station_graph_SW.calculate_distances()

    stations_SW = ["CBF", "RDK", "AIO", "SDA"]

    state_stations['SW'] = [stations_SW, station_graph_SW]
    # ------------------------------------------------------------------
    # South Central district
    station_graph_SC = StationGraph()
    station_graph_SC.add_station('CSQ', 41.01879, -94.3608)
    station_graph_SC.add_station('I75', 41.04717, -93.68761)
    station_graph_SC.add_station('CNC', 41.01843, -93.36077)
    station_graph_SC.add_station('OXV', 41.29845, -93.11139)
    station_graph_SC.add_station('PEA', 41.39891, -92.94311)
    station_graph_SC.add_station('LWD', 40.63064, -93.90047)
    station_graph_SC.add_station('TVK', 40.68318, -92.89834)
    station_graph_SC.calculate_distances()

    stations_SC = ["CSQ", "I75", "LWD", "TVK"]

    state_stations['SC'] = [stations_SC, station_graph_SC]
    # ------------------------------------------------------------------
    # Southeast district
    station_graph_SE = StationGraph()
    station_graph_SE.add_station('OOA', 41.22728, -92.49187)
    station_graph_SE.add_station('AWG', 41.27514, -91.67481)
    station_graph_SE.add_station('OTM', 41.10079, -92.44459)
    station_graph_SE.add_station('FFL', 41.05209, -91.98341)
    station_graph_SE.add_station('MPZ', 40.94525, -91.51223)
    station_graph_SE.add_station('BRL', 40.77293, -91.12549)
    station_graph_SE.add_station('FSW', 40.66148, -91.32672)
    station_graph_SE.add_station('EOK', 40.46146, -91.42739)
    station_graph_SE.calculate_distances()

    stations_SE = ["OTM", "AWG", "MPZ", "EOK"]

    state_stations['SE'] = [stations_SE, station_graph_SE]
    # ------------------------------------------------------------------
    file_names = {"NW": {}, "NC": {}, "NE": {}, "WC": {}, "C": {}, "EC": {}, "SW": {}, "SC": {}, "SE": {}}
    # ------------------------------------------------------------------
    weather_files_csv = './weather_files_csv/'

    if not os.path.exists(weather_files_csv):
        os.makedirs(weather_files_csv)
        print(f"Directory '{weather_files_csv}' created successfully.")
    else:
        print(f"Directory '{weather_files_csv}' already exists.")


    suit_days_pdf = './suit_days_pdf/'

    if not os.path.exists(suit_days_pdf):
        os.makedirs(suit_days_pdf)
        print(f"Directory '{suit_days_pdf}' created successfully.")
    else:
        print(f"Directory '{suit_days_pdf}' already exists.")
    # ------------------------------------------------------------------
    for district in state_stations.keys():
        stations = state_stations[district][0]
        station_graph = state_stations[district][1]
        file_names[district][18] = []
        file_names[district][19] = []
        file_names[district][20] = []
        file_names[district][21] = []
        file_names[district][22] = []
        file_names[district][23] = []
        for station in stations:
            file_names[district][18].append(
                get_weather_data("2018-03-26", "2018-11-25", station, './weather_files_csv/',
                                 ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
            file_names[district][19].append(
                get_weather_data("2019-03-25", "2019-12-8", station, './weather_files_csv/',
                                ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
            file_names[district][20].append(
                get_weather_data("2020-03-30", "2020-11-29", station, './weather_files_csv/',
                                 ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
            file_names[district][21].append(
                get_weather_data("2021-03-29", "2021-11-28", station, './weather_files_csv/',
                                 ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
            file_names[district][22].append(
                get_weather_data("2022-03-28", "2022-11-27", station, './weather_files_csv/',
                                 ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
            file_names[district][23].append(
                get_weather_data("2023-03-27", "2023-11-26", station, './weather_files_csv/',
                                 ['precip_in', 'avg_wind_speed_kts', 'avg_rh', 'avg_feel'], station_graph))
    # ------------------------------------------------------------------
    with open('file_names.json', 'w') as json_file:
        json.dump(file_names, json_file)
    # ------------------------------------------------------------------
    start_end_18_23 = {18: ["04-01-18", "11-25-18"], 19: ["04-01-19", "12-09-19"], 20: ["04-06-20", "11-30-20"],
                       21: ["04-05-21", "11-29-21"], 22: ["04-04-22", "11-28-22"], 23: ["04-03-23", "11-27-23"]}
    # ------------------------------------------------------------------
    output_names = {18: [], 19: [], 20: [], 21: [], 22: [], 23: []}
    # ------------------------------------------------------------------
    save_folder = './suit_days_pdf/'
    for key in start_end_18_23.keys():
        start_date, end_date = start_end_18_23[key]
        url_template = 'https://www.nass.usda.gov/Statistics_by_State/Iowa/Publications/Crop_Progress_&_Condition/20key/IA-Crop-Progress-{0}.pdf'.replace(
            "key", str(key))
        output_names[key] = download_files_on_days(start_date, end_date, url_template, save_folder, target_day='Saturday')
    # ------------------------------------------------------------------
    with open('output_names.json', 'w') as json_file:
        json.dump(output_names, json_file)

