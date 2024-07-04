import tkinter as tk
import ttkbootstrap as ttk
import sqlite3

conexion = sqlite3.connect('discos.db')
cursor = conexion.cursor()

ventana = tk.Tk()
ventana.title("Buscador en discos")
ventana.geometry("800x600")

campo = tk.StringVar()

def busqueda():
    global campo
    cursor.execute(f"SELECT * FROM archivos WHERE archivo LIKE '%"+campo.get()+"%'")
    filas = cursor.fetchall()
    for fila in filas:
        valores = []
        for campo in fila:
            valores.append(campo)
        arbol.insert("", "end", values=tuple(valores))
marco1 = tk.Frame(ventana)
marco1.pack(side="top")

ttk.Label(marco1,text="Introduce lo que quieres buscar").pack(side="left",padx=10,pady=10)
ttk.Entry(marco1,textvariable=campo).pack(side="left",padx=10,pady=10)
ttk.Button(marco1,text="Comienza la búsqueda",command=busqueda).pack(side="left",padx=10,pady=10)

marco2 = tk.Frame(ventana)
marco2.pack(side="top")

arbol = ttk.Treeview(marco2, columns=("ID", "disco", "carpeta","archivo","fecha","tamaño"), show='headings')

arbol.heading("ID", text="ID")
arbol.heading("disco", text="disco")
arbol.heading("carpeta", text="carpeta")
arbol.heading("archivo", text="archivo")
arbol.heading("fecha", text="fecha")
arbol.heading("tamaño", text="tamaño")

arbol.pack(padx=10,pady=10)




ventana.mainloop()

