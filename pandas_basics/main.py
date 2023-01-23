# # First way
# # with open('weather_data.csv') as file:
# #     data = file.readlines()
# # print(data)
#
# # import csv
# # with open('weather_data.csv') as file:
# #     data = csv.DictReader(file)
# #     temperatures = []
# #     for row in data:
# #         temperatures.append(int(row['temp']))
# #
# # print(temperatures)
#
# # second way
# # import csv
# #
# # with open('weather_data.csv') as file:
# #     data = csv.reader(file)
# #     temp = []
# #     for row in data:
# #         temp.append(row[1])
# #
# # print(temp)
# # temp.remove('temp')
# # print(temp)
# # temperatures = []
# # for i in temp:
# #     temperatures.append(int(i))
# #
# # print(temperatures)
#
#
# # Third way
# # import csv
# #
# # with open('weather_data.csv') as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] == 'temp':
# #             pass
# #         else:
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'].mean())
# # print(data['temp'].max())
#
# # print(data[data.temp == data.temp.max()])
#
# print(data[data.day == 'Monday'].temp * 1.8 + 32)



import pandas

data = pandas.read_csv("squirrel_data.csv")
count_data = data['Primary Fur Color'].value_counts()
count_data.to_csv('squirrel_count.csv')