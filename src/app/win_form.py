import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def open_win_form(parent: tk.Tk):
    #Ventana 
    win = tk.Toplevel(parent)
    win.title("Registro información médica")
    win.geometry("1300x700")

    #Frame de la ventana
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    lblTitulo = ttk.Label(frm, text="Registro de información médica", font=("Verdana", 24, "bold"))
    lblTitulo.place(x=50, y=20)

    lblNombre =ttk.Label(frm, text="Nombre:", font=("Verdana", 18, "bold"))
    lblNombre.place(x=50, y=100)
    entNombre = ttk.Entry(frm, width=10, font=("Verdana", 18))
    entNombre.place(x=50, y=140)

    lblEdad = ttk.Label(frm, text="Edad:", font=("Verdana", 18, "bold"))
    lblEdad.place(x=300, y=100)
    entEdad = ttk.Entry(frm, width=10, font=("Verdana", 18))
    entEdad.place(x=300, y=140)

    lblFecha = ttk.Label(frm, text="Fecha de registro:", font=("Verdana", 18, "bold"))
    lblFecha.place(x=550, y=100)
    entFecha = ttk.Entry(frm, width=10, font=("Verdana", 18))
    entFecha.place(x=550, y=140)

    lblMedicamentos = ttk.Label(frm, text="Medicamentos", font=("Verdana", 18, "bold"))
    lblMedicamentos.place(x=50, y=250)

    cmbMedicamento = ttk.Combobox(frm, values=["15", "16", "17", "18", "19", "20"], font=("Arial", 14), state="readonly")
    cmbMedicamento.place(x=50, y=290, width=150, height=30)

    def validar_y_guardar():
        nombre = entNombre.get().strip()
        edad_txt = entEdad.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre es requerido.")
            return
        if not edad_txt.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return
        ruta = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Texto", "*.txt")])
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(f"Nombre: {nombre}\nEdad: {edad_txt}\n")
            messagebox.showinfo("OK", "Datos guardados.")

    btnGuardar = ttk.Button(frm, text="Guardar", command=validar_y_guardar)
    btnGuardar.place(x=1050, y=600)
    btnCerrar = ttk.Button(frm, text="Cerrar", command=win.destroy)
    btnCerrar.place(x=1150, y=600)