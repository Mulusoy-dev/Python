
import pymongo
#from bson.objectid import ObjectId




#myclient=pymongo.MongoClient()   



#myclient=pymongo.MongoClient("mongodb://localhost:27017")                  #Yerel Server bağlantısı ve işlemleri için 

mydb=myclient["node-app"]                                                   #node-app isminde bir collection arar, bulamazsa oluşturur

#print(myclient.list_database_names())                                      #localhost veritabanlarını görüntülemek için


mycollection=mydb["products"]                                               #products isminde bir collection oluşturuldu

#print(mydb.list_collection_names())                                        #collection listesini görüntüler


# productList=[                                                               #productList isminde bir ürünler listesi alınsın

#         {"name":"Samsung1","price":"8500","description":"good"},                                  
#         {"name":"Samsung2","price":"9000","categories":['telephone','electronic']},
        
    

# ]




#result = mycollection.insert_many(productList)                             #girilen ürün bilgisi insert_one komutu ile mycollection değişkenine eklendi
#print(result.inserted_ids)

#result=mycollection.find_one()                                             #bulduğu ilk kaydı getirir
#print(result)

#for i in mycollection.find():                                              #tüm bilgiler gelir
#        print(i)

#for i in mycollection.find({"name":"Samsung1"},{"_id":0}):
#        print(i)

#result=mycollection.find_one({"_id": ObjectId("62b96bb44b1629caade46e4f")})
       
#print(result)



#result=mycollection.find({

#        "name" : {
#                "$in" : ["Samsung1","Samsung2"]
#        }       
#})

#for i in result:
#        print(i)




#result=mycollection.find({

#        "price": {
#                "$gte": "8500"
#        }

#})


# result=mycollection.find({

#         "name":{"$regex":"^S"}
        
# })

# for i in result:
#         print(i)


result=mycollection.find().sort('name')                                #alfabetik olarak sıralandı
result=mycollection.find().sort('price')                               #artan sıraya göre sıralandı

for i in result:
        print(i)





















