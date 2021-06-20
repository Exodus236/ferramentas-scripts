
#!/usr/bin/env python3
import requests
import time
import os

def requi():
    alvo=input("alvo: ")
    arquivo=open("wordlist.txt", "r")
    for cada in arquivo:
        request=alvo + cada
        requisicao=requests.get(request)
        print(requisicao.status_code)
        if requisicao.status_code == 404:
            print("404 Off -> :( ")
        elif requisicao.status_code == 200:
            print("200  On -> :) !!!!")
        elif requisicao.status_code == 403:
            print("403 -> On (Forbidden) !!")
        elif requisicao.status_code == 301:
            print("301 -> On (Redirect) !!")
        else:
            print("...")

requi()
