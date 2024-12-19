import pandas as pd
import matplotlib.pyplot as plt
import lines

x_axis = []
y_axis = []

file_path = "stationwise_hourly_entry_exit_february_2024.xlsx"
df_entry = pd.read_excel(file_path, sheet_name="Entry")
df_exit = pd.read_excel(file_path, sheet_name="Exit")

for i in range(253):
    station_name = pd.Series(df_entry.iloc[i])
    row = pd.Series(df_entry.iloc[i])

    lst = ["HR4", "HR5", "HR6", "HR7", "HR8", "HR9", "HR10", "HR11", "HR12", "HR13", "HR14", "HR15","HR16", "HR17", "HR18", "HR19", "HR20", "HR21", "HR22", "HR23", "HR24"]

    station_name = "sitename"
    day = "businessday"
    line_id = "lineid"

    total_entry = 0

    y_axis.append(row[station_name])
    for j in lst:
        total_entry += int(row[j])

    x_axis.append(total_entry)

plt.title("Top 30 conjested stations as on 1st Feb 2024")
plt.xlabel('Lines')
plt.ylabel('Passenger count')

max_stations = {}

for i in range(30):
    max_stations[y_axis[x_axis.index(max(x_axis))]] = max(x_axis)
    y_axis.remove(y_axis[x_axis.index(max(x_axis))])
    x_axis.remove(max(x_axis))

keys = list(max_stations.keys()) #name of stations
values = list(max_stations.values())

plt.xticks(rotation=90)
plt.bar(keys, values)

plt.show()
