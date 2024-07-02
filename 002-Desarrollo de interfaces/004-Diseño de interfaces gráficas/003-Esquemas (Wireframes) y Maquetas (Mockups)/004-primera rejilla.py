import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Aplicación empresarial")
ventana.geometry("800x600")

cabecera = tk.Frame(ventana)
cabecera.grid(row=0,column=0)

cuerpo = tk.Frame(ventana)
cuerpo.grid(row=1,column=0)

ventana.mainloop()
