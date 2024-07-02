import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x600")

class Nave:
    def __init__(self):
        self.x = 50
        self.y = 50
    def getPosicion(self):
        return {'x':self.x,'y':self.y}
    def setPosicion(self,nx,ny):
        self.x = nx
        self.y = ny

jugador = Nave()

lienzo = tk.Canvas(ventana,bg="white",width=800,height=600)
lienzo.pack()

print(jugador.getPosicion())
lienzo.create_rectangle(
    jugador.getPosicion()['x'],
    jugador.getPosicion()['y'],
    jugador.getPosicion()['x']+10,
    jugador.getPosicion()['y']+10,
    fill="red",
    outline="green")

ventana.mainloop()
