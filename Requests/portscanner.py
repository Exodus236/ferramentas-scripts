import socket
import time

def request():
    ip=input("Passe o ip do dominio\n>> ")
    ports=[21,22,23,25,53,80,443,445,8000,8080,22222,65000]
    for port in ports:
        code=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code.settimeout(0.3)
        code2=code.connect_ex((ip,port))
        time.sleep(0.3)
        if code2 == 0:
            print(f"Port {port} -> Open")
        elif code2 == 11:
            print(f"Port {port} -> Closed")

request()
