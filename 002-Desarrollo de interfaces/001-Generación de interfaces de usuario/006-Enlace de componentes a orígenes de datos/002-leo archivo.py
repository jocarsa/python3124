import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

arbol = ttk.Treeview(ventana, columns=("ID", "nombre", "apellidos","email","telefono"), show='headings')

arbol.heading("ID", text="ID")
arbol.heading("nombre", text="nombre")
arbol.heading("apellidos", text="apellidos")
arbol.heading("email", text="email")
arbol.heading("telefono", text="telefono")

arbol.pack(padx=10,pady=10)

archivo = open("clientes.csv",'r')
lineas = archivo.readlines()

for linea in lineas:
    nombre = linea.split(",")[0]
    apellidos = linea.split(",")[1]
    email = linea.split(",")[2]
    telefono = linea.split(",")[3]
    arbol.insert("", "end", values=(1, nombre, apellidos,email,telefono))


ventana.mainloop()

