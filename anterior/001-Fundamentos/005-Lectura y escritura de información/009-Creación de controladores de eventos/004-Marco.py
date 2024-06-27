import tkinter as tk
import ttkbootstrap as ttk

def pulsaBoton():
    print("Voy a insertar un nombre en el archivo")
    archivo = open("nombres.txt",'a')
    archivo.write(nuevo_nombre.get()+"\n")
    archivo.close()

ventana = tk.Tk()
nuevo_nombre = tk.StringVar()
marco = tk.Frame(padx=20,pady=20)
ttk.Label(marco,text="Introduce un nombre").pack(padx=20,pady=20)
ttk.Entry(marco,textvariable=nuevo_nombre).pack(padx=20,pady=20)
ttk.Button(marco,text="Insertar nuevo nombre",command=pulsaBoton).pack(padx=20,pady=20)
marco.grid(column=0,row=0)
ventana.mainloop()
