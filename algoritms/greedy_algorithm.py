states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

best_station = None
status_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    if len(covered) > len(status_covered):
        best_station = station
        status_covered = covered
        final_stations.add(best_station)
        states_needed -= status_covered

        while states_needed:
            best_station = None
            states_covered = set()
            for station, states in stations.items():
                covered = states_needed & states
                if len(covered) > len(status_covered):
                    best_station = station
                    status_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
