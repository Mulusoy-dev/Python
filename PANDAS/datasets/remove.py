import pymongo


myclient=pymongo.MongoClient("") # SERVER bağlantısı için 

mydb=myclient["train-db"]                                                                                                    # train-db isminde bir veritabanı arar, bulamazsa oluşturur
mycollection = mydb["TTS-information"]


mycollection.delete_many({})




