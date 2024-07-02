import tkinter as tk
from tkinter import ttk

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
tablas.pack(side="left", fill="both")

ventana.mainloop()
