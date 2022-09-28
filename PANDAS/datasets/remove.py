import pymongo


myclient=pymongo.MongoClient("mongodb+srv://melih:bacMwaeP5Z47YG36@cluster0.tokxl.mongodb.net/TTS-information?retryWrites=true&w=majority") # SERVER bağlantısı için 

mydb=myclient["train-db"]                                                                                                    # train-db isminde bir veritabanı arar, bulamazsa oluşturur
mycollection = mydb["TTS-information"]


mycollection.delete_many({})




