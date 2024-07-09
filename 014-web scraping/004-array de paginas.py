import requests
import re

paginas = [
    'https://www.hanami8.com/',
    'https://ara-tech.es/',
    'https://www.coderland.com/',
    'https://www.sortlist.es/',
    'https://isvisoft.com/',
    'https://focusoft.es/',
    'https://programacionamedidavalencia.es/',
    'https://phios.group/'
    ]
for pagina in paginas:
    try:
        url = pagina
        respuesta = requests.get(url).text
        patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(patron, respuesta)
        print(emails)
    except:
        print("error")



