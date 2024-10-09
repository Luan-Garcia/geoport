# bibliotecas
from colorama import Fore
from cryptography.fernet import Fernet
import sys
from core.painels import ip, phishing, malware, rastrear
from core.functions import painel
from core.ui import clear, logo, title

def main():
    resposta = int(input('O que deseja?\n⤷ '))

    # IP Functions
    if resposta == 1:
        clear()
        logo()
        ip.start()

    # Phishing
    elif resposta == 2:
        clear()
        logo()
        phishing.start()
    
    # Malware
    elif resposta == 3:
        clear()
        logo()
        malware.start()

    # Rastrear
    elif resposta == 4:
        clear()
        logo()
        rastrear.start()
    
    elif resposta == 0:
        sys.exit()
    else:
        clear()
        return

if __name__ == '__main__':
    clear()

    while True:
        try:
            clear()
            logo()
            painel(['Ferramentas IP', 'Phishing', 'Criar Malware', 'Rastrear Alvo'])
            main()

        except Exception as ex:
            clear()
            title(f'{Fore.RED}Ocorreu um erro tente novamente!\n{ex}')
            continue