import tkinter as tk
from tkinter import ttk
import random

ventana = tk.Tk()
ventana.geometry("800x600")

balas = []
enemigos = []
numeroenemigos = 5

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

def disparar(event):
    print("disparo")
    bala = Bala(jugador.x + 5, jugador.y - 10)  # Adjust the initial position of the bullet
    balas.append(bala)
    sprite_bala = lienzo.create_image(
        bala.getPosicion()['x'],
        bala.getPosicion()['y'],
        image=bala_image,
        anchor='nw'
    )
    bala.sprite_id = sprite_bala
    bala.mover_bala()
    print(balas)

class Entidad:
    def __init__(self, x=50, y=50):
        self.x = x
        self.y = y
    def getPosicion(self):
        return {'x': self.x, 'y': self.y}
    def setPosicion(self, nx, ny):
        self.x = nx
        self.y = ny

class Bala(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocidad = 5
        self.sprite_id = None
    def mover_bala(self):
        self.x += self.velocidad
        lienzo.coords(self.sprite_id, self.x, self.y)
        ventana.after(50, self.mover_bala)

class Nave(Entidad):
    def __init__(self):
        super().__init__()

class Enemigo(Entidad):
    def __init__(self,mix,miy):
        super().__init__()
        self.sprite_id = None
        self.x = mix
        self.y = miy

jugador = Nave()

lienzo = tk.Canvas(ventana, bg="white", width=800, height=600)
lienzo.pack()





sprite_image = tk.PhotoImage(file="navejugador.png")
sprite_image_enemigo = tk.PhotoImage(file="naveenemigo.png")
bala_image = tk.PhotoImage(file="bala.png")


for i in range(0,numeroenemigos):
    enemigo = Enemigo(random.randint(0,800),random.randint(0,600))
    enemigos.append(enemigo)
    sprite_enemigo = lienzo.create_image(
        enemigo.getPosicion()['x'],
        enemigo.getPosicion()['y'],
        image=sprite_image_enemigo,
        anchor='nw'
    )
    enemigo.sprite_id = sprite_enemigo
    

spritejugador = lienzo.create_image(
    jugador.getPosicion()['x'],
    jugador.getPosicion()['y'],
    image=sprite_image,
    anchor='nw')

ventana.bind('<KeyPress-w>', mover)
ventana.bind('<KeyPress-s>', mover)
ventana.bind('<KeyPress-a>', mover)
ventana.bind('<KeyPress-d>', mover)
ventana.bind('<KeyPress-space>', disparar)

ventana.mainloop()
