import pandas as pd
import time
import os
import win32com.client
import datetime


########        ilk dinamik değişen excel uygulaması - Pandas 




# win32com kullanarak Excel yazılımını açma
File = win32com.client.Dispatch("Excel.Application") 


# Belirlenen Excel'i açma
Workbook = File.Workbooks.open("C:/Users/melih/Desktop/exchange.xlsx")



# def dateExcel(path):
#     # os stat bilgileri 
#     excel_status = os.stat(path)
#     # print(excel_status)


#     fileSize = (excel_status.st_size/1024)                                                 # Dosya Boyutu (Kb)
#     print(f'File Size: {fileSize} Kb')


#     create_file_date=datetime.datetime.fromtimestamp(excel_status.st_ctime)                # Dosya oluşturulma tarihi
#     print(f'File creation date: {create_file_date}')


#     access_file_date=datetime.datetime.fromtimestamp(excel_status.st_atime)                # Dosyaya en son erişilme tarihi
#     print(f'File access date: {access_file_date}')


#     modify_file_date=datetime.datetime.fromtimestamp(excel_status.st_mtime)                # Dosya değiştirlme tarihi 
#     print(f'File modification date: {modify_file_date}')


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
    #dateExcel("C:/Users/melih/Desktop/exchange.xlsx")
    time.sleep(30)

# user_select = df["Satış"]
# print(user_select)