import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

var1 = tk.IntVar()

componente = ttk.Checkbutton(ventana,text="Primer Curso")
componente.pack(padx=10,pady=10)

componente = ttk.Checkbutton(ventana,text="Segundo Curso")
componente.pack(padx=10,pady=10)

ventana.mainloop()

