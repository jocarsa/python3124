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
    mover_bala(bala)
    print(balas)

def mover_bala(bala):
    bala.x += bala.velocidad
    lienzo.coords(bala.sprite_id, bala.x, bala.y)
    if bala.x > 800:  # Remove the bullet if it goes off screen
        lienzo.delete(bala.sprite_id)
        balas.remove(bala)
    else:
        ventana.after(50, lambda: mover_bala(bala))
    check_collision()

def check_collision():
    for bala in balas:
        for enemigo in enemigos:
            if (enemigo.x < bala.x < enemigo.x + 50) and (enemigo.y < bala.y < enemigo.y + 50):
                lienzo.delete(bala.sprite_id)
                lienzo.delete(enemigo.sprite_id)
                balas.remove(bala)
                enemigos.remove(enemigo)
                return  # Exit after handling collision to avoid modifying the list while iterating

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

class Nave(Entidad):
    def __init__(self):
        super().__init__()

class Enemigo(Entidad):
    def __init__(self, mix, miy):
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

for i in range(numeroenemigos):
    enemigo = Enemigo(random.randint(0, 750), random.randint(0, 550))
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
    anchor='nw'
)

ventana.bind('<KeyPress-w>', mover)
ventana.bind('<KeyPress-s>', mover)
ventana.bind('<KeyPress-a>', mover)
ventana.bind('<KeyPress-d>', mover)
ventana.bind('<KeyPress-space>', disparar)

ventana.mainloop()
