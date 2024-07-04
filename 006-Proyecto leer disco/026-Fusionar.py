import tkinter as tk
import ttkbootstrap as ttk
import sqlite3

conexion = sqlite3.connect('discos.db')
cursor = conexion.cursor()

ventana = tk.Tk()
ventana.title("Buscador en discos")
ventana.geometry("800x600")

campo = tk.StringVar()
disco = tk.StringVar()
def busqueda():
    for elemento in arbol.get_children():
        arbol.delete(elemento)
    
    search_term = campo.get()
    cursor.execute("SELECT Identificador, disco, carpeta, archivo, datetime(fecha, 'unixepoch') AS fecha_human_readable, (tamaño / (1024)) || ' KB' AS tamaño_MB FROM archivos WHERE archivo LIKE ?", ('%' + search_term + '%',))
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=fila)

def ordenar_por_columna(tree, col, reverse):
    # Obtener datos de la Treeview
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # Ordenar datos
    data.sort(reverse=reverse)

    # Reordenar los items en el árbol
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)

    # Alternar el estado de ordenación
    tree.heading(col, command=lambda: ordenar_por_columna(tree, col, not reverse))

marco1 = tk.Frame(ventana)
marco1.pack(side="top")

ttk.Label(marco1, text="Introduce lo que quieres buscar").pack(side="left", padx=10, pady=10)
ttk.Entry(marco1, textvariable=campo).pack(side="left", padx=10, pady=10)
ttk.Button(marco1, text="Comienza la búsqueda", command=busqueda).pack(side="left", padx=10, pady=10)
ttk.Label(marco1, text="o bien, pon título al disco: ").pack(side="left", padx=10, pady=10)
ttk.Entry(marco1, textvariable=disco).pack(side="left", padx=10, pady=10)
ttk.Button(marco1, text="Comienza la indexación", command=busqueda).pack(side="left", padx=10, pady=10)

marco2 = tk.Frame(ventana)
marco2.pack(side="top", fill=tk.BOTH, expand=True)

arbol = ttk.Treeview(marco2, columns=("ID", "disco", "carpeta", "archivo", "fecha", "tamaño"), show='headings')

arbol.heading("ID", text="ID", command=lambda: ordenar_por_columna(arbol, "ID", False))
arbol.heading("disco", text="disco", command=lambda: ordenar_por_columna(arbol, "disco", False))
arbol.heading("carpeta", text="carpeta", command=lambda: ordenar_por_columna(arbol, "carpeta", False))
arbol.heading("archivo", text="archivo", command=lambda: ordenar_por_columna(arbol, "archivo", False))
arbol.heading("fecha", text="fecha", command=lambda: ordenar_por_columna(arbol, "fecha", False))
arbol.heading("tamaño", text="tamaño", command=lambda: ordenar_por_columna(arbol, "tamaño", False))

scrollbar = ttk.Scrollbar(marco2, orient=tk.VERTICAL, command=arbol.yview)
arbol.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
arbol.pack(side="left", fill="both", expand=True, padx=10, pady=10)

ventana.mainloop()
