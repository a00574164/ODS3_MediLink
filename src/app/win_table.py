import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import date, timedelta

def open_win_table(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Tabla (Treeview)")
    win.geometry("800x500")
    boton_cerrar = ttk.Button(win, text="Cerrar", command=win.destroy)
    boton_cerrar.pack(side="bottom", pady=10)

    columnas = ("Fecha", "Medicamento", "Dosis", "Estado")
    tv = ttk.Treeview(win, columns=columnas, show="headings")
    for col in columnas:
      tv.heading(col, text=col)
      tv.column(col, width=150, anchor="center")

    # Generate sample data for demonstration
    medicamentos = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Metformina"]
    dosis_opciones = ["500mg", "1 g", "250mg", "2 g", "5 mg"]
    estados = ["Tomado", "Pendiente", "No tomado"]
    for _ in range(10):
        dias_atras = random.randint(0, 7)
        Fecha_aleatoria = (date.today() - timedelta(days=dias_atras)).strftime("%Y-%m-%d")

        med = random.choice(medicamentos)
        dosis = random.choice(dosis_opciones)
        estado = random.choice(estados)

        tv.insert("", "end", values=(Fecha_aleatoria, med, dosis, estado))
    tv.pack(expand=True, fill="both", padx=20, pady=10)
    btn_cerrar = ttk.Button(win, text="Cerrar", command=win.destroy)