import pandas as pd
import time
import os
import win32com.client

# ilk dinamik değişen excel uygulaması - Pandas 

# os.startfile("C:/Users/melih/Desktop/exchange.xlsx")

# win32com kullanarak Excel yazılımını açma
File = win32com.client.Dispatch("Excel.Application")# 

# Belirlenen Excel'i açma
Workbook = File.Workbooks.open("C:/Users/melih/Desktop/exchange.xlsx")

# Tüm çalışma sayfalarını yenile
# Workbook.RefreshAll()

# Çalışma sayfasını kaydetme
# Workbook.Save()

# Excel dosyasını kapatma
# File.Quit()




while True:
    
    df = dataFrame = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
    print(df)
    Workbook.Save()
    time.sleep(30)

# user_select = df["Satış"]
# print(user_select)


