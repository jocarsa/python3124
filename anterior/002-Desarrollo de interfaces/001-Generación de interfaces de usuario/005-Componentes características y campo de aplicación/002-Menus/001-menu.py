import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

barramenu = tk.Menu(ventana)


archivo = tk.Menu(barramenu, tearoff=0)
archivo.add_command(label="New")
archivo.add_command(label="Open")
archivo.add_command(label="Save")
archivo.add_separator()
archivo.add_command(label="Exit")
barramenu.add_cascade(label="File", menu=archivo)


editar = tk.Menu(barramenu, tearoff=0)
editar.add_command(label="Undo")
editar.add_command(label="Redo")
editar.add_separator()
editar.add_command(label="Cut")
editar.add_command(label="Copy")
editar.add_command(label="Paste")
barramenu.add_cascade(label="Edit", menu=editar)

ventana.config(menu=barramenu)

ventana.mainloop()

