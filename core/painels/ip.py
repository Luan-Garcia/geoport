from colorama import Fore
from core.functions import json_to_string, painel
from core.ui import clear, logo, question, title
import nmap3
import shodan
from json import loads
from urllib.request import urlopen 

def start():
    while True:
        clear()
        logo()
        title('Ferramentas IP')
        painel(['Geolocalização de IP', 'Nmap Scan', "Shodan", "Whois", "DNSLytics"])

        resposta1 = int(input('O que você deseja fazer? \n⤷  '))
        
        # Geolocalização de IP
        if resposta1 == 1:
            while True:
                try:
                    ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')
                    
                    if ip == '0':
                        break

                    if ip: 
                        url = f"http://ip-api.com/json/{ip}"

                        request = urlopen(url)
                        data = request.read().decode()

                        data = eval(data)

                        for i in data:
                            print(f"{Fore.RED}{i} == {data[i]}")
                        break
                    else:
                        continue
                    
                except Exception as ex:
                    print(f"{Fore.RED}Error: ({ex})")

        # Nmap Scan
        elif resposta1 == 2:
            while True:
                clear()
                logo()
                title('Nmap Scan')
                painel(['Scan tradicional', 'Descoberta de vulnerabilidades', 'Varredura com ping', 'Descoberta de hosts', 'Varredura de conexão'], sair='Voltar')
                resposta3 = int(input('O que deseja fazer? \n⤷  '))
                
                if resposta3 == 1:
                    nm = input("Digite o IP \n⤷  ")
                    nmap = nmap3.NmapHostDiscovery()
                    results = nmap.nmap_no_portscan(nm)
                    
                    print(json_to_string(results))
                elif resposta3 == 0:
                    break
                else:
                    continue
        # Shodan
        elif resposta1 == 3:
            try:
                shodan_func()
            except Exception as  ex:
                print(f"{Fore.RED}Error: ({ex})")
        # Whois
        elif resposta1 == 4:
            try:
                whois()
            except Exception as  ex:
                print(f"{Fore.RED}Error: ({ex})")
        elif resposta1 == 5:
            continue
        else:
            break

def shodan_func():
    while True:
        clear()
        logo()
        
        ips = input("Insira o endereço de IP: \n⤷  ")
        ips = ip.split(',')

        if ip == '0':
            break

        if ip:
            api_key = input('Insira a sua API key, você pode obte-la em account.shodan.io \n⤷')
            
            if len(api_key):
                break
            
            api = shodan.Shodan(api_key)

            for ip in ips:
                try:
                    results = api.host(ip)
                    print("Portas abertas para:")
                    for port in results['ports']:
                        print(port)
                except shodan.APIError as e:
                    print(f"Error: {e}")

            question()
    

def whois():
    ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')

    if ip:
        url = f"https://ipwhois.app/json/{ip}"
        
        request = urlopen(url)
        data = loads(request.read().decode())

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
        question()