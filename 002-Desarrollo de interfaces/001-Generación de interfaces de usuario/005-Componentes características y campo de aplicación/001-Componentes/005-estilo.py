import tkinter as tk
import ttkbootstrap as ttk

ventana = tk.Tk()

componente = ttk.Combobox(ventana,values=['manzana','pera','platano','fresa'])
componente.pack(padx=10,pady=10)

ventana.mainloop()

