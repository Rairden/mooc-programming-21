import math


def get_station_data(filename: str):
    with open(filename) as file:
        next(file)
        stations = {}

        for line in file:
            ln = line.replace("\n", "").split(";")
            stations[ln[3]] = (float(ln[0]), float(ln[1]))

    return stations


def greatest_distance(stations: dict):
    maxDist = 0
    allStations = list(stations.keys())

    for i, st1 in enumerate(stations):
        for j in range(i + 1, len(stations)):
            dist = distance(stations, st1, allStations[j])
            if dist > maxDist:
                maxDist = dist
                stat1 = st1
                stat2 = allStations[j]

    return stat1, stat2, maxDist


def distance(stations: dict, station1: str, station2: str):
    s1 = stations[station1]
    s2 = stations[station2]
    x_km = (s1[0] - s2[0]) * 55.26
    y_km = (s1[1] - s2[1]) * 111.2
    distance_km = math.sqrt(x_km ** 2 + y_km ** 2)

    return distance_km


if __name__ == '__main__':
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    e = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    print(e)

    stations = get_station_data("stations1.csv")
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
