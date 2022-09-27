import pandas as pd
import pymongo
import time, datetime
import os


# Mongo client
myclient=pymongo.MongoClient("") # SERVER bağlantısı için 

mydb=myclient["train-db"]                                                                                                    # train-db isminde bir veritabanı arar, bulamazsa oluşturur
mycollection = mydb["TTS-information"]                                                                                  # exchange-information isminde bir collection ekler                                                                                       


#print(myclient.list_database_names())                           # veritabanlarını listeler                                                             
#print(mydb.list_collection_names())                             # koleksiyonları listeler                                               


df = pd.read_excel("C:/Users/melih/Desktop/prototype.xlsx")
#print(df)






# os stat bilgileri 
excel_status = os.stat("C:/Users/melih/Desktop/prototype.xlsx")
#print(excel_status)


fileSize = (excel_status.st_size/1024)                                                 # Dosya Boyutu (Kb)
#print(f'File Size: {fileSize} Kb')


create_file_date=datetime.datetime.fromtimestamp(excel_status.st_ctime)                # Dosya oluşturulma tarihi
#print(f'File creation date: {create_file_date}')


access_file_date=datetime.datetime.fromtimestamp(excel_status.st_atime)                # Dosyaya en son erişilme tarihi
#print(f'File access date: {access_file_date}')


modify_file_date=datetime.datetime.fromtimestamp(excel_status.st_mtime)                # Dosya değiştirlme tarihi 
#print(f'File modification date: {modify_file_date}')




train_dict = df.to_dict(orient="records")
#print(train_dict)



# print(battery_data)


def insert_document(document):
    try:
        mycollection.insert_many(document)
        return True
    except Exception as e:
        print("An exception occurred :", e)
        return False


def main():
    
    catenary_voltage = train_dict[0]["VALUES"]
    output_ac_to_loads_1 = train_dict[1]["VALUES"]
    batt_volt_1 = train_dict[2]["VALUES"]
    output_dc_to_batt_1 = train_dict[3]["VALUES"]
    output_dc_to_loads_1 = train_dict[4]["VALUES"]


    output_ac_to_loads_2 = train_dict[5]["VALUES"]
    batt_volt_2 = train_dict[6]["VALUES"]
    output_dc_to_batt_2 = train_dict[7]["VALUES"]
    output_dc_to_loads_2 = train_dict[8]["VALUES"]
    batt_temperature_A_2 = train_dict[9]["VALUES"]
    batt_temperature_B_2 = train_dict[10]["VALUES"]


    output_ac_to_loads_3 = train_dict[11]["VALUES"] 
    batt_volt_3 = train_dict[12]["VALUES"]
    output_dc_to_batt_3 = train_dict[13]["VALUES"]
    output_dc_to_loads_3 = train_dict[14]["VALUES"]
    batt_temperature_A_3 = train_dict[15]["VALUES"]
    batt_temperature_B_3 = train_dict[16]["VALUES"]


    output_ac_to_loads_4 = train_dict[17]["VALUES"]
    batt_volt_4 = train_dict[18]["VALUES"] 
    output_dc_to_batt_4 = train_dict[19]["VALUES"]
    output_dc_to_loads_4 = train_dict[20]["VALUES"]
    batt_temperature_A_4 = train_dict[21]["VALUES"]
    batt_temperature_B_4 = train_dict[22]["VALUES"]


    battery_data = [
        {
            "Time Information":
            {
                "Dosya boyutu (Kb)": str(fileSize) + "Kb",
                "Dosya oluşturulma tarihi": str(create_file_date),
                "Dosyaya en son erişilme tarihi": str(access_file_date),
                "Dosya değiştirlme tarihi": str(modify_file_date)
            },

            "Battery Informations":
            {
                "Catenary Voltage":catenary_voltage,
                "Output AC to Loads 1":output_ac_to_loads_1,
                "Batt Volt 1":batt_volt_1,
                "Output DC to Batt 1":output_dc_to_batt_1,
                "Output DC to Loads 1":output_dc_to_loads_1,

                "Output AC to Loads 2":output_ac_to_loads_2,
                "Batt Volt 2":batt_volt_2,
                "Output DC to Batt 2":output_dc_to_batt_2,
                "Output DC to Loads 2":output_dc_to_loads_2,
                "Batt temperature(A) 2":batt_temperature_A_2,
                "Batt temperature(B) 2":batt_temperature_B_2,

                "Output AC to Loads 3":output_ac_to_loads_3,
                "Batt Volt 3":batt_volt_3,
                "Output DC to Batt 3":output_dc_to_batt_3,
                "Output DC to Loads 3":output_dc_to_loads_3,
                "Batt temperature(A) 3":batt_temperature_A_3,
                "Batt temperature(B) 3":batt_temperature_B_3,

                "Output AC to Loads 4":output_ac_to_loads_4,
                "Batt Volt 4":batt_volt_4,
                "Output DC to Batt 4":output_dc_to_batt_4,
                "Output DC to Loads 4":output_dc_to_loads_4,
                "Batt temperature(A) 4":batt_temperature_A_4,
                "Batt temperature(B) 4":batt_temperature_B_4,
            }
        }
    ]
    print(insert_document(battery_data))
main()

# my_data = mycollection.insert_many(battery_data)                                # insert_many metodu ile çoklu veri seti girişi yapılır.                                                                               # insert_one metodu ile tek bir veri seti girişi yapılır. 
# print(my_data.inserted_ids)
# print("Connected")
                                                                                   
 

