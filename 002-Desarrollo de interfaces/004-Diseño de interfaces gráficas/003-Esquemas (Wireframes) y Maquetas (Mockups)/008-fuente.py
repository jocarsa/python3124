import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Aplicación empresarial")
ventana.geometry("800x600")

cabecera = tk.Frame(ventana, height=50, width=800, bg="#373737")
cabecera.pack_propagate(False) 
cabecera.pack(side="top", fill="x")

nombre = tk.Label(cabecera,text="MiCRM", bg="#373737",fg="#eeeeee", font=("Courier", 32))
nombre.pack(side="left")

cuerpo = tk.Frame(ventana, height=750, width=800, bg="#eeeeee")
cuerpo.pack_propagate(False)
cuerpo.pack(side="top", fill="both", expand=True)

ventana.mainloop()
