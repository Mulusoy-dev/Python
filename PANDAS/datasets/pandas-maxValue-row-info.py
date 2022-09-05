
import pandas

dataFrame = pandas.read_csv("/Users/melih/Desktop/Python/PANDAS/datasets/weather_data.csv")
# print(dataFrame)
# print(dataFrame["temp"])

data_dict = dataFrame.to_dict()
# print(data_dict['day'])


temp_list = dataFrame["temp"].to_list()
# print(f"Sum of list: {sum(temp_list)}")
# print(f"Average of list: {sum(temp_list)/(len(temp_list))}")

# method 2:
# print(f"Average of list method 2: {dataFrame['temp'].mean()}")


# max value of list
# print(f"Maximum value of list: {dataFrame['temp'].max()}")



print(f"Max value of Data: {dataFrame.temp.max()}")
maxRow = dataFrame.temp.idxmax()
print(f"Max value data row information: {maxRow}")



