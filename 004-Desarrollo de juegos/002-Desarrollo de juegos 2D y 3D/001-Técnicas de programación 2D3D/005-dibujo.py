import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("800x600")

lienzo = tk.Canvas(ventana,bg="white",width=800,height=600)
lienzo.pack()

lienzo.create_rectangle(10,10,20,20,fill="red",outline="green")

ventana.mainloop()
