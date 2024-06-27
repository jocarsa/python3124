import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

marco = tk.Frame(ventana)

tk.Label(marco,text="Texto 1").pack(padx=10,pady=10)
tk.Label(marco,text="Texto 2").pack(padx=10,pady=10)

marco.pack(padx=10,pady=10)

ventana.mainloop()

