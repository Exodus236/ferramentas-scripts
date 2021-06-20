
#!/usr/bin/env python3 
 
import time
import sys
import os 
import requests 
import paramiko
import getpass


def ssh():
    alvo=input("passe o ip do SSH: ")
    usuario=input("Passe o usuario: ")
    senha=getpass.getpass("Passe a senha: ")
    porta=input("Passe a porta: ")
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=f"{alvo}",port=f"{porta}",username=f"{usuario}",password=f"{senha}")
        cmd=input("Passe o comando $: ")
        stdin, stdout, stderr = ssh.exec_command(f'{cmd} \n')
        print(stdout.readlines())
    except paramiko.ssh_exception.AuthenticationException:
        print("Erro de autenticacao")
        time.sleep(0.5)
        print("Tentando se reconectar")
        ssh.connect(hostname=f"{alvo}",username=f"{usuario}",password=f"{senha}")
        cmd=input("Passe comando $: ")
        stdin, stdout, stderr = ssh.exec_command(f"{cmd} \n")
        print(stdout.readlines())

ssh()
