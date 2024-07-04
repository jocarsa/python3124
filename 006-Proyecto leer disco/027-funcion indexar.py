import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
import sqlite3
import os

conexion = sqlite3.connect('discos.db')
cursor = conexion.cursor()

ventana = tk.Tk()
ventana.title("Buscador en discos")
ventana.geometry("800x600")

campo = tk.StringVar()
disco = tk.StringVar()

def indexa():
    print("voy a indexar")
    folder_selected = filedialog.askdirectory()
    # Leemos datos de partida
    contenido = os.walk(disco)
    for root, dirs, files in os.walk(folder_selected):
        #print(f"Root: {root}")
        #print("Directories:")
        for dir_name in dirs:
            #print(f"  {dir_name}")
            pass
        #print("Files:")
        for file_name in files:
            file_size = 0
            try:
                file_size = os.path.getsize(root+"/"+file_name)
            except:
                pass
            try:
                modification_time = os.path.getmtime(root+"/"+file_name)
            except:
                pass
            #print(f"  {file_name} - {file_size} - {modification_time}")
            try:
                cursor.execute(f"""
                INSERT INTO
                archivos
                VALUES (
                NULL,
                '{disco.get()}',
                '{root}',
                '{file_name}',
                '{modification_time}',
                '{file_size}')
                """)
                
                print("#", end=" ")
                conexion.commit()
            except:
                pass
        
        #print("\n")

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
ttk.Button(marco1, text="Comienza la indexación", command=indexa).pack(side="left", padx=10, pady=10)

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
