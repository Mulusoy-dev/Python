import pandas as pd
import numpy as np

### NOTLAR
# DataFrame: Serilerin birleştirilmesi ile oluşur.
# Projede birden fazla olan excel dosyaları dataFrame'ler kullanarak birleştirilebilir.
# Pandas, DataFrame üzerinde JSON, CSV, XLSX, Database yani heterojen veriler üzerinde aynı anda işlem yapılabilir.



# s1=pd.Series([12,14,16,18,20])
# s2=pd.Series([11,13,15,17,19])
# data=dict(apples=s1, oranges=s2)
# df=pd.DataFrame(data)
# print(df)


# my_dictionary={"Name":["ahmet","ayse","mehmet","veli"],"Grade":[50,75,66,44]}
# print(pd.DataFrame(my_dictionary))

#########################################################################################################

# Satır ve Sütun işlemleri - Excel veya CSV formatından istenilen bilgiyi almak

#df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns = ["column1","column2","column3"])
#print(df)


#select_data = df["column1"]                                                                      # 1. Sütundaki verileri al       (Tek bir sütundan verileri al)
#select_data=df[["column1","column2"]]                                                            # 1. ve 2. Sütundaki verileri al (Çoklu Sütun işlemleri)


# lock metodu ile satır yani index'e göre işlem yapılır.
#### Kural: loc["row","column"]
# Sadece sütun işlemi yapabilmek için loc[:, "columnX"]
#select_data=df.loc["A"]                                                                          # A satırında bulunan tüm elemanlar alınır. (Tek bir satırdan verileri alma)
#select_data=df.loc[:,"column1"]                                                                  # loc ile de sütun işlemleri yapılabilir.


#select_data=df.loc["A","column2"]                                                                #  [1.satır, 2.sütun] - Belirli bir hücredeki veriyi almak için 
#select_data=df.loc["A":"B","column1"]                                                            #  [1.satır ve 2. satır, 1.sütun]
#print(select_data)



# Yeni bir sütun eklemek için, yeni bir seri oluşturulmalı --> pd.Series()
#df["column4"] = pd.Series(randn(3), ["A","B","C"])
#print(df)



# Bir sütun silmek için drop() metodu kullanılır. Silinmesi istenilen sütun ismi drop içine yazılır.
#select_data=df.drop("column4", axis = 1)
#print(select_data)


########################################################################################################

# data = np.random.randint(10,100,75).reshape(15,5)              # 1- ile 100 arasında 75 adet tamsayıyı, 15x5 matris oluşturulması
# df=pd.DataFrame(data, columns= ["column1","column2","column3","column4","column5"])
# print(df)

# result=df.columns                                              # Sütun bilgileri alınır
# result=df.head(6)                                              # İlk 6 kayıt bilgisi alınır
# result=df.tail(6)                                              # Son 6 kayıt bilgisi alınır



# Belirli bir sütun bilgisini almak için

# result=df["column1"].head(4)                                   # 1. Yöntem: 1. Sütundan 4 veri al
# result=df.column1.head(4)                                      # 2. Yöntem                                    



# Birden fazla sütun bilgisi alınması gerekirse

# result=df[["column1","column2"]].head(5)                       # 1. ve 2. Sütundan ilk 5 satır bilgisi alınır
# result=df[["column1","column3"]].tail(5)                       # 1. ve 2. Sütundan son 5 satır bilgisi alınır



# DataFrame parçalama işlemi yapılabilir.

# result=df[0:10]                                              # 0-10 satır arası bilgi alınabilir.
# print(result)

##################################################################################################################
# Filtreleme işlemleri

# filter = df > 60                                               # DataFrame içerisinde tüm değerleri kontrol eder ve şart sağlanırsa 'TRUE' değer döndürür
# filter = df[df > 60]                                           # 60'dan büyük şartını sağlayan değerleri görebilmek için
# filter = df[df % 2 == 0]                                       # 2'ye bölümünden kalan 0 şartını sağlayan değerleri görebilmek için
# filter = df[df["column2"] > 60][["column2"]]                   # 2. Sütunda 60'dan büyük şartını sağlayan değerleri görebilmek için

## Filtreleme işlemleri için kullanılan diğer yöntem: QUERY

# filter = df.query("column1 >= 50 & column1 % 2 == 0")          # 1. Sütundaki elemanların 50'den büyük ve 2'ye bölümünden kalan 0'a eşit olan elemanları al
# print(filter)                                                               

##################################################################################################################