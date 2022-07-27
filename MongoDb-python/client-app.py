

# Socket programlama ile server tarafının kodlanmasının ardından client tarafını da kodlayarak bağlantı başlatılır.
# Bunun için yine önceki kütüphane dahil edilip ardından bağlanacak IP ve portu belirlenir.
# Son olarak bağlantı kurularak karşıdan gelen mesaj ekrana yazdırılır.

# Client tarafını yazarken ek olarak 'recv()' fonksiyonu ile mesajın tampon boyutunun (buffer size) ayarlanması gerekiyor.
# Böylece bir sn de alınacak maksimum dosya boyutunu byte cinsinden ayarlanmış olur.
# Bu boyut ayarlanırken değerin 2 nin üssü şeklinde olmasına dikkat edilir. (Örneğin 1024, 2048, 4096…)
#

import socket


# Socket oluşturma
s=socket.socket()


# Bağlanılacak adres ve port
host="localhost"
port=12345

# Bağlantı yapılır
s.connect((host,port))

# Serverdan yanıt al
yanit=s.recv(1024)
print(yanit.decode("utf-8"))

#Bağlantıyı sonlandır
s.close()

