import pandas as pd

df = dataFrame = pd.read_csv("C:/Users/melih/Desktop/Python/PANDAS/datasets/Players.csv")


df = df.dropna()                                                       # NaN olan verilerin silinmesi işlemi
print(df.columns)                                                      # sütunlar listeleme işlemi


df["Player"] = df["Player"].str.upper()                                # Player sütununda bulunan tüm kayıtlar büyük harf olur
df["Player"] = df["Player"].str.lower()                                # Player sütununda bulunan tüm kayıtlar küçük harf olur
print(df)



# Veri Arama ve Filtreleme İşlemi
data_filter1 = df[df["Player"].str.contains('jordan')]                 # 1. Yöntem: İçinden sadece 'jordan' geçen kayıtları getirir

data_filter2 = df[df.Player.str.contains('jordan')]                    # 2. Yöntem: 1. yöntem ile aynı görevi yapar
print(data_filter2)
