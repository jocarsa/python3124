import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()
ventana.title("Buscador en discos")
ventana.geometry("800x600")

marco1 = tk.Frame(ventana)
marco1.pack(side="top")

ttk.Label(marco1,text="Introduce lo que quieres buscar").pack(side="left",padx=10,pady=10)
ttk.Entry(marco1).pack(side="left",padx=10,pady=10)
ttk.Button(marco1,text="Comienza la búsqueda").pack(side="left",padx=10,pady=10)

marco2 = tk.Frame(ventana)
marco2.pack(side="top")

arbol = ttk.Treeview(marco2, columns=("ID", "disco", "carpeta","archivo","fecha","tamaño"), show='headings')

arbol.heading("ID", text="ID")
arbol.heading("disco", text="disco")
arbol.heading("carpeta", text="carpeta")
arbol.heading("archivo", text="archivo")
arbol.heading("fecha", text="fecha")
arbol.heading("tamaño", text="tamaño")

arbol.pack(padx=10,pady=10)

arbol.insert("", "end", values=(1, "Alicia", "Martinez"))


ventana.mainloop()

