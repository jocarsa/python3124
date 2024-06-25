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

nuevo_nombre = tk.StringVar()
marco = tk.Frame(padx=20,pady=20)
ttk.Label(marco,text="Introduce un nombre").pack(padx=20,pady=20)
ttk.Entry(marco,textvariable=nuevo_nombre).pack(padx=20,pady=20)
ttk.Button(marco,text="Insertar nuevo nombre",command=pulsaBoton).pack(padx=20,pady=20)
marco.grid(column=0,row=0)
marco2 = tk.Frame(padx=20,pady=20)
ttk.Button(marco2,text="Obtener registros",command=obtieneRegistros).pack(padx=20,pady=20)
caja_texto = ttk.Text(marco2)
caja_texto.pack(padx=20,pady=20)
marco2.grid(column=1,row=0)
ventana.mainloop()
