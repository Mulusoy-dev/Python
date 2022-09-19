import pandas as pd
import pymongo
import time, datetime
import os

## Mongo client
myclient=pymongo.MongoClient() # SERVER bağlantısı için 

mydb=myclient["train-db"]                                                                                                    # train-db isminde bir veritabanı arar, bulamazsa oluşturur
mycollection = mydb["exchange_information"]                                                                                  # exchange-information isminde bir collection ekler                                                                                       


# print(myclient.list_database_names())                           # veritabanlarını listeler                                                             
# print(mydb.list_collection_names())                             # koleksiyonları listeler                                               


df = pd.read_excel("C:/Users/melih/Desktop/exchange.xlsx")
print(df)




# os stat bilgileri 
excel_status = os.stat("C:/Users/melih/Desktop/exchange.xlsx")
# print(excel_status)


fileSize = (excel_status.st_size/1024)                                                 # Dosya Boyutu (Kb)
# print(f'File Size: {fileSize} Kb')


create_file_date=datetime.datetime.fromtimestamp(excel_status.st_ctime)                # Dosya oluşturulma tarihi
# print(f'File creation date: {create_file_date}')


access_file_date=datetime.datetime.fromtimestamp(excel_status.st_atime)                # Dosyaya en son erişilme tarihi
# print(f'File access date: {access_file_date}')


modify_file_date=datetime.datetime.fromtimestamp(excel_status.st_mtime)                # Dosya değiştirlme tarihi 
# print(f'File modification date: {modify_file_date}')





exchange_data = [
    {
        "Time Information":
        {
            "Dosya boyutu (Kb)": str(fileSize) + "Kb",
            "Dosya oluşturulma tarihi": str(create_file_date),
            "Dosyaya en son erişilme tarihi": str(access_file_date),
            "Dosya değiştirlme tarihi": str(modify_file_date)
        },


        "Dolar":
            {
            "Dolar Alış": df["Alış"].to_dict()[0],
            "Dolar Satış": df["Satış"].to_dict()[0],  
            "En Yüksek": df["Yüksek"].to_dict()[0],
            "Dolar Düşük": df["Düşük"].to_dict()[0],
            "Dolar Değişim": df["Değişim"].to_dict()[0],
            },

        "Euro":
            {
            "Euro Alış": df["Alış"].to_dict()[1],
            "Euro Satış": df["Satış"].to_dict()[1],  
            "En Yüksek": df["Yüksek"].to_dict()[1],
            "Euro Düşük": df["Düşük"].to_dict()[1],
            "Euro Değişim": df["Değişim"].to_dict()[1],
            },

        "Sterlin":
            {
            "Sterlin Alış": df["Alış"].to_dict()[2],
            "Sterlin Satış": df["Satış"].to_dict()[2],  
            "En Yüksek": df["Yüksek"].to_dict()[2],
            "Sterlin Düşük": df["Düşük"].to_dict()[2],
            "Sterlin Değişim": df["Değişim"].to_dict()[2],
            },

        "İsviçre Frangı":
            {
            "İsviçre Frangı Alış": df["Alış"].to_dict()[3],
            "İsviçre Frangı Satış": df["Satış"].to_dict()[3],  
            "En Yüksek": df["Yüksek"].to_dict()[3],
            "İsviçre Frangı Düşük": df["Düşük"].to_dict()[3],
            "İsviçre Frangı Değişim": df["Değişim"].to_dict()[3],
            },

        "Kanada Doları":
            {
            "Kanada Doları Alış": df["Alış"].to_dict()[4],
            "Kanada Doları Satış": df["Satış"].to_dict()[4],  
            "En Yüksek": df["Yüksek"].to_dict()[4],
            "Kanada Doları Düşük": df["Düşük"].to_dict()[4],
            "Kanada Doları Değişim": df["Değişim"].to_dict()[4],
            },

        "Rus Rublesi":
            {
            "Rus Rublesi Alış": df["Alış"].to_dict()[5],
            "Rus Rublesi Satış": df["Satış"].to_dict()[5],  
            "En Yüksek": df["Yüksek"].to_dict()[5],
            "Rus Rublesi Düşük": df["Düşük"].to_dict()[5],
            "Rus Rublesi Değişim": df["Değişim"].to_dict()[5],
            },

        "Birleşik Arap Emirlikleri Dirhemi":
            {
            "Birleşik Arap Emirlikleri Dirhemi Alış": df["Alış"].to_dict()[6],
            "Birleşik Arap Emirlikleri Dirhemi Satış": df["Satış"].to_dict()[6],  
            "En Yüksek": df["Yüksek"].to_dict()[6],
            "Birleşik Arap Emirlikleri Dirhemi Düşük": df["Düşük"].to_dict()[6],
            "Birleşik Arap Emirlikleri Dirhemi Değişim": df["Değişim"].to_dict()[6],
            },

        "Avustralya Doları":
            {
            "Avustralya Doları Alış": df["Alış"].to_dict()[7],
            "Avustralya Doları Satış": df["Satış"].to_dict()[7],  
            "En Yüksek": df["Yüksek"].to_dict()[7],
            "Avustralya Doları Düşük": df["Düşük"].to_dict()[7],
            "Avustralya Doları Değişim": df["Değişim"].to_dict()[7],
            },

        "Danimarka Kronu":
            {
            "Danimarka Kronu Alış": df["Alış"].to_dict()[8],
            "Danimarka Kronu Satış": df["Satış"].to_dict()[8],  
            "En Yüksek": df["Yüksek"].to_dict()[8],
            "Danimarka Kronu Düşük": df["Düşük"].to_dict()[8],
            "Danimarka Kronu Değişim": df["Değişim"].to_dict()[8],
            },
        
        "İsveç Kronu":
            {
            "İsveç Kronu Alış": df["Alış"].to_dict()[9],
            "İsveç Kronu Satış": df["Satış"].to_dict()[9],  
            "En Yüksek": df["Yüksek"].to_dict()[9],
            "İsveç Kronu Düşük": df["Düşük"].to_dict()[9],
            "İsveç Kronu Değişim": df["Değişim"].to_dict()[9],
            },

        "Norveç Kronu":
            {
            "Norveç Kronu Alış": df["Alış"].to_dict()[10],
            "Norveç Kronu Satış": df["Satış"].to_dict()[10],  
            "En Yüksek": df["Yüksek"].to_dict()[10],
            "Norveç Kronu Düşük": df["Düşük"].to_dict()[10],
            "Norveç Kronu Değişim": df["Değişim"].to_dict()[10],
            },

        "100 Japon Yeni":
            {
            "100 Japon Yeni Alış": df["Alış"].to_dict()[11],
            "100 Japon Yeni Satış": df["Satış"].to_dict()[11],  
            "En Yüksek": df["Yüksek"].to_dict()[11],
            "100 Japon Yeni Düşük": df["Düşük"].to_dict()[11],
            "100 Japon Yeni Değişim": df["Değişim"].to_dict()[11],
            },

        "Kuveyt Dinarı":
            {
            "Kuveyt Dinarı Alış": df["Alış"].to_dict()[12],
            "Kuveyt Dinarı Satış": df["Satış"].to_dict()[12],  
            "En Yüksek": df["Yüksek"].to_dict()[12],
            "Kuveyt Dinarı Düşük": df["Düşük"].to_dict()[12],
            "Kuveyt Dinarı Değişim": df["Değişim"].to_dict()[12],
            },

        "Güney Afrika Randı":
            {
            "Güney Afrika Randı Alış": df["Alış"].to_dict()[13],
            "Güney Afrika Randı Satış": df["Satış"].to_dict()[13],  
            "En Yüksek": df["Yüksek"].to_dict()[13],
            "Güney Afrika Randı Düşük": df["Düşük"].to_dict()[13],
            "Güney Afrika Randı Değişim": df["Değişim"].to_dict()[13],
            },

        "Bahreyn Dinarı":
            {
            "Bahreyn Dinarı Alış": df["Alış"].to_dict()[14],
            "Bahreyn Dinarı Satış": df["Satış"].to_dict()[14],  
            "En Yüksek": df["Yüksek"].to_dict()[14],
            "Bahreyn Dinarı Düşük": df["Düşük"].to_dict()[14],
            "Bahreyn Dinarı Değişim": df["Değişim"].to_dict()[14],
            },
        
        "Libya Dinarı":
            {
            "Libya Dinarı Alış": df["Alış"].to_dict()[15],
            "Libya Dinarı Satış": df["Satış"].to_dict()[15],  
            "En Yüksek": df["Yüksek"].to_dict()[15],
            "Libya Dinarı Düşük": df["Düşük"].to_dict()[15],
            "Libya Dinarı Değişim": df["Değişim"].to_dict()[15],
            },

        "Suudi Arabistan Riyali":
            {
            "Suudi Arabistan Riyali Alış": df["Alış"].to_dict()[16],
            "Suudi Arabistan Riyali Satış": df["Satış"].to_dict()[16],  
            "En Yüksek": df["Yüksek"].to_dict()[16],
            "Suudi Arabistan Riyali Düşük": df["Düşük"].to_dict()[16],
            "Suudi Arabistan Riyali Değişim": df["Değişim"].to_dict()[16],
            },
        
        "Irak Dinarı":
            {
            "Irak Dinarı Alış": df["Alış"].to_dict()[17],
            "Irak Dinarı Satış": df["Satış"].to_dict()[17],  
            "En Yüksek": df["Yüksek"].to_dict()[17],
            "Irak Dinarı Düşük": df["Düşük"].to_dict()[17],
            "Irak Dinarı Değişim": df["Değişim"].to_dict()[17],
            },

        "İsrail Şekeli":
            {
            "İsrail Şekeli Alış": df["Alış"].to_dict()[18],
            "İsrail Şekeli Satış": df["Satış"].to_dict()[18],  
            "En Yüksek": df["Yüksek"].to_dict()[18],
            "İsrail Şekeli Düşük": df["Düşük"].to_dict()[18],
            "İsrail Şekeli Değişim": df["Değişim"].to_dict()[18],
            },

        "İran Riyali":
            {
            "İran Riyali Alış": df["Alış"].to_dict()[19],
            "İran Riyali Satış": df["Satış"].to_dict()[19],  
            "En Yüksek": df["Yüksek"].to_dict()[19],
            "İran Riyali Düşük": df["Düşük"].to_dict()[19],
            "İran Riyali Değişim": df["Değişim"].to_dict()[19],
            },

        "Hindistan Rupisi":
            {
            "Hindistan Rupisi Alış": df["Alış"].to_dict()[20],
            "Hindistan Rupisi Satış": df["Satış"].to_dict()[20],  
            "En Yüksek": df["Yüksek"].to_dict()[20],
            "Hindistan Rupisi Düşük": df["Düşük"].to_dict()[20],
            "Hindistan Rupisi Değişim": df["Değişim"].to_dict()[20],
            },

        "Meksika Pesosu":
            {
            "Meksika Pesosu Alış": df["Alış"].to_dict()[21],
            "Meksika Pesosu Satış": df["Satış"].to_dict()[21],  
            "En Yüksek": df["Yüksek"].to_dict()[21],
            "Meksika Pesosu Düşük": df["Düşük"].to_dict()[21],
            "Meksika Pesosu Değişim": df["Değişim"].to_dict()[21],
            },

        "Macar Forinti":
            {
            "Macar Forinti Alış": df["Alış"].to_dict()[22],
            "Macar Forinti Satış": df["Satış"].to_dict()[22],  
            "En Yüksek": df["Yüksek"].to_dict()[22],
            "Macar Forinti Düşük": df["Düşük"].to_dict()[22],
            "Macar Forinti Değişim": df["Değişim"].to_dict()[22],
            },

        "Yeni Zelanda Doları":
            {
            "Yeni Zelanda Doları Alış": df["Alış"].to_dict()[23],
            "Yeni Zelanda Doları Satış": df["Satış"].to_dict()[23],  
            "En Yüksek": df["Yüksek"].to_dict()[23],
            "Yeni Zelanda Doları Düşük": df["Düşük"].to_dict()[23],
            "Yeni Zelanda Doları Değişim": df["Değişim"].to_dict()[23],
            },
        
        "Brezilya Reali":
            {
            "Brezilya Reali Alış": df["Alış"].to_dict()[24],
            "Brezilya Reali Satış": df["Satış"].to_dict()[24],  
            "En Yüksek": df["Yüksek"].to_dict()[24],
            "Brezilya Reali Düşük": df["Düşük"].to_dict()[24],
            "Brezilya Reali Değişim": df["Değişim"].to_dict()[24],
            },

        "Endonezya Rupiahi":
            {
            "Endonezya Rupiahi Alış": df["Alış"].to_dict()[25],
            "Endonezya Rupiahi Satış": df["Satış"].to_dict()[25],  
            "En Yüksek": df["Yüksek"].to_dict()[25],
            "Endonezya Rupiahi Düşük": df["Düşük"].to_dict()[25],
            "Endonezya Rupiahi Değişim": df["Değişim"].to_dict()[25],
            },

        "Çek Korunası":
            {
            "Çek Korunası Alış": df["Alış"].to_dict()[26],
            "Çek Korunası Satış": df["Satış"].to_dict()[26],  
            "En Yüksek": df["Yüksek"].to_dict()[26],
            "Çek Korunası Düşük": df["Düşük"].to_dict()[26],
            "Çek Korunası Değişim": df["Değişim"].to_dict()[26],
            },

        "Polonya Zlotisi":
            {
            "Polonya Zlotisi Alış": df["Alış"].to_dict()[27],
            "Polonya Zlotisi Satış": df["Satış"].to_dict()[27],  
            "En Yüksek": df["Yüksek"].to_dict()[27],
            "Polonya Zlotisi Düşük": df["Düşük"].to_dict()[27],
            "Polonya Zlotisi Değişim": df["Değişim"].to_dict()[27],
            },

        "Romanya Leyi":
            {
            "Romanya Leyi Alış": df["Alış"].to_dict()[28],
            "Romanya Leyi Satış": df["Satış"].to_dict()[28],  
            "En Yüksek": df["Yüksek"].to_dict()[28],
            "Romanya Leyi Düşük": df["Düşük"].to_dict()[28],
            "Romanya Leyi Değişim": df["Değişim"].to_dict()[28],
            },

        "Çin Yuanı":
            {
            "Çin Yuanı Alış": df["Alış"].to_dict()[29],
            "Çin Yuanı Satış": df["Satış"].to_dict()[29],  
            "En Yüksek": df["Yüksek"].to_dict()[29],
            "Çin Yuanı Düşük": df["Düşük"].to_dict()[29],
            "Çin Yuanı Değişim": df["Değişim"].to_dict()[29],
            },

        "Arjantin Pesosu":
            {
            "Arjantin Pesosu Alış": df["Alış"].to_dict()[30],
            "Arjantin Pesosu Satış": df["Satış"].to_dict()[30],  
            "En Yüksek": df["Yüksek"].to_dict()[30],
            "Arjantin Pesosu Düşük": df["Düşük"].to_dict()[30],
            "Arjantin Pesosu Değişim": df["Değişim"].to_dict()[30],
            },

        "Arnavutluk Leki":
            {
            "Arnavutluk Leki Alış": df["Alış"].to_dict()[31],
            "Arnavutluk Leki Satış": df["Satış"].to_dict()[31],  
            "En Yüksek": df["Yüksek"].to_dict()[31],
            "Arnavutluk Leki Düşük": df["Düşük"].to_dict()[31],
            "Arnavutluk Leki Değişim": df["Değişim"].to_dict()[31],
            },

        "Azerbaycan Manatı":
            {
            "Azerbaycan Manatı Alış": df["Alış"].to_dict()[32],
            "Azerbaycan Manatı Satış": df["Satış"].to_dict()[32],  
            "En Yüksek": df["Yüksek"].to_dict()[32],
            "Azerbaycan Manatı Düşük": df["Düşük"].to_dict()[32],
            "Azerbaycan Manatı Değişim": df["Değişim"].to_dict()[32],
            },

        "Bosna-Hersek Markı":
            {
            "Bosna-Hersek Markı Alış": df["Alış"].to_dict()[33],
            "Bosna-Hersek Markı Satış": df["Satış"].to_dict()[33],  
            "En Yüksek": df["Yüksek"].to_dict()[33],
            "Bosna-Hersek Markı Düşük": df["Düşük"].to_dict()[33],
            "Bosna-Hersek Markı Değişim": df["Değişim"].to_dict()[33],
            },

        "Şili Pesosu":
            {
            "Şili Pesosu Alış": df["Alış"].to_dict()[34],
            "Şili Pesosu Satış": df["Satış"].to_dict()[34],  
            "En Yüksek": df["Yüksek"].to_dict()[34],
            "Şili Pesosu Düşük": df["Düşük"].to_dict()[34],
            "Şili Pesosu Değişim": df["Değişim"].to_dict()[34],
            },

        "Kolombiya Pesosu":
            {
            "Kolombiya Pesosu Alış": df["Alış"].to_dict()[35],
            "Kolombiya Pesosu Satış": df["Satış"].to_dict()[35],  
            "En Yüksek": df["Yüksek"].to_dict()[35],
            "Kolombiya Pesosu Düşük": df["Düşük"].to_dict()[35],
            "Kolombiya Pesosu Değişim": df["Değişim"].to_dict()[35],
            },

        "Kostarika Kolonu":
            {
            "Kostarika Kolonu Alış": df["Alış"].to_dict()[36],
            "Kostarika Kolonu Satış": df["Satış"].to_dict()[36],  
            "En Yüksek": df["Yüksek"].to_dict()[36],
            "Kostarika Kolonu Düşük": df["Düşük"].to_dict()[36],
            "Kostarika Kolonu Değişim": df["Değişim"].to_dict()[36],
            },

        "Cezayir Dinarı":
            {
            "Cezayir Dinarı Alış": df["Alış"].to_dict()[37],
            "Cezayir Dinarı Satış": df["Satış"].to_dict()[37],  
            "En Yüksek": df["Yüksek"].to_dict()[37],
            "Cezayir Dinarı Düşük": df["Düşük"].to_dict()[37],
            "Cezayir Dinarı Değişim": df["Değişim"].to_dict()[37],
            },

        "Mısır Lirası":
            {
            "Mısır Lirası Alış": df["Alış"].to_dict()[38],
            "Mısır Lirası Satış": df["Satış"].to_dict()[38],  
            "En Yüksek": df["Yüksek"].to_dict()[38],
            "Mısır Lirası Düşük": df["Düşük"].to_dict()[38],
            "Mısır Lirası Değişim": df["Değişim"].to_dict()[38],
            },

        "Hong Kong Doları":
            {
            "Hong Kong Doları Alış": df["Alış"].to_dict()[39],
            "Hong Kong Doları Satış": df["Satış"].to_dict()[39],  
            "En Yüksek": df["Yüksek"].to_dict()[39],
            "Hong Kong Doları Düşük": df["Düşük"].to_dict()[39],
            "Hong Kong Doları Değişim": df["Değişim"].to_dict()[39],
            },

        "Hırvat Kunası":
            {
            "Hırvat Kunası Alış": df["Alış"].to_dict()[40],
            "Hırvat Kunası Satış": df["Satış"].to_dict()[40],  
            "En Yüksek": df["Yüksek"].to_dict()[40],
            "Hırvat Kunası Düşük": df["Düşük"].to_dict()[40],
            "Hırvat Kunası Değişim": df["Değişim"].to_dict()[40],
            },

        "İzlanda Kronası":
            {
            "İzlanda Kronası Alış": df["Alış"].to_dict()[41],
            "İzlanda Kronası Satış": df["Satış"].to_dict()[41],  
            "En Yüksek": df["Yüksek"].to_dict()[41],
            "İzlanda Kronası Düşük": df["Düşük"].to_dict()[41],
            "İzlanda Kronası Değişim": df["Değişim"].to_dict()[41],
            },

        "Ürdün Dinarı":
            {
            "Ürdün Dinarı Alış": df["Alış"].to_dict()[42],
            "Ürdün Dinarı Satış": df["Satış"].to_dict()[42],  
            "En Yüksek": df["Yüksek"].to_dict()[42],
            "Ürdün Dinarı Düşük": df["Düşük"].to_dict()[42],
            "Ürdün Dinarı Değişim": df["Değişim"].to_dict()[42],
            },

        "Güney Kore Wonu":
            {
            "Güney Kore Wonu Alış": df["Alış"].to_dict()[43],
            "Güney Kore Wonu Satış": df["Satış"].to_dict()[43],  
            "En Yüksek": df["Yüksek"].to_dict()[43],
            "Güney Kore Wonu Düşük": df["Düşük"].to_dict()[43],
            "Güney Kore Wonu Değişim": df["Değişim"].to_dict()[43],
            },

        "Kazak Tengesi":
            {
            "Kazak Tengesi Alış": df["Alış"].to_dict()[44],
            "Kazak Tengesi Satış": df["Satış"].to_dict()[44],  
            "En Yüksek": df["Yüksek"].to_dict()[44],
            "Kazak Tengesi Düşük": df["Düşük"].to_dict()[44],
            "Kazak Tengesi Değişim": df["Değişim"].to_dict()[44],
            },

        "Lübnan Lirası":
            {
            "Lübnan Lirası Alış": df["Alış"].to_dict()[45],
            "Lübnan Lirası Satış": df["Satış"].to_dict()[45],  
            "En Yüksek": df["Yüksek"].to_dict()[45],
            "Lübnan Lirası Düşük": df["Düşük"].to_dict()[45],
            "Lübnan Lirası Değişim": df["Değişim"].to_dict()[45],
            },

        "Sri Lanka Rupisi":
            {
            "Sri Lanka Rupisi Alış": df["Alış"].to_dict()[46],
            "Sri Lanka Rupisi Satış": df["Satış"].to_dict()[46],  
            "En Yüksek": df["Yüksek"].to_dict()[46],
            "Sri Lanka Rupisi Düşük": df["Düşük"].to_dict()[46],
            "Sri Lanka Rupisi Değişim": df["Değişim"].to_dict()[46],
            },

        "Fas Dirhemi":
            {
            "Fas Dirhemi Alış": df["Alış"].to_dict()[47],
            "Fas Dirhemi Satış": df["Satış"].to_dict()[47],  
            "En Yüksek": df["Yüksek"].to_dict()[47],
            "Fas Dirhemi Düşük": df["Düşük"].to_dict()[47],
            "Fas Dirhemi Değişim": df["Değişim"].to_dict()[47],
            },

        "Moldovya Leusu":
            {
            "Moldovya Leusu Alış": df["Alış"].to_dict()[48],
            "Moldovya Leusu Satış": df["Satış"].to_dict()[48],  
            "En Yüksek": df["Yüksek"].to_dict()[48],
            "Moldovya Leusu Düşük": df["Düşük"].to_dict()[48],
            "Moldovya Leusu Değişim": df["Değişim"].to_dict()[48],
            },

        "Makedon Dinarı":
            {
            "Makedon Dinarı Alış": df["Alış"].to_dict()[49],
            "Makedon Dinarı Satış": df["Satış"].to_dict()[49],  
            "En Yüksek": df["Yüksek"].to_dict()[49],
            "Makedon Dinarı Düşük": df["Düşük"].to_dict()[49],
            "Makedon Dinarı Değişim": df["Değişim"].to_dict()[49],
            },
        
        "Malezya Ringgiti":
            {
            "Malezya Ringgiti Alış": df["Alış"].to_dict()[50],
            "Malezya Ringgiti Satış": df["Satış"].to_dict()[50],  
            "En Yüksek": df["Yüksek"].to_dict()[50],
            "Malezya Ringgiti Düşük": df["Düşük"].to_dict()[50],
            "Malezya Ringgiti Değişim": df["Değişim"].to_dict()[50],
            },

        "Umman Riyali":
            {
            "Umman Riyali Alış": df["Alış"].to_dict()[51],
            "Umman Riyali Satış": df["Satış"].to_dict()[51],  
            "En Yüksek": df["Yüksek"].to_dict()[51],
            "Umman Riyali Düşük": df["Düşük"].to_dict()[51],
            "Umman Riyali Değişim": df["Değişim"].to_dict()[51],
            },

        "Peru İnti":
            {
            "Peru İnti Alış": df["Alış"].to_dict()[52],
            "Peru İnti Satış": df["Satış"].to_dict()[52],  
            "En Yüksek": df["Yüksek"].to_dict()[52],
            "Peru İnti Düşük": df["Düşük"].to_dict()[52],
            "Peru İnti Değişim": df["Değişim"].to_dict()[52],
            },

        "Filipinler Pesosu":
            {
            "Filipinler Pesosu Alış": df["Alış"].to_dict()[53],
            "Filipinler Pesosu Satış": df["Satış"].to_dict()[53],  
            "En Yüksek": df["Yüksek"].to_dict()[53],
            "Filipinler Pesosu Düşük": df["Düşük"].to_dict()[53],
            "Filipinler Pesosu Değişim": df["Değişim"].to_dict()[53],
            },

        "Pakistan Rupisi":
            {
            "Pakistan Rupisi Alış": df["Alış"].to_dict()[54],
            "Pakistan Rupisi Satış": df["Satış"].to_dict()[54],  
            "En Yüksek": df["Yüksek"].to_dict()[54],
            "Pakistan Rupisi Düşük": df["Düşük"].to_dict()[54],
            "Pakistan Rupisi Değişim": df["Değişim"].to_dict()[54],
            },

        "Katar Riyali":
            {
            "Katar Riyali Alış": df["Alış"].to_dict()[55],
            "Katar Riyali Satış": df["Satış"].to_dict()[55],  
            "En Yüksek": df["Yüksek"].to_dict()[55],
            "Katar Riyali Düşük": df["Düşük"].to_dict()[55],
            "Katar Riyali Değişim": df["Değişim"].to_dict()[55],
            },

        "Sırbistan Dinarı":
            {
            "Sırbistan Dinarı Alış": df["Alış"].to_dict()[56],
            "Sırbistan Dinarı Satış": df["Satış"].to_dict()[56],  
            "En Yüksek": df["Yüksek"].to_dict()[56],
            "Sırbistan Dinarı Düşük": df["Düşük"].to_dict()[56],
            "Sırbistan Dinarı Değişim": df["Değişim"].to_dict()[56],
            },

        "Singapur Doları":
            {
            "Singapur Doları Alış": df["Alış"].to_dict()[57],
            "Singapur Doları Satış": df["Satış"].to_dict()[57],  
            "En Yüksek": df["Yüksek"].to_dict()[57],
            "Singapur Doları Düşük": df["Düşük"].to_dict()[57],
            "Singapur Doları Değişim": df["Değişim"].to_dict()[57],
            },

        "Suriye Lirası":
            {
            "Suriye Lirası Alış": df["Alış"].to_dict()[58],
            "Suriye Lirası Satış": df["Satış"].to_dict()[58],  
            "En Yüksek": df["Yüksek"].to_dict()[58],
            "Suriye Lirası Düşük": df["Düşük"].to_dict()[58],
            "Suriye Lirası Değişim": df["Değişim"].to_dict()[58],
            },

        "Tayland Bahtı":
            {
            "Tayland Bahtı Alış": df["Alış"].to_dict()[59],
            "Tayland Bahtı Satış": df["Satış"].to_dict()[59],  
            "En Yüksek": df["Yüksek"].to_dict()[59],
            "Tayland Bahtı Düşük": df["Düşük"].to_dict()[59],
            "Tayland Bahtı Değişim": df["Değişim"].to_dict()[59],
            },

        "Yeni Tayvan Doları":
            {
            "Yeni Tayvan Doları Alış": df["Alış"].to_dict()[60],
            "Yeni Tayvan Doları Satış": df["Satış"].to_dict()[60],  
            "En Yüksek": df["Yüksek"].to_dict()[60],
            "Yeni Tayvan Doları Düşük": df["Düşük"].to_dict()[60],
            "Yeni Tayvan Doları Değişim": df["Değişim"].to_dict()[60],
            },

        "Ukrayna Grivnası":
            {
            "Ukrayna Grivnası Alış": df["Alış"].to_dict()[61],
            "Ukrayna Grivnası Satış": df["Satış"].to_dict()[61],  
            "En Yüksek": df["Yüksek"].to_dict()[61],
            "Ukrayna Grivnası Düşük": df["Düşük"].to_dict()[61],
            "Ukrayna Grivnası Değişim": df["Değişim"].to_dict()[61],
            },

        "Uruguay Pesosu":
            {
            "Uruguay Pesosu Alış": df["Alış"].to_dict()[62],
            "Uruguay Pesosu Satış": df["Satış"].to_dict()[62],  
            "En Yüksek": df["Yüksek"].to_dict()[62],
            "Uruguay Pesosu Düşük": df["Düşük"].to_dict()[62],
            "Uruguay Pesosu Değişim": df["Değişim"].to_dict()[62],
            },
            
        "Gürcistan Larisi":
            {
            "Gürcistan Larisi Alış": df["Alış"].to_dict()[63],
            "Gürcistan Larisi Satış": df["Satış"].to_dict()[63],  
            "En Yüksek": df["Yüksek"].to_dict()[63],
            "Gürcistan Larisi Düşük": df["Düşük"].to_dict()[63],
            "Gürcistan Larisi Değişim": df["Değişim"].to_dict()[63],
            },

        "Tunus Dinarı":
            {
            "Tunus Dinarı Alış": df["Alış"].to_dict()[64],
            "Tunus Dinarı Satış": df["Satış"].to_dict()[64],  
            "En Yüksek": df["Yüksek"].to_dict()[64],
            "Tunus Dinarı Düşük": df["Düşük"].to_dict()[64],
            "Tunus Dinarı Değişim": df["Değişim"].to_dict()[64],
            },

        "Bulgar Levası":
            {
            "Bulgar Levası Alış": df["Alış"].to_dict()[65],
            "Bulgar Levası Satış": df["Satış"].to_dict()[65],  
            "En Yüksek": df["Yüksek"].to_dict()[65],
            "Bulgar Levası Düşük": df["Düşük"].to_dict()[65],
            "Bulgar Levası Değişim": df["Değişim"].to_dict()[65],
            },


    }
]

print(exchange_data)



                                                                                 
my_data = mycollection.insert_many(exchange_data)                                # insert_many metodu ile çoklu veri seti girişi yapılır.
                                                                                 # insert_one metodu ile tek bir veri seti girişi yapılır. 
print(my_data.inserted_ids)                                                      # eklenen objenin veri tabanı numarası




