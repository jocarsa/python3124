import tkinter as tk
import ttkbootstrap as ttk

def click(event):
    print("Has pulsado el boton izquierdo")

def click2(event):
    print("Has pulsado el boton del medio")

def click3(event):
    print("Has pulsado el boton derecho")

def click4(event):
    print("Has pulsado doble click")

def entra(event):
    print("Has entrado")

def sale(event):
    print("Has salido")

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame")
boton.pack(padx=10,pady=10)

boton.bind("<Button-1>", click)
boton.bind("<Button-2>", click2)
boton.bind("<Button-3>", click3)
boton.bind("<Double-1>", click4)
boton.bind("<Enter>", entra)
boton.bind("<Leave>", sale)



ventana.mainloop()

