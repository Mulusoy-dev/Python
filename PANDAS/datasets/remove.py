import pymongo


myclient=pymongo.MongoClient("mongodb+srv://melih:ZuyL3IyzsGY9a2MV@cluster0.tokxl.mongodb.net/?retryWrites=true&w=majority") # SERVER bağlantısı için 

mydb=myclient["train-db"]                                                                                                    # train-db isminde bir veritabanı arar, bulamazsa oluşturur
mycollection = mydb["TTS-information"]


mycollection.delete_many({})




