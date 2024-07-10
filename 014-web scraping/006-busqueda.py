import requests
from lxml import etree

url = "https://jocarsa.com"
respuesta = requests.get(url).text 

procesador = etree.HTMLParser()
arbol = etree.fromstring(respuesta, procesador)

titulos = arbol.findall(".//h4")
for titulo in titulos:
    print(titulo.text)
