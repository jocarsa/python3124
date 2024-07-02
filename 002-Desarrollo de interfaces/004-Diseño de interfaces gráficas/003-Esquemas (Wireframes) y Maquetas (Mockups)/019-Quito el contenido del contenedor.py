import tkinter as tk
from tkinter import ttk
import mysql.connector

servidor = "localhost"
usuario = "josevicente"
contrasena = "josevicente"
base_de_datos = "empresa"

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)

cursor = conexion.cursor()

def cargaTabla(tabla):
    print("Vamos a operar con la tabla:",tabla)
    for widget in contenido.winfo_children():
        widget.destroy()
    nombretabla = tk.Label(contenido,text=tabla, bg="white",fg="#aaaaaa", font=("Courier", 32, "bold"))
    nombretabla.pack(side="top",padx=10)

ventana = tk.Tk()
ventana.title("Aplicación empresarial")
ventana.geometry("800x600")

cabecera = tk.Frame(ventana, height=50, width=800, bg="#373737")
cabecera.pack_propagate(False) 
cabecera.pack(side="top", fill="x")

nombre = tk.Label(cabecera,text="MiCRM", bg="#373737",fg="#eeeeee", font=("Courier", 32, "bold"))
nombre.pack(side="left",padx=10)

buscador = tk.Entry(cabecera,bd=2, highlightthickness=1, highlightcolor="blue", highlightbackground="black")
buscador.pack(side="left",padx=10,pady=15)

botonfuncion1 = ttk.Button(cabecera,text="Salir")
botonfuncion1.pack(side="right",padx=10)

cuerpo = tk.Frame(ventana, height=750, width=800, bg="#eeeeee")
cuerpo.pack_propagate(False)
cuerpo.pack(side="top", fill="both", expand=True)

tablas = tk.Frame(cuerpo,height=750, width=200, bg="#111111")
cabecera.pack_propagate(False) 
tablas.pack(side="left", fill="both")

cursor.execute("SHOW TABLES;")
filas = cursor.fetchall()

botones = []

for fila in filas:
    botontemporal = tk.Button(tablas,text=fila,bg="#222222",fg="white",bd=0,padx=10,pady=10,width=10,command=lambda f=fila[0]: cargaTabla(f))
    botones.append(botontemporal)
    botontemporal.pack(side="top",padx=10,pady=10)

conexion.commit()

contenido = tk.Frame(cuerpo,height=750, width=700, bg="white")
contenido.pack_propagate(False) 
contenido.pack(side="right", fill="both")

ventana.mainloop()
