# Socket modülü dahil edilir.

import socket

# Server adres bilgileri için lazım olacak IP ve port numaralarını belirlenir.
# Bu örnekte hem server hem client çalışma pc olacağı için server IP adresi 127.0.0.1 yani localhost olacaktır.
#
# 127.0.0.1 adresi bilgisayarın yerel IP adresidir. Bu adres yalnızca bilgisayar içerisinde yer alan web sunucusu veya yazılımlar tarafından kullanılır.
# Tamamıyla bilgisayarınız üzerinde yer alan bir adres olması nedeniyle bu adres diğer bilgisayarlarla veya ağlarla iletişim kurmaya açık değildir.


host="localhost"
port=12345


# İlk socket oluşturulur.

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket oluşturuldu")

s.bind((host,port))
print("socket {} nolu porta bağlandı".format(port))

# socket(family, type) yapısı:
#      'family' parametresi  AF_UNIX -> UNIX domain protokolleri
#                            AF_INET -> TCP ve UDP için IPv4 protokolleri
#                            AF_INET6 -> TCP ve UDP için IPv6 protokolleri
# değişkenlerini alabilir. 

#       'type' parametresi  SOCK_STREAM -> TCP bağlantı tipi
#                           SOCK_DGRAM -> UDP bağlantı tipi
#                           SOCK_RAW -> Henüz olgunlaşmamış soketler
#                           SOCK_RDM -> Güvenilir datagramlar için
#                           SOCK_SEQPACKET -> Bağlantı üzerinden kayıtlar için bir dizi transfer.
# değişkenlerini alabilir.


# Bu örnekte TCP bağlantı tipini ve IPv4 adresleme seçeneği kullanıldı. 


# Bağlantı kuruldu ve SERVER kanalı dinlemeye geçer.
 

s.listen(5)              # Aynı anda en fazla 5 bağlantıya izin verildiği belirtilmiştir.
print("socket dinleniyor")


# Sıradaki işlem bağlantıları kabul etmek ve bir client bağlandığı zaman ona 'send()' fonksiyonu ile küçük bir mesaj göndermek olabilir. 

 
while True:

    # Client ile bağlantı kurulmak istenirse
    c, addr = s.accept()
    print('Gelen bağlantı: ',addr)

    # Client tarafına mesaj gönderelim.
    msg="My first message"
    msg2="My second message\n"
    msg3="My third message"
    msg_list=[msg,msg2,msg3]

    for i in msg_list:
        c.send(i.encode('utf-8'))   
                            
    
    #c.send(msg2.encode('utf-8'))
    
    # Bağlantı sonlandırma
    # c.close()


