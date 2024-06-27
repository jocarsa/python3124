import tkinter as tk
from tkinter import Menu
import ttkbootstrap as ttk

def pulsaBoton():
    print("Voy a insertar un nombre en el archivo")
    archivo = open("nombres.txt",'a')
    archivo.write(nuevo_nombre.get()+"\n")
    archivo.close()
def obtieneRegistros():
    print("Obtengo los registros")
    archivo = open("nombres.txt",'r')
    contenido = archivo.readlines()
    caja_texto.delete('1.0', tk.END)
    for linea in contenido:
        caja_texto.insert(tk.END, linea+"\n")

ventana = tk.Tk()

mimenu = Menu(ventana)
ventana.config(menu=mimenu)
acciones = Menu(mimenu, tearoff=0)
acciones.add_command(label="Listar registros")
acciones.add_command(label="Nuevo registro")
acciones.add_command(label="Actualizar registro")
acciones.add_command(label="Eliminar registro")
acciones.add_command(label="Guardar registros en el disco")
acciones.add_command(label="Leer registros del disco")
mimenu.add_cascade(label="Archivo", menu=acciones)



ventana.mainloop()
