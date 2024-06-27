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

marcolistar = ttk.LabelFrame(ventana, text="Listado de registros")
marcolistar.pack(padx=20,pady=20)
tk.Label(marcolistar,text="Hola")

marcoinsertar = ttk.LabelFrame(ventana, text="Insertar registro")
marcoinsertar.pack(padx=20,pady=20)
tk.Label(marcoinsertar,text="Hola")

marcoactualizar = ttk.LabelFrame(ventana, text="Actualizar registro")
marcoactualizar.pack(padx=20,pady=20)
tk.Label(marcoactualizar,text="Hola")

marcoeliminar = ttk.LabelFrame(ventana, text="Eliminar registro")
marcoeliminar.pack(padx=20,pady=20)
tk.Label(marcoeliminar,text="Hola")

ventana.mainloop()
