import requests
from lxml import etree

url = "https://www.google.com/search?q=empresas+programacion+valencia&sca_esv=b716066298432941&hl=es&sxsrf=ADLYWILzVGcEbw1OXvThsa6kmdFN9lCs7g:1720522852525&udm=1&sa=X&ved=2ahUKEwignc-L55mHAxXWRaQEHQhBC3IQjGp6BAhfEAE&biw=1536&bih=793&dpr=1.25"
respuesta = requests.get(url).text 

procesador = etree.HTMLParser()
arbol = etree.fromstring(respuesta, procesador)

class_name = "yYlJEf"
titulos = arbol.xpath(f"//*[@class='{class_name}']")

for titulo in titulos:
    print(f"Tag: {titulo.tag}, Text: {titulo.text}, Class: {titulo.get('class')}")
