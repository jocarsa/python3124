import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x600")

def mover(event):
    if event.keysym == 'w':
        jugador.setPosicion(jugador.x, jugador.y - 10)
    elif event.keysym == 's':
        jugador.setPosicion(jugador.x, jugador.y + 10)
    elif event.keysym == 'a':
        jugador.setPosicion(jugador.x - 10, jugador.y)
    elif event.keysym == 'd':
        jugador.setPosicion(jugador.x + 10, jugador.y)
    
    posicion = jugador.getPosicion()
    lienzo.coords(spritejugador, posicion['x'], posicion['y'])
    
    

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


sprite_image = tk.PhotoImage(file="navejugador.png")  
spritejugador = lienzo.create_image(
    jugador.getPosicion()['x'],
    jugador.getPosicion()['y'],
    image=sprite_image,
    anchor='nw')

ventana.bind('<KeyPress-w>', mover)
ventana.bind('<KeyPress-s>', mover)
ventana.bind('<KeyPress-a>', mover)
ventana.bind('<KeyPress-d>', mover)

ventana.mainloop()
