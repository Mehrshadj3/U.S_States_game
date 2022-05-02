#with open('weather_data.csv', 'r') as weather:
#    print(weather.readlines())

import csv

with open('weather_data.csv','r') as weather:
    data = csv.reader(weather)
    temps = []
    for i in data:

         temps.append((i[1]))
    temps.remove('temp')

    print(temps)


import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data['temp'].to_list()
print(temp_list)

print(data['temp'])
print(data.condition)


monday = (data[data.day == 'monday'])
print(monday)

#creat dataframe:

data1 = pandas.DataFrame()
data1.to_csv('new_data.csv')

















