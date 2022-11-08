import pandas as pd
import time, datetime
import os
import win32com.client
import datetime
import subprocess

###########################################################################################


def ISAGRAF_open():
    global open_program
    prog = r"C:/Program Files/LTC/LTspiceXVII/XVIIx64.exe"
    try:
        # 'DEBUG' mouse clicking  
        open_program = subprocess.Popen([prog])
        time.sleep(2)
    except Exception as e:
        print(e)


def ISAGRAF_close():
    prog = r"C:/Program Files/LTC/LTspiceXVII/XVIIx64.exe"
    try:
        open_program.terminate()
        time.sleep(2)
    except Exception as e:
        print(e)

##########################################################################################


def win32_module():
    global Workbook
    # win32com kullanarak Excel yazılımını açma
    File = win32com.client.Dispatch("Excel.Application") 

    # Belirlenen Excel'i açma
    Workbook = File.Workbooks.open("C:/Users/melih/Desktop/exchange.xlsx")



# def openfile():
#     prog = r"C:/Users/mulus/OneDrive/Masaüstü/exchange.xlsx"
#     try:
#         open_program = subprocess.Popen([prog])
#     except Exception as e:
#         print(e)


def stopfile():
    try:
        Workbook.Close(True)     # save the workbook
        time.sleep(2)            # 2 sec wait 
    except Exception as e:
        print(e)



def same_value():
    df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
    if df["Alış"].to_dict()[0] == temp:
        print("Values are equal. Program should be restart.")
        print(temp)
        time.sleep(2)
        ISAGRAF_close()                      # ISAGRAF closed and 2 sec wait
        stopfile()                           # Excel Program is closed and 2 sec wait 

        ISAGRAF_open()                       # ISAGRAF restarted and 2 sec wait
        win32_module()                       # Excel Program is restarted
    else:
        print("Successful")
        

        



def main():
    global temp
    df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
    temp = df["Alış"].to_dict()[0]
    print(temp)
    print("----------------------------------------------------")
    time.sleep(65)
    Workbook.Save()




ISAGRAF_open()
win32_module()



while True:
    
    
    main()
    same_value()

 