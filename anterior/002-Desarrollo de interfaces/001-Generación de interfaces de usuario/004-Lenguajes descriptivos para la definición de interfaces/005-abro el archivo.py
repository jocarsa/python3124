# pip install lxml
from lxml import etree

arbol = etree.parse('interfaz.xml')
raiz = arbol.getroot()

print(raiz.tag)

for elemento in raiz:
    print(elemento.tag, elemento.text)



