import pandas as pd
import time, datetime
import os
import win32com.client
import datetime


# win32com kullanarak Excel yazılımını açma
File = win32com.client.Dispatch("Excel.Application") 


# Belirlenen Excel'i açma
Workbook = File.Workbooks.open("C:/Users/melih/Desktop/exchange.xlsx")



def same_value():
    global is_same
    df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
    if df["Alış"].to_dict()[0] == temp:
        print("Please start program again")
        print(temp)

        # Program must be restart.
        # Delay 



        is_same = False

        



def main():
    global temp
    df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
    temp = df["Alış"].to_dict()[0]
    print(temp)
    print("----------------------------------------------------")
    time.sleep(130)
    Workbook.Save()


is_same = True
while is_same:
    # global is_same
    main()
    same_value()

    
    

















#     exchange_data = [
#     {
#         "Dolar":
#         {
#             "Dolar Alış": df["Alış"].to_dict()[0],
#             "Dolar Satış": df["Satış"].to_dict()[0],  
#             "En Yüksek": df["Yüksek"].to_dict()[0],
#             "Dolar Düşük": df["Düşük"].to_dict()[0],
#             "Dolar Değişim": df["Değişim"].to_dict()[0],
#         },

#         "Euro":
#         {
#             "Euro Alış": df["Alış"].to_dict()[1],
#             "Euro Satış": df["Satış"].to_dict()[1],  
#             "En Yüksek": df["Yüksek"].to_dict()[1],
#             "Euro Düşük": df["Düşük"].to_dict()[1],
#             "Euro Değişim": df["Değişim"].to_dict()[1],
#         },
#     }
# ]
