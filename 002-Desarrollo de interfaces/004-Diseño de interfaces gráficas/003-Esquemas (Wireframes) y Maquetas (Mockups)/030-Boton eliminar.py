import tkinter as tk
from tkinter import ttk
import mysql.connector

servidor = "localhost"
usuario = "josevicente"
contrasena = "josevicente"
base_de_datos = "empresa"

arbol = None
marcoinsertar = None
entries = []  # List to hold entry widgets

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)

cursor = conexion.cursor()

def guardar(tabla):
    global entries
    print("Guardando el registro en la tabla:", tabla)
    valores = [entry.get() for entry in entries]
    placeholders = ", ".join(["%s"] * len(valores))
    columnas = ", ".join([entry.column_name for entry in entries])
    sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"
    cursor.execute(sql, valores)
    conexion.commit()
    cargaTabla(tabla)  # Refresh the table view after inserting
    print("Registro guardado correctamente.")

def eliminar(tabla, item_id):
    print("Eliminando registro con ID:", item_id, "de la tabla", tabla)
    cursor.execute(f"DELETE FROM {tabla} WHERE Identificador = %s", (item_id,))
    conexion.commit()
    cargaTabla(tabla)  # Refresh the table view after deleting
    print("Registro eliminado correctamente.")

def on_tree_select(event):
    global arbol
    selected_item = arbol.selection()[0]
    item_id = arbol.item(selected_item)['values'][0]
    print("Registro seleccionado con ID:", item_id)
    eliminar(tabla_actual, item_id)

def nuevo(tabla):
    global arbol, marcoinsertar, entries
    print("Voy a crear un nuevo elemento en la tabla:", tabla)
    entries = []  # Reset the entries list
    if arbol:
        arbol.grid_remove()
    for widget in contenido.winfo_children():
        widget.destroy()
    marcoinsertar = tk.Frame(contenido, bg="white")
    marcoinsertar.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    tk.Label(marcoinsertar, text="Formulario de inserción", bg="white", font=("Courier", 20)).pack(padx=10, pady=10)
    cursor.execute(f"DESCRIBE {tabla};")
    filas = cursor.fetchall()
    for fila in filas:
        tk.Label(marcoinsertar, text=fila[0], bg="white").pack(padx=10, pady=5)
        entry = tk.Entry(marcoinsertar)
        entry.pack(padx=10, pady=5)
        entry.column_name = fila[0]  # Attach the column name to the entry widget
        entries.append(entry)
    
    tk.Button(marcoinsertar, text="Guardar", command=lambda: guardar(tabla)).pack(padx=10, pady=10)
    contenido.grid_rowconfigure(1, weight=1)
    contenido.grid_columnconfigure(0, weight=1)

def cargaTabla(tabla):
    global arbol, marcoinsertar, tabla_actual
    tabla_actual = tabla
    print("Vamos a operar con la tabla:", tabla)
    for widget in contenido.winfo_children():
        widget.destroy()
    nombretabla = tk.Label(contenido, text=tabla, bg="white", fg="#aaaaaa", font=("Courier", 32, "bold"))
    nombretabla.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    tk.Button(contenido, text="Crear nuevo registro", command=lambda: nuevo(tabla)).grid(row=0, column=1, padx=10, pady=10, sticky="w")
    tk.Button(contenido, text="Eliminar registro seleccionado", command=lambda: eliminar(tabla, None)).grid(row=0, column=2, padx=10, pady=10, sticky="w")
    
    cursor.execute(f"DESCRIBE {tabla};")
    filas = cursor.fetchall()
    listacolumnas = []
    for fila in filas:
        listacolumnas.append(fila[0])
    arbol = ttk.Treeview(contenido, columns=tuple(listacolumnas), show='headings')
    arbol.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
    for columna in listacolumnas:
        arbol.heading(columna, text=columna)
    cursor.execute(f"SELECT * FROM {tabla};")
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=fila)
    
    # Bind the treeview selection event to the on_tree_select function
    arbol.bind('<<TreeviewSelect>>', on_tree_select)
    
    # Make the treeview expandable
    contenido.grid_rowconfigure(1, weight=1)
    contenido.grid_columnconfigure(0, weight=1)
    contenido.grid_columnconfigure(1, weight=1)

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
    botontemporal = tk.Button(tablas, text=fila[0], bg="#222222", fg="white", bd=0, padx=10, pady=10, width=10, command=lambda f=fila[0]: cargaTabla(f))
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
