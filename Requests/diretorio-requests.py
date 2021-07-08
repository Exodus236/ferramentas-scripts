#!/usr/bin/env python3
import requests
import time
import os

def requi():
    alvo=input("alvo: ")
    wordl=input("Nome da wordlist: ")
    arquivo=open(f"{wordl}", "r")
    for cada in arquivo:
        request=alvo + cada
        requisicao=requests.get(request)
        print(requisicao.status_code)
        if requisicao.status_code == 404:
            print(f"{cada} 404 Off -> :( ")
        elif requisicao.status_code == 200:
            print(f"{cada} 200  On -> :) !!!!")
        elif requisicao.status_code == 403:
            print(f"{cada} 403 -> On (Forbidden) !!")
        elif requisicao.status_code == 301:
            print(f"{cada} 301 -> On (Redirect) !!")
        else:
            print("...")

requi()
