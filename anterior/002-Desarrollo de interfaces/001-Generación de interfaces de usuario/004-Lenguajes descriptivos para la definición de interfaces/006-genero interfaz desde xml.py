# pip install lxml
from lxml import etree
import tkinter as tk

ventana = tk.Tk()

arbol = etree.parse('interfaz2.xml')
raiz = arbol.getroot()

print(raiz.tag)

for elemento in raiz:
    elementotemporal = None
    if elemento.tag == "label":
        elementotemporal = tk.Label(ventana,text=elemento.text)
    elif elemento.tag == "entry":
        elementotemporal = tk.Entry(ventana)
    elif elemento.tag == "button":
        elementotemporal = tk.Button(ventana,text=elemento.text)
    elementotemporal.pack(padx=10,pady=10)

ventana.mainloop()

