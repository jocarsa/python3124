import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Aplicación empresarial")
ventana.geometry("800x600")

cabecera = tk.Frame(ventana, height=50, width=800, bg="#373737")
cabecera.pack_propagate(False) 
cabecera.pack(side="top", fill="x")

nombre = tk.Label(cabecera, text="MiCRM", bg="#373737", fg="#eeeeee", font=("Courier", 32, "bold"))
nombre.pack(side="left", padx=10)

buscador = tk.Entry(cabecera, bd=2, highlightthickness=1, highlightcolor="blue", highlightbackground="black")
buscador.pack(side="left", padx=10, pady=15)

# Create a custom style for the button using a canvas to simulate border radius
def create_rounded_button(parent, text, command=None, bg='#4CAF50', fg='white', bd=0, radius=15):
    canvas = tk.Canvas(parent, borderwidth=0, highlightthickness=0, background=bg)
    canvas.create_oval((0, 0, radius, radius), outline=bg, fill=bg)
    canvas.create_oval((0, radius, radius, 2 * radius), outline=bg, fill=bg)
    canvas.create_oval((radius, 0, 2 * radius, radius), outline=bg, fill=bg)
    canvas.create_oval((radius, radius, 2 * radius, 2 * radius), outline=bg, fill=bg)
    canvas.create_rectangle((radius / 2, 0, 1.5 * radius, 2 * radius), outline=bg, fill=bg)
    canvas.create_rectangle((0, radius / 2, 2 * radius, 1.5 * radius), outline=bg, fill=bg)

    btn = tk.Button(canvas, text=text, command=command, bg=bg, fg=fg, bd=bd, highlightthickness=0, relief='flat')
    btn.place(relx=0.5, rely=0.5, anchor='center')

    return canvas

botonfuncion1 = create_rounded_button(cabecera, text="Salir", bg='#FF5733', fg='white', radius=20)
botonfuncion1.pack(side="right", padx=10, pady=10)

cuerpo = tk.Frame(ventana, height=750, width=800, bg="#eeeeee")
cuerpo.pack_propagate(False)
cuerpo.pack(side="top", fill="both", expand=True)

ventana.mainloop()
