from colorama import Fore
import re
import os
import json

def salvar_consulta(nome_arquivo, text):
    if not os.path.exists("consultas"):
        os.makedirs("consultas")

    caminho_completo = os.path.join('consultas', nome_arquivo)

    with open(caminho_completo, "w") as arquivo:
        json.dump(text, arquivo, indent=4)

def json_to_string(data, prefix=""):
    result = []
    try:
        if isinstance(data, dict):
            for key, value in data.items():
                full_key = f"{prefix}{key}" if prefix else key
                if isinstance(value, dict) or isinstance(value, list):
                    result.append(f"{Fore.BLUE}{full_key}:")
                    result.append(json_to_string(value, prefix=""))
                else:
                    result.append(f"{Fore.GREEN}{full_key} == {value}")
        
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                # result.append(json_to_string(item, prefix=f"{Fore.GREEN}{prefix}[{idx+1}]\n"))
                result.append(f"{idx + 1}:")
                result.append(json_to_string(item, prefix=""))
        else:
            result.append(f"{prefix} == {data}")
    except Exception as ex:
        return ex
    
    return "\n".join(result)

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
    return True

def validate_number(number):
    padrao = re.compile(r'^\+?\d{1,3}?\s?\(?\d{2,3}\)?\s?\d{4,5}-?\d{4}$')
    return bool(padrao.match(number))

def painel(items, sair='Sair'):
    formatted_items = [
        f"{Fore.GREEN}[{index+1}]{Fore.WHITE} {item}"
        for index,
        item in enumerate(items)
    ]
    result = "\n".join(formatted_items)

    print(f"""{result}
{Fore.RED}[0]{Fore.WHITE} {sair}\n""")
    
def input_text(text, text2=''):
    b = Fore.BLUE
    c = Fore.WHITE

    if (len(text2) >= 1):
        text2 = f'{b}({c}{text2}{b}){c}'

    text = f'''{b}┌[{c}{text}{b}]{c} {text2}
{b}└>{c}  '''
    return text

