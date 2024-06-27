import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

arbol = ttk.Treeview(ventana, columns=("ID", "nombre", "apellidos","email","telefono"), show='headings')

arbol.heading("ID", text="ID")
arbol.heading("nombre", text="nombre")
arbol.heading("apellidos", text="apellidos")
arbol.heading("email", text="email")
arbol.heading("telefono", text="telefono")

arbol.pack(padx=10,pady=10)

arbol.insert("", "end", values=(1, "Alicia", "Martinez"))
arbol.insert("", "end", values=(2, "Roberto", "Lopez"))
arbol.insert("", "end", values=(3, "Carlos", "Garcia"))

ventana.mainloop()

