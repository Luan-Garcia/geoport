# Importar a biblioteca Requests pra raspagem de dados
import requests

# Colorama pra estilizar
from colorama import Fore, Back

def main_phishing():
	print(f"""{Fore.BLUE}
Qual ação de Phishing deseja fazer
-- 1 -- Analisar URL
-- 2 -- Analisar Email
-- 3 -- Analisar SMS
{Fore.WHITE}""")
	
	input_acao = input("Qual ação de Phishing você deseja fazer: ")
	
	def site_phishing():
		# Função para analisar se é Phishing
		def check_openphish(url):
			# Analisar a lista de APIs do OpenPish
			api_url = 'https://openphish.com/feed.txt'
			resposta = requests.get(api_url)
			urls_phishing = resposta.text.split(" ")
			
			# Checar se a URL está na lista do OpenPhish
			if url in urls_phishing:
				return True
			return False
		
		# A URL que o usuario deseja analisar
		URL = input('Qual a URL que deseja analisar: ')
		
		# Chamar a função
		is_phishing = check_openphish(URL)
		
		# Se for Phishing...
		if is_phishing:
				print(f"""{Fore.RED} {Back.WHITE}------------------------------------------------------------------A URL {URL} é um site de Pishing--------------------------------------------------------------------------------------""")
		else:
			# Se não for Phishing...
			print(f"""{Fore.BLUE}{Back.GREEN}------------------------------------------------------------------A URL {URL} não é um site de Pishing----------------------------------------------------------------------------------
""")
	
	# Checagem de email
	def email_phishing():
		# Definir um input de multiplas linhas
		def multi_line_input(prompt):
		    print(prompt)
		    lines = []
		    while True:
		        line = input()
		        if line:
		            lines.append(line)
		        else:
		            break
		    return ' '.join(lines)
		
		# Função para analisar o email
		def check_email(email):
			# Palavras que podem indicar Phishing
			palavras_phish = [".exe", ".apk", ".zip", "login", "senha", "password"]
			# Checar se alguma das palavras esta no email
			for palavra in palavras_phish:
				if palavra in email:
					return True
				return False
		
		# Chamar o input de multiplas linhas
		corpo_email = multi_line_input("Corpo do email(Aperte enter em uma linha vazia para finalizar: ")
		# Chamar a função
		is_phishing_email = check_email(corpo_email)
		# Se não tiver...
		if is_phishing_email:
			print(f"""{Fore.GREEN} O email é confiavel""")
		else:
			# Se tiver...
			print(f"""{Fore.RED} Potencialmente perigoso""")
	
	# Checagem de SMS
	def sms_phishing():
		# Definir um input de multiplas linhas
		def multi_line_input(prompt):
		    print(prompt)
		    lines = []
		    while True:
		        line = input()
		        if line:
		            lines.append(line)
		        else:
		            break
		    return ' '.join(lines)
		
		# Função para analisar o SMS
		def check_sms(sms):
			# Palavras que podem indicar Phishing
			palavras_phish = [".exe", ".apk", ".zip", "login", "senha", "password"]
			# Checar se alguma das palavras esta no email
			for palavra in palavras_phish:
				if palavra in sms:
					return True
				return False
		
		# Chamar o input de multiplas linhas
		corpo_sms = multi_line_input("Corpo do SMS(Aperte enter em uma linha vazia para finalizar: ")
		# Chamar a função
		is_phishing_sms = check_sms(corpo_sms)
		# Se não tiver...
		if is_phishing_sms:
			print(f"""{Fore.RED} Potencialmente perigoso""")
		else:
			# Se tiver...
			print(f"""{Fore.GREEN} O email é confiavel""")
	
	
	def ataque_phishing():
			print(f"{Fore.RED}Você escolheu ataque de Phishing, isso é ilegal! Não faça isso, por favor!")
			
	
	
	
	if '1' in input_acao:
		site_phishing()
	elif '2' in input_acao:
		email_phishing()
	elif '3' in input_acao:
		sms_phishing()
	elif '4' in input_acao:
		ataque_phishing()
	else:
		print(f"{Fore.YELLOW}~~Ação invalida~~")
