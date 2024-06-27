import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

radio1 = tk.IntVar()
tk.Label(ventana,text="Elige un curso")
componente = ttk.Radiobutton(ventana,text="Primer Curso",variable=radio1,value=1)
componente.pack(padx=10,pady=10)

componente2 = ttk.Radiobutton(ventana,text="Segundo Curso",variable=radio1,value=2)
componente2.pack(padx=10,pady=10)

radio2 = tk.IntVar()
tk.Label(ventana,text="Elige un grupo")
componente = ttk.Radiobutton(ventana,text="Grupo de mañanas",variable=radio2,value=1)
componente.pack(padx=10,pady=10)

componente2 = ttk.Radiobutton(ventana,text="Grupo de tardes",variable=radio2,value=2)
componente2.pack(padx=10,pady=10)

ventana.mainloop()

