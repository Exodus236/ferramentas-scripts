#!/usr/bin/python3
##You can change the name this file , and Start with code : python <name.py> or python scan_ss.py
import socket
ip = input("Ip alvo: ")
portas = []
vazia = 0
while vazia < 3:
    portas.append(int(input("porta: ")))
    vazia += 1
for cada in portas:
    neti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    neti.settimeout(0.05)
    cod = neti.connect_ex((ip, port)) 
    if cod == 0:
        print (str(port) + " -> Aberta")
    else:
        print (str(port) + " -> Fechada")


print ("Finalizado ... Script by : (exodus236) -> Silva")
