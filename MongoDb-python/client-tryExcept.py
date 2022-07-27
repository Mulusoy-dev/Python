

import socket
from time import sleep

# Soketi yapılandır ve Server'a bağlan
clientSocket = socket.socket()
host = socket.gethostname()
port = 25000
clientSocket.connect((host, port))

# Bağlantı durumunu takip et
connected = True
print("Server'a bagli")

while True:
    # Veri gönderip almaya çalış, aksi takdirde yeniden bağlan
    try:
        message = clientSocket.recv(1024).decode("UTF-8")
        #clientSocket.send(bytes("Client wave", "UTF-8"))
        print( message )
    except socket.error:
        # Bağlantı durumunu ayarla ve soketi yeniden oluştur
        connected = False
        clientSocket = socket.socket()
        print("Bağlanti kaybi... yeniden bağlaniliyor")
        while not connected:
            # Yeniden bağlanmayı dene, aksi takdirde 2 saniye uyu
            try:
                clientSocket.connect((host, port))
                connected = True
                print("Yeniden bağlanma başarili")
            except socket.error:
                sleep(2)
clientSocket.close();
