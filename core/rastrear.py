import requests
from colorama import Fore
from core import ui
import json
from core.functions import json_to_string

with open('./apis.json', 'r') as file:
    data = json.load(file)

def cep(cep):
    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    if req.items():
        print(json_to_string(req))

        return req
    else:
        print(f"{Fore.RED}Nenhuma informação encontrada ou erro na consulta.")
    
def cpf(cpf, base):
    
    if base == 1:
        url = f'{data.get('CPF1')}{cpf}'
    if base == 2:
        url = f'{data.get('CPF2')}{cpf}'
    
    response = requests.get(url)

    if response.status_code == 200:
        print(json_to_string(response.json()))

        return response.json()
    else:
        return None  # Nenhuma informação encontrada ou erro na consulta
    
def numero(numero):
    url = f'{data.get('NUMBER')}{numero}'

    response = requests.get(url)
    if response.status_code == 200:
        print(json_to_string(response.json()))

        return response.json()
    else:
        return None  # Nenhuma informação encontrada ou erro na consulta

def name(name):
    url = f'{data.get('NAME')}{name}'

    response = requests.get(url)
    if response.status_code == 200 or response.json().status == True:
        retorno = json_to_string(response.json())
        if len(retorno) > 2500:
            ui.title("Consulta extensa (Selecione 2 para salvar e ver completo)")
        else:
            print(retorno)
        
        return response.json()
    else:
        return None  # Nenhuma informação encontrada ou erro na consulta