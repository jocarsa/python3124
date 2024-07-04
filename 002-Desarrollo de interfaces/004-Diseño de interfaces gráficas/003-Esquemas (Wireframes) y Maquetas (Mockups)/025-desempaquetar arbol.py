import tkinter as tk
from tkinter import ttk
import mysql.connector

servidor = "localhost"
usuario = "josevicente"
contrasena = "josevicente"
base_de_datos = "empresa"

arbol = None

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)

cursor = conexion.cursor()

def nuevo(tabla):
    global arbol
    print("Voy a crear un nuevo elemento en la tabla:",tabla)
    if arbol:
        arbol.grid_remove()

def cargaTabla(tabla):
    global arbol
    print("Vamos a operar con la tabla:", tabla)
    for widget in contenido.winfo_children():
        widget.destroy()
    nombretabla = tk.Label(contenido, text=tabla, bg="white", fg="#aaaaaa", font=("Courier", 32, "bold"))
    nombretabla.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    tk.Button(contenido,text="Crear nuevo registro",command=lambda:nuevo(tabla)).grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    cursor.execute(f"DESCRIBE {tabla};")
    filas = cursor.fetchall()
    listacolumnas = []
    for fila in filas:
        listacolumnas.append(fila[0])
    arbol = ttk.Treeview(contenido, columns=tuple(listacolumnas), show='headings')
    arbol.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    for columna in listacolumnas:
        arbol.heading(columna, text=columna)
    cursor.execute(f"SELECT * FROM {tabla};")
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=fila)
    
    # Make the treeview expandable
    contenido.grid_rowconfigure(1, weight=1)
    contenido.grid_columnconfigure(0, weight=1)

ventana = tk.Tk()
ventana.title("Aplicación empresarial")
ventana.geometry("800x600")

cabecera = tk.Frame(ventana, height=50, bg="#373737")
cabecera.grid(row=0, column=0, columnspan=2, sticky="ew")

nombre = tk.Label(cabecera, text="MiCRM", bg="#373737", fg="#eeeeee", font=("Courier", 32, "bold"))
nombre.pack(side="left", padx=10)

buscador = tk.Entry(cabecera, bd=2, highlightthickness=1, highlightcolor="blue", highlightbackground="black")
buscador.pack(side="left", padx=10, pady=15)

botonfuncion1 = ttk.Button(cabecera, text="Salir")
botonfuncion1.pack(side="right", padx=10)

cuerpo = tk.Frame(ventana, bg="#eeeeee")
cuerpo.grid(row=1, column=0, columnspan=2, sticky="nsew")

tablas = tk.Frame(cuerpo, bg="#111111")
tablas.grid(row=0, column=0, sticky="nsew")

cursor.execute("SHOW TABLES;")
filas = cursor.fetchall()

botones = []

for fila in filas:
    botontemporal = tk.Button(tablas, text=fila, bg="#222222", fg="white", bd=0, padx=10, pady=10, width=10, command=lambda f=fila[0]: cargaTabla(f))
    botones.append(botontemporal)
    botontemporal.pack(side="top", padx=10, pady=10)

conexion.commit()

contenido = tk.Frame(cuerpo, bg="white")
contenido.grid(row=0, column=1, sticky="nsew")

# Configure resizing behavior
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
cuerpo.grid_rowconfigure(0, weight=1)
cuerpo.grid_columnconfigure(1, weight=1)

ventana.mainloop()
