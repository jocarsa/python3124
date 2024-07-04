import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()
ventana.title("Buscador en discos")
ventana.geometry("800x600")

marco1 = tk.Frame(ventana)
marco1.pack(side="top")

ttk.Label(marco1,text="Introduce lo que quieres buscar").pack(side="left",padx=10,pady=10)
ttk.Entry(marco1).pack(side="left",padx=10,pady=10)
ttk.Button(marco1,text="Comienza la búsqueda").pack(side="left",padx=10,pady=10)

marco2 = tk.Frame(ventana)
marco2.pack(side="top")

ventana.mainloop()

