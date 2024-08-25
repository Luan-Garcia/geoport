import requests
from colorama import Fore
from urllib.request import urlopen 
from core import ui
import nmap
from nmap import PortScanner
import os
import json
from json import loads
from requests import get
import shodan

def cep(cep):
    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    if req.items():
        for key, value in req.items():
            print(f'{Fore.RED}{key} == {value}')
    else:
        print(f"{Fore.RED}Nenhuma informação encontrada ou erro na consulta.")
    
def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * len(cpf):
        return False
    
    def calculate_digit(cpf, digit_position):
        weights = list(range(digit_position, 1, -1))
        sum_digits = sum(int(digit) * weight for digit, weight in zip(cpf, weights))
        remainder = sum_digits % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf[:9], 10)
    if int(cpf[9]) != first_digit:
        return False

    second_digit = calculate_digit(cpf[:10], 11)
    if int(cpf[10]) != second_digit:
        return False

    return True

def validate_cep(cep):
    # Remove qualquer caractere que não seja dígito
    cep = ''.join(filter(str.isdigit, cep))

    # Verifica se o CEP tem exatamente 8 dígitos
    if len(cep) != 8:
        return False

    # Regras adicionais poderiam ser implementadas aqui, por exemplo,
    # validar se o CEP pertence a uma faixa válida de códigos postais no Brasil.
    return True

def cpf(cpf, base):
    if base == 1:
        url = f"https://centralbroxys.net/apis/cadsus/cpf.php?token=@BINGSIXBOT&cpf={cpf}"
    if base == 2:
        url = f"https://centralbroxys.net/apis/siregi/cpf.php?token=@BINGSIXBOT&cpf={cpf}"
    
    response = requests.get(url)

    if response.status_code == 200:
        if base == 1:
            return response.json()
        if base == 2:
            return response.json()['dados']
    else:
        return None  # Nenhuma informação encontrada ou erro na consulta

def nmap():
    ui.menu_nmap()
    resposta3 = int(input('O que deseja fazer? \n⤷  '))
    if resposta3 == 1:
        nm = PortScanner(input("Digite o IP \n ⤷"))
        info = nm.scan("129.168.0.19")
        print(info)

def shodan_func():
    ui.clear
    ui.logo
    
    ips = input("Insira o endereço de IP: \n⤷  ")

    ips = ips.split(',')
    api_key = input('Insira a sua API key, você pode obte-la em account.shodan.io \n⤷')

    api = shodan.Shodan(api_key)

    for ip in ips:
        try:
            results = api.host(ip)
            print("Portas abertas para:")
            for port in results['ports']:
                print(port)
        except shodan.APIError as e:
            print(f"Error: {e}")
    ui.question
    
def whois():
    Ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')

    if Ip:
        url = f"https://ipwhois.app/json/{Ip}"

        request = urlopen(url)

        data = request.read().decode()

        data = json.loads(data)

        print(f"{Fore.RED}IP: {data['ip']}")
        print(f"{Fore.RED}Type: {data['type']}")
        print(f"{Fore.RED}Continent: {data['continent']}")
        print(f"{Fore.RED}Country: {data['country']}")
        print(f"{Fore.RED}Country Capital: {data['country_capital']}")
        print(f"{Fore.RED}Region: {data['region']}")
        print(f"{Fore.RED}City: {data['city']}")
        print(f"{Fore.RED}Country Phone: {data['country_phone']}")
        print(f"{Fore.RED}Latitude: {data['latitude']}")
        print(f"{Fore.RED}Longitude: {data['longitude']}")
        print(f"{Fore.RED}Organização: {data['org']}")
        print(f"{Fore.RED}ISP: {data['isp']}")
        print(f"{Fore.RED}Timezone: {data['timezone']}")
        ui.question()

def pergunta():
    resposta1 = int(input('O que você deseja fazer? \n⤷  '))
    if resposta1 == 1:
        try:
            Ip()
        except Exception as  ex:
            print(f"{Fore.RED}Error: ({ex})")
    if resposta1 == 2:
        nmap()
    if resposta1 == 3:
        try:
            shodan_func()
        except Exception as  ex:
            print(f"{Fore.RED}Error: ({ex})")
    if resposta1 == 4:
        try:
            whois()
        except Exception as  ex:
            print(f"{Fore.RED}Error: ({ex})")
    
def Ip():
    ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')
    
    if ip: 
        url = f"http://ip-api.com/json/{ip}"

        request = urlopen(url)
        data = request.read().decode()

        data = eval(data)

        for i in data:
            print(f"{Fore.RED}{i} == {data[i]}")
        
        ui.question()
    else:
        return None