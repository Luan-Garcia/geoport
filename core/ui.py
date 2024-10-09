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

def title(nome):
    print(f"{Fore.BLUE}{nome : ^60}{Fore.RESET}")

def question():
    print(f"""
    {Fore.GREEN}[1]{Fore.WHITE} Realizar outra consulta
    {Fore.BLUE}[0] Voltar{Fore.WHITE}""")
    
    return int(input(f'⤷  '))

# def menu_nmap():
#     clear()
#     logo()
#     print(f"""
#     {Fore.GREEN}[1]{Fore.WHITE} Scan tradicional
#     {Fore.GREEN}[2]{Fore.WHITE} Descoberta de vulnerabilidades
#     {Fore.GREEN}[3]{Fore.WHITE} Varredura com ping
#     {Fore.GREEN}[4]{Fore.WHITE} Descoberta de hosts
#     {Fore.GREEN}[5]{Fore.WHITE} Varredura de conexão
#     {Fore.RED}[0]{Fore.WHITE} Sair
#     """)