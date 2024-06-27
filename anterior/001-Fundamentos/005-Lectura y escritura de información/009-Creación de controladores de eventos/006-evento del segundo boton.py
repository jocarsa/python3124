import tkinter as tk
import ttkbootstrap as ttk

def pulsaBoton():
    print("Voy a insertar un nombre en el archivo")
    archivo = open("nombres.txt",'a')
    archivo.write(nuevo_nombre.get()+"\n")
    archivo.close()
def obtieneRegistros():
    print("Obtengo los registros")
    archivo = open("nombres.txt",'r')

ventana = tk.Tk()
nuevo_nombre = tk.StringVar()
marco = tk.Frame(padx=20,pady=20)
ttk.Label(marco,text="Introduce un nombre").pack(padx=20,pady=20)
ttk.Entry(marco,textvariable=nuevo_nombre).pack(padx=20,pady=20)
ttk.Button(marco,text="Insertar nuevo nombre",command=pulsaBoton).pack(padx=20,pady=20)
marco.grid(column=0,row=0)
marco2 = tk.Frame(padx=20,pady=20)
ttk.Button(marco2,text="Obtener registros",command=obtieneRegistros).pack(padx=20,pady=20)
caja_texto = ttk.Text(marco2)
caja_texto.pack(padx=20,pady=20)
marco2.grid(column=1,row=0)
ventana.mainloop()
