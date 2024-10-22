from core.ui import clear, logo, title, question

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
        URL = input('Qual a URL que deseja analisar⤷ ')
        		
        # Chamar a função
        is_phishing = check_openphish(URL)
        
        # Se for Phishing...
        if is_phishing:
        	print(f"{Fore.RED}AURL {URL} é um site de Pishing""")
        else:
            # Se não for Phishing...
        	print(f"{Fore.GREEN}A URL {URL} não é um site de Pishing")

def start():
    while True:
        clear()
        logo()
        title("Pishing - Ações\n")

        print("""
        [1] Verificar URL
        [2] Analisar email
        [3] Analisar SMS
        [4] Ataque Phishing
        """)
        
        input_acao = int(input("Selecione uma ação de Phishing⤷ "))

        if input_acao == 1:
            site_phishing()

        response = question()
        if response == 1:
            clear()
            continue
        else:
            clear()
            break

