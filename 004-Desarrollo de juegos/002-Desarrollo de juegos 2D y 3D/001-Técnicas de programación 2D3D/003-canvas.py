import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x600")

lienzo = tk.Canvas(ventana,bg="white")
lienzo.pack()

ventana.mainloop()
