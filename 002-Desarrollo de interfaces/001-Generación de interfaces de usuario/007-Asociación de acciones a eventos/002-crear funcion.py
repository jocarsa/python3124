import tkinter as tk
import ttkbootstrap as ttk

def hazAlgo():
    print("Has pulsado el boton")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame",command=hazAlgo).pack(padx=10,pady=10)

ventana.mainloop()

