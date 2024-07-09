import requests

url = 'https://jocarsa.com'
respuesta = requests.get(url)
print(respuesta.text)
