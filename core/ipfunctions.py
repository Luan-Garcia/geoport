from urllib.request import urlopen 
from colorama import Fore
import json

def whois():
    Ip = input(f'{Fore.WHITE}Digite o IP\n⤷  ')

    if Ip:
        url = f"https://ipwhois.app/json/{Ip}"

        request = urlopen(url)
        data = json.loads(request.read().decode())

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