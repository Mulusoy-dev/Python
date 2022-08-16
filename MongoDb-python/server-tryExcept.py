

import socket  
from time import sleep  


# Yerel ana bilgisayarda soket oluştur ve yapılandır  
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = socket.gethostname()                                                # Aynı cihaz üzerinden kullanılıyorsa 'gethostname()' metodu kullanılır.   
port = 25000                                                               # Geçici port  
serverSocket.bind( ( host, port ) )  
serverSocket.listen( 1 )  
 
 
print( "istemciye bağlantisi basarili" )  
con, addr = serverSocket.accept()

while True:
    
    print(f"Bağlantı adresi {addr}")  
    # Istemci(Client)'a veri gönder  
    con.send( bytes( "User Information", "UTF-8" ) )  
  
    # Istemciden veri al  
    #message = con.recv( 1024 ).decode( "UTF-8" )  
    #print( message )  
  
    # 1 saniye bekle  
    sleep( 1 )
con.close()