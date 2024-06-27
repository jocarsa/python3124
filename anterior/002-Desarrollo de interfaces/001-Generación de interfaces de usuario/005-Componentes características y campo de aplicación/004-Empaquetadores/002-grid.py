import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

tk.Label(ventana,text="Texto 1").grid(padx=10,pady=10,row=0,column=0)
tk.Label(ventana,text="Texto 2").grid(padx=10,pady=10,row=0,column=1)

ventana.mainloop()

