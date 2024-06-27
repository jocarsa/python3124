import tkinter as tk
import ttkbootstrap as ttk

def pulsaBoton():
    print("Voy a insertar un nombre en el archivo")
    archivo = open("nombres.txt",'a')
    archivo.write(nuevo_nombre.get()+"\n")
    archivo.close()

ventana = tk.Tk()
nuevo_nombre = tk.StringVar()
ttk.Label(ventana,text="Introduce un nombre").pack(padx=20,pady=20)
ttk.Entry(ventana,textvariable=nuevo_nombre).pack(padx=20,pady=20)
ttk.Button(ventana,text="Insertar nuevo nombre",command=pulsaBoton).pack(padx=20,pady=20)

ventana.mainloop()
