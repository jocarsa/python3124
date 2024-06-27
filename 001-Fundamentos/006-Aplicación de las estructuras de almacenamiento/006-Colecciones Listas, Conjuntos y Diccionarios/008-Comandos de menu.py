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
        
def muestraListar():
    print("ok")
    marcolistar.pack(padx=20, pady=20)
    marcoinsertar.pack_forget()
    marcoactualizar.pack_forget()
    marcoeliminar.pack_forget()

def muestraInsertar():
    marcoinsertar.pack(padx=20, pady=20)
    marcolistar.pack_forget()
    marcoactualizar.pack_forget()
    marcoeliminar.pack_forget()

def muestraActualizar():
    marcoactualizar.pack(padx=20, pady=20)
    marcolistar.pack_forget()
    marcoinsertar.pack_forget()
    marcoeliminar.pack_forget()

def muestraEliminar():
    marcoeliminar.pack(padx=20, pady=20)
    marcolistar.pack_forget()
    marcoinsertar.pack_forget()
    marcoactualizar.pack_forget()
ventana = tk.Tk()

mimenu = Menu(ventana)
ventana.config(menu=mimenu)
acciones = Menu(mimenu, tearoff=0)
acciones.add_command(label="Listar registros",command=muestraListar)
acciones.add_command(label="Nuevo registro",command=muestraInsertar)
acciones.add_command(label="Actualizar registro",command=muestraActualizar)
acciones.add_command(label="Eliminar registro",command=muestraEliminar)
acciones.add_command(label="Guardar registros en el disco")
acciones.add_command(label="Leer registros del disco")
mimenu.add_cascade(label="Archivo", menu=acciones)

marcolistar = ttk.LabelFrame(ventana, text="Listado de registros")
tk.Label(marcolistar,text="Hola").pack(padx=20,pady=20)

marcoinsertar = ttk.LabelFrame(ventana, text="Insertar registro")
tk.Label(marcoinsertar,text="Hola").pack(padx=20,pady=20)

marcoactualizar = ttk.LabelFrame(ventana, text="Actualizar registro")
tk.Label(marcoactualizar,text="Hola").pack(padx=20,pady=20)

marcoeliminar = ttk.LabelFrame(ventana, text="Eliminar registro")
tk.Label(marcoeliminar,text="Hola").pack(padx=20,pady=20)

ventana.mainloop()
