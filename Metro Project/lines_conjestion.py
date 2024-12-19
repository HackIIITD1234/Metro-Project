import pandas as pd
import matplotlib.pyplot as plt
import lines

x_axis = []
y_axis = []

file_path = "stationwise_hourly_entry_exit_february_2024.xlsx"
df_entry = pd.read_excel(file_path, sheet_name="Entry")
df_exit = pd.read_excel(file_path, sheet_name="Exit")

for i in range(253):  #change here to get data for month
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

line_conjestion = {'red_line_1' : 0, 'yellow_line_2' : 0, 'blue_line_3' : 0, "blue_line_4" : 0, "green_line_5" : 0, "violet_line_6" : 0, "pink_line_7" : 0, "magenta_line_8" : 0}

for i in range(len(x_axis)):
    if y_axis[i].title() in lines.red_line1:
        line_conjestion['red_line_1']  += x_axis[i]
    elif y_axis[i].title() in lines.yellow_line2:
        line_conjestion['yellow_line_2']  += x_axis[i]
    elif y_axis[i].title() in lines.blue_line3:
        line_conjestion['blue_line_3']  += x_axis[i]
    elif y_axis[i].title() in lines.blue_line4:
        line_conjestion['blue_line_4']  += x_axis[i]
    elif y_axis[i].title() in lines.green_line5:
        line_conjestion['green_line_5']  += x_axis[i]
    elif y_axis[i].title() in lines.violet_line6:
        line_conjestion['violet_line_6']  += x_axis[i]
    elif y_axis[i].title() in lines.pink_line7:
        line_conjestion['pink_line_7']  += x_axis[i]
    elif y_axis[i].title() in lines.magenta_line8:
        line_conjestion['magenta_line_8']  += x_axis[i]

print(line_conjestion)

keys = list(line_conjestion.keys())
values = list(line_conjestion.values())
colors = ['red', 'yellow', 'blue', 'blue', 'green', 'violet', 'pink', 'magenta']
plt.title("1st Feb 2024")
plt.xlabel('Lines')
plt.ylabel('Passenger count')
plt.bar(keys, values, width = 0.4, color = colors)
plt.xticks(rotation=90)
plt.show()