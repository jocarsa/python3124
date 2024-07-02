import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x600")

posxjugador = 50
posyjugador = 50

lienzo = tk.Canvas(ventana,bg="white",width=800,height=600)
lienzo.pack()

lienzo.create_rectangle(
    posxjugador,
    posyjugador,
    posxjugador+10,
    posyjugador+10,
    fill="red",
    outline="green")

ventana.mainloop()
