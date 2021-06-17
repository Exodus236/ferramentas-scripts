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
            print("Off -> :( ")
        elif requisicao.status_code == 200:
            print("Diretorio vivo -> :) !!!!")
        else:
            print("Nao Entendido")

requi()