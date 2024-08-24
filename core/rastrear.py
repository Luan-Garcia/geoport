import requests
from colorama import Fore
from urllib.request import urlopen 
from core import ui

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
    
def Ip(ip):
    
    url = f"http://ip-api.com/json/{ip}"

    request = urlopen(url)
    data = request.read().decode()

    data = eval(data)

    for i in data:
        print(f"{Fore.RED}{i} == {data[i]}")
    
    