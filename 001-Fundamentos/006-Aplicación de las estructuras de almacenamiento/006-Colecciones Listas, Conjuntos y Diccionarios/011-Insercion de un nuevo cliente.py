import tkinter as tk
from tkinter import Menu
import ttkbootstrap as ttk

class Cliente:
    def __init__(self,miid,minombre,misapellidos,miemail,mitelefono):
        self.identificador = miid
        self.nombre = minombre
        self.apellidos = misapellidos
        self.email = miemail
        self.telefono = mitelefono
    def setNombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    def getNombre(self):
        return self.nombre
    def setApellidos(self,nuevos_apellidos):
        self.nombre = nuevos_apellidos
    def getApellidos(self):
        return self.nombre
    def setEmail(self,nuevo_email):
        self.nombre = nuevo_email
    def getEmail(self):
        return self.nombre
    def setTelefono(self,nuevo_telefono):
        self.nombre = nuevo_telefono
    def getTelefono(self):
        return self.nombre

clientes = []

def insertaCliente():
    global clientes
    clientes.append(Cliente(miid,minombre,misapellidos,miemail,mitelefono))
    print(clientes)
        
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

miid = tk.StringVar()
minombre = tk.StringVar()
misapellidos = tk.StringVar()
miemail = tk.StringVar()
mitelefono = tk.StringVar()

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
tk.Label(marcoinsertar,text="Insertar un nuevo cliente").pack(padx=20,pady=20)
tk.Label(marcoinsertar,text="Indica su ID").pack(padx=5,pady=5)
tk.Entry(marcoinsertar,textvariable=miid).pack(padx=5,pady=5)
tk.Label(marcoinsertar,text="Indica su nombre").pack(padx=5,pady=5)
tk.Entry(marcoinsertar,textvariable=minombre).pack(padx=5,pady=5)
tk.Label(marcoinsertar,text="Indica sus apellidos").pack(padx=5,pady=5)
tk.Entry(marcoinsertar,textvariable=misapellidos).pack(padx=5,pady=5)
tk.Label(marcoinsertar,text="Indica su email").pack(padx=5,pady=5)
tk.Entry(marcoinsertar,textvariable=miemail).pack(padx=5,pady=5)
tk.Label(marcoinsertar,text="Indica su telefono").pack(padx=5,pady=5)
tk.Entry(marcoinsertar,textvariable=mitelefono).pack(padx=5,pady=5)
ttk.Button(marcoinsertar,text="Inserta nuevo cliente",command=insertaCliente).pack(padx=5,pady=5)

marcoactualizar = ttk.LabelFrame(ventana, text="Actualizar registro")
tk.Label(marcoactualizar,text="Hola").pack(padx=20,pady=20)

marcoeliminar = ttk.LabelFrame(ventana, text="Eliminar registro")
tk.Label(marcoeliminar,text="Hola").pack(padx=20,pady=20)

ventana.mainloop()
