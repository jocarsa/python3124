import requests
import re

url = 'https://www.hanami8.com/'
respuesta = requests.get(url).text
patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(patron, respuesta)
print(emails)



