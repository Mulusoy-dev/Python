import pandas as pd

# Dosyada hakkındaki bilgiler
df = pd.read_csv("C:/Users/melih/Desktop/Python/PANDAS/datasets/IMDBdata_MainData_poster_refresh.csv")


# İlk 5 kaydı gösterin
select_data=df.head(5)


# ilk 10 kaydı gösterin
select_data=df.head(10)


# Son 5 kaydı gösterin
select_data=df.tail(5)


# Sadece title sütununu alın.
#select_data=df.loc[:,"title"]
select_data=df["title"]


# Sadece title sütununu içeren ilk 5 kaydı alın
select_data=df["title"].head(5)


# Sadece title ve rated sütununu içeren ilk 5 kaydı alın.
select_data=df[["title","rated"]].head(5)


# Sadece title ve rated sütununu içeren son 7 kaydı alın
select_data=df[["title","rated"]].tail(7)


# Sadece title ve rated sütununu içeren ikinci 5 kaydı alın.
select_data=df.loc[5:9,["title","rated"]]


# Sadece title ve rated sütununu içeren ve imdb puanı 'PG-13' olan kayıtlardan ilk 50 tanesini alın.
#filter = df[df["rated"] == "PG-13"][["title","rated"]].head(50)
#final_list=filter[["title","rated"]]


# Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
filter = df.query("year >= 2014 & year <= 2015")["title"]


print(df)
print(filter)

#print(select_data)