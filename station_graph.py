from math import radians, sin, cos, sqrt, atan2

class StationGraph:
    def __init__(self):
        self.graph = {}
        self.start_station = None
        self.sorted_stations = []

    def add_station(self, station, latitude, longitude):
        self.graph[station] = {'latitude': latitude, 'longitude': longitude}

    def set_start(self, start_station):
        if start_station in self.graph:
            self.start_station = start_station
            self.calculate_distances()
        else:
            print(f"Station '{start_station}' not found in the graph.")

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def calculate_distances(self):
        if self.start_station is not None:
            # List to store distances as sublists [station, distance]
            distances_list = []

            for station, coordinates in self.graph.items():
                if self.start_station != station:
                    # Calculate the Euclidean distance between the start station and the current station
                    distance = self.haversine_distance(
                        coordinates['latitude'], coordinates['longitude'],
                        self.graph[self.start_station]['latitude'], self.graph[self.start_station]['longitude']
                    )

                    # Add the station and its distance to the list
                    distances_list.append([station, distance])

            # Sort distances_list by distance in ascending order
            self.sorted_stations = sorted(distances_list, key=lambda x: x[1])
            #print(self.sorted_stations)



    def next_nearest(self):
        if not self.sorted_stations:
            #print("No more stations.")
            return None

        closest_station = self.sorted_stations.pop(0)[0]
        return closest_station