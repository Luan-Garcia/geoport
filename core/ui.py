from colorama import Fore
import os
import sys

def clear():
    if os.name == 'nt':  # Windows
        os.system("cls")
    else:  # Unix/Linux/MacOS
        os.system("clear")

def logo():
    print(f"""{Fore.RED}
  _______  ______   ______   .______     ______   .______     .___________.
 /  _____||   ____| /  __  \  |   _  \   /  __  \  |   _  \    |           |
|  |  __  |  |__   |  |  |  | |  |_)  | |  |  |  | |  |_)  |   `---|  |----`
|  | |_ | |   __|  |  |  |  | |   ___/  |  |  |  | |      /        |  |     
|  |__| | |  |____ |  `--'  | |  |      |  `--'  | |  |\  \----.   |  |     
 \______| |_______| \______/  | _|       \______/  | _| `._____|   |__|  
          {Fore.WHITE}""")

def menu():
    print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Ferramentas IP.
    {Fore.GREEN}[2]{Fore.WHITE} Phishing
    {Fore.GREEN}[3]{Fore.WHITE} Criar Malware
    {Fore.GREEN}[4]{Fore.WHITE} Obter informações de número
    {Fore.GREEN}[5]{Fore.WHITE} Rastrear Alvo
    {Fore.RED}[0] Sair{Fore.WHITE}""")
    
def title(nome):
    print(f"{Fore.BLUE}{nome : ^60}{Fore.RESET}")

def question():
    print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Realizar outra consulta
    {Fore.BLUE}[0] Voltar{Fore.WHITE}""")
    
    return int(input(f'⤷  '))