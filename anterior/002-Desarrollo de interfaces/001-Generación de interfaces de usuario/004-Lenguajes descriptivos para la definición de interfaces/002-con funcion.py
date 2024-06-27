import tkinter as tk

ventana = tk.Tk()

def pulsaBoton():
    print("Has pulsado el boton")

tk.Label(ventana,text="Introduce tu nombre").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)
tk.Label(ventana,text="Introduce tu apellido").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)
tk.Label(ventana,text="Introduce tu email").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)
tk.Label(ventana,text="Introduce tu telefono").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)
tk.Button(ventana,text="Ejecuta",command=pulsaBoton).pack(padx=10,pady=10)

ventana.mainloop()
