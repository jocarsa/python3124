import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()
nuevo_nombre = tk.StringVar()
ttk.Label(ventana,text="Introduce un nombre").pack(padx=20,pady=20)
ttk.Entry(ventana,textvariable=nuevo_nombre).pack(padx=20,pady=20)
ttk.Button(ventana,text="Insertar nuevo nombre").pack(padx=20,pady=20)

ventana.mainloop()
