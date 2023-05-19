# Scanner de vulnerabilite
# Ce projet consiste a scanner les ports d'une adresse Ip

import socket

Multiport=True # choisir soit scanner un seul port ou plusieur 
port=80     # Le seul port a scanner
tabport=[80,433,20,21] # Le tableau de port a scanner


host = socket.gethostname()
ip = socket.gethostbyname(host)
print("You're host Name is: "+ host ,"\nYou're Ip adress is: "+ ip)

if Multiport:
    for port in tabport:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if s.connect_ex((ip,port)):
            print("Port "+str(port)+" Ferme")
        else:
            print("Scan port valider le port:"+str(port)+"est ouvert")
        s.close()    
    exit(0)        
else:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if s.connect_ex((ip,port)):
        print("Port"+str(port)+" Ferme")
        s.close()
        exit(1)
    else:
        print("Scan port valider le port:"+str(port)+"est ouvert")
        s.close()
        exit(0)




