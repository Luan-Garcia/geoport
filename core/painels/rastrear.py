from core.ui import clear, logo, title
from core.functions import painel, validate_cep, validate_cpf, validate_number, salvar_consulta
from core import rastrear
from colorama import Fore

def start():    
    while True:
        clear()
        logo()
        title("Rastrear Alvo\n")

        painel(['CEP', 'CPF', 'Número', 'Nome'], 'Voltar')
        response = int(input(f'{Fore.WHITE}Insira a pesquisa que você deseja\n⤷  '))

        # CEP
        if response == 1:
            while True:
                clear()
                logo()
                title("Rastrear Alvo")

                cep = input(f'{Fore.WHITE}Insira um CEP ({Fore.LIGHTBLACK_EX}01001-000{Fore.RESET})\n⤷  ')
                if cep == 0:
                    break

                validate = validate_cep(cep)
                if validate == False:
                    continue
                
                resposta = rastrear.cep(cep)
                painel(['Realizar outra consulta', 'Salvar consulta'], sair='Voltar')
                
                response2 = int(input(f'⤷  '))
                if response2 == 1:
                    clear()
                    continue

                elif response2 == 2:
                
                    salvar_consulta(f'cep_{cep}.txt', resposta)
                    title('Consulta salva com sucesso.\nAperte enter para voltar')
                    input(f'⤷  ')
                    break

                else:
                    clear()
                    break;
        
        # CPF
        elif response == 2:
            while True:
                clear()
                logo()
                title("Rastrear Alvo\n")
                
                cpf = input(f'{Fore.WHITE}Insira um CPF ({Fore.LIGHTBLACK_EX}000.000.000-00{Fore.RESET})\n⤷  ')
                if cpf == 0:
                    break

                validate = validate_cpf(cpf)
                if validate == False:
                    continue
                
                painel(['CADSUS', 'SIREGI'], sair='Voltar')
                base = int(input(f'{Fore.WHITE}\nSelecione a base\n⤷  '))
                if base == 0:
                    break

                result = rastrear.cpf(cpf, base)

                painel(['Realizar outra consulta', 'Salvar consulta'], sair='Voltar')
                
                response2 = int(input(f'⤷  '))
                if response2 == 1:
                    clear()
                    continue

                elif response2 == 2:
                
                    salvar_consulta(f'cpf_{cpf}.txt', result)
                    title('Consulta salva com sucesso.\nAperte enter para voltar')
                    input(f'⤷  ')
                    break
                else:
                    clear()
                    break;
        
        # Number
        elif response == 3:
            while True:
                clear()
                logo()
                title("Rastrear alvo\n")
                
                number = input(f'{Fore.WHITE}Insira um número ({Fore.LIGHTBLACK_EX}00000000000{Fore.RESET})\n⤷  ')
                if number == 0:
                    continue
            
                validate = validate_number(number)
                if validate == False:
                    continue

                result = rastrear.numero(number)
                
                painel(['Realizar outra consulta', 'Salvar consulta'], sair='Voltar')
                response2 = int(input(f'⤷  '))
                if response2 == 1:
                    clear()
                    continue
                elif response2 == 2:
                
                    salvar_consulta(f'number_{number}.txt', result)
                    title('Consulta salva com sucesso.\nAperte enter para voltar')
                    input(f'⤷  ')
                    break
                else:
                    clear()
                    break;
        
        # Nome
        elif response == 4:
            while True:
                clear()
                logo()
                title("Rastrear alvo\n")
                
                name = str(input(f'{Fore.WHITE}Insira um nome:\n⤷  '))
                if name == 0:
                    continue

                result = rastrear.name(name)
                
                painel(['Realizar outra consulta', 'Salvar consulta'], sair='Voltar')
                response2 = int(input(f'⤷  '))
                if response2 == 1:
                    clear()
                    continue
                elif response2 == 2:
                
                    salvar_consulta(f'name_{name}.txt', result)
                    title('Consulta salva com sucesso.\nAperte enter para voltar')
                    input(f'⤷  ')
                    break
                else:
                    clear()
                    break;
        
        elif response == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    