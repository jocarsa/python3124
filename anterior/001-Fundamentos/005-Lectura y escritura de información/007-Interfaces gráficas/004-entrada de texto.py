import tkinter as tk

ventana = tk.Tk()
nuevo_nombre = tk.StringVar()
tk.Label(ventana,text="Introduce un nombre").pack(padx=20,pady=20)
tk.Entry(ventana,textvariable=nuevo_nombre).pack(padx=20,pady=20)


ventana.mainloop()
