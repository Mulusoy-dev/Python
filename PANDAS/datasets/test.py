import pandas as pd
import time
import os
import win32com.client
import datetime
import pymongo


########        ilk dinamik değişen excel uygulaması - Pandas 


# win32com kullanarak Excel yazılımını açma
#File = win32com.client.Dispatch("Excel.Application") 


# Belirlenen Excel'i açma
#Workbook = File.Workbooks.open("C:/Users/melih/Desktop/exchange.xlsx")
#Workbook2 = File.Workbooks.open("C:/Users/melih/Desktop/gold.xlsx")



#### Neden json formatına ihtiyaç var?   MongoDb yalnızca JSON, CSV ve TSV dosyalarını destekler. 

#### NOT: MongoDb, server kısmını ifade eder. (Mongodb server tabanlı bir veri tabanıdır.)

### MongoDb



my_client = pymongo.MongoClient("mongodb+srv://melih:ciRblHYkusvVbYEB@cluster0.tokxl.mongodb.net/?retryWrites=true&w=majority") 
# Bağlantı için  "Connect your application" işaretlendi.  

print(my_client.list_database_names())
# Uzak bilgisayardaki veritabanlarını listeler.





























# while True:
    
#     df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
#     js = df.to_json(orient = 'columns')
#     print(df)
#     print(js)
#     # df2 = pd.read_excel("C:/Users/melih/Desktop/gold.xlsx")
#     # print(df2)
#     print("----------------------------------------------------")
#     # dateExcel("C:/Users/melih/Desktop/exchange.xlsx")
#     time.sleep(45)
#     Workbook.Save()
#     # Workbook2.Save()
    
