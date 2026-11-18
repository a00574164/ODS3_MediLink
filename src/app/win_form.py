import tkinter as tk
from tkinter import ttk, filedialog, messagebox

AZUL = "#2F6FE0"
FONDO = "#E8F0FD"
LATERAL = "#D3E2FA"
BLANCO = "#FFFFFF"


def open_win_form(parent: tk.Tk):
    # Ventana
    win = tk.Toplevel(parent)
    win.title("MediLink - Registrar información médica")
    win.geometry("1100x650")
    win.configure(bg=FONDO)

    # Estilos
    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("TFrame", background=FONDO)
    style.configure("Lateral.TFrame", background=LATERAL)
    style.configure("Card.TLabelframe", background=BLANCO)
    style.configure("Card.TLabelframe.Label", background=BLANCO,
                    font=("Verdana", 14, "bold"))
    style.configure("TLabel", background=BLANCO, font=("Verdana", 11))
    style.configure("Titulo.TLabel", background=FONDO, font=("Verdana", 22, "bold"))
    style.configure("Sub.TLabel", background=FONDO, font=("Verdana", 11))
    style.configure("Menu.TButton", font=("Verdana", 11), anchor="w", padding=10)
    style.configure("Guardar.TButton", font=("Verdana", 11, "bold"),
                    background=AZUL, foreground="white", padding=10)
    style.map("Guardar.TButton", background=[("active", "#1F55B8")])
    style.configure("Limpiar.TButton", font=("Verdana", 11), padding=10)

    # Barra lateral
    lateral = ttk.Frame(win, style="Lateral.TFrame", width=220)
    lateral.pack(side="left", fill="y")
    lateral.pack_propagate(False)

    tk.Label(lateral, text="MediLink", bg=LATERAL, fg=AZUL,
             font=("Verdana", 20, "bold")).pack(pady=(30, 0))
    tk.Label(lateral, text="Tu salud, conectada", bg=LATERAL,
             font=("Verdana", 9)).pack(pady=(0, 25))

    for texto in ["Inicio", "Registrar información", "Mis medicamentos",
                  "Historial médico", "Mi progreso", "Configuración"]:
        ttk.Button(lateral, text=texto, style="Menu.TButton").pack(
            fill="x", padx=12, pady=3)

    # Contenido
    frm = ttk.Frame(win, padding=20)
    frm.pack(side="left", fill="both", expand=True)

    ttk.Label(frm, text="Registrar información médica",
              style="Titulo.TLabel").pack(anchor="w")
    ttk.Label(frm, text="Mantén un registro de tu tratamiento y cómo te sientes",
              style="Sub.TLabel").pack(anchor="w", pady=(0, 15))

    # Datos del paciente
    boxPaciente = ttk.LabelFrame(frm, text="Información del paciente",
                                 style="Card.TLabelframe", padding=15)
    boxPaciente.pack(fill="x", pady=(0, 15))

    lblNombre = ttk.Label(boxPaciente, text="Nombre:")
    lblNombre.grid(row=0, column=0, sticky="w")
    entNombre = ttk.Entry(boxPaciente, width=30, font=("Verdana", 11))
    entNombre.grid(row=1, column=0, padx=(0, 20), pady=5)

    lblEdad = ttk.Label(boxPaciente, text="Edad:")
    lblEdad.grid(row=0, column=1, sticky="w")
    entEdad = ttk.Entry(boxPaciente, width=8, font=("Verdana", 11))
    entEdad.grid(row=1, column=1, padx=(0, 20), pady=5)

    lblFecha = ttk.Label(boxPaciente, text="Fecha de registro:")
    lblFecha.grid(row=0, column=2, sticky="w")
    entFecha = ttk.Entry(boxPaciente, width=14, font=("Verdana", 11))
    entFecha.grid(row=1, column=2, pady=5)
    entFecha.insert(0, "dd/mm/aaaa")

    # Medicamentos
    boxMed = ttk.LabelFrame(frm, text="Medicamentos",
                            style="Card.TLabelframe", padding=15)
    boxMed.pack(fill="x")

    lblMed = ttk.Label(boxMed, text="Medicamento:")
    lblMed.grid(row=0, column=0, sticky="w")
    cmbMedicamento = ttk.Combobox(
        boxMed, values=["Metformina", "Losartán", "Aspirina", "Omeprazol"],
        font=("Verdana", 11), width=22)
    cmbMedicamento.grid(row=1, column=0, padx=(0, 20), pady=5)

    lblDosis = ttk.Label(boxMed, text="Dosis:")
    lblDosis.grid(row=0, column=1, sticky="w")
    entDosis = ttk.Entry(boxMed, width=12, font=("Verdana", 11))
    entDosis.grid(row=1, column=1, padx=(0, 20), pady=5)

    lblHora = ttk.Label(boxMed, text="Horario:")
    lblHora.grid(row=0, column=2, sticky="w")
    cmbHora = ttk.Combobox(boxMed, values=["08:00", "12:00", "16:00", "20:00"],
                           font=("Verdana", 11), width=10)
    cmbHora.grid(row=1, column=2, padx=(0, 20), pady=5)

    varRecordatorio = tk.BooleanVar(value=True)
    chkRecordatorio = ttk.Checkbutton(boxMed, text="Activar recordatorio",
                                      variable=varRecordatorio)
    chkRecordatorio.grid(row=1, column=3)

    # Funciones
    def limpiar():
        entNombre.delete(0, "end")
        entEdad.delete(0, "end")
        entFecha.delete(0, "end")
        entDosis.delete(0, "end")
        cmbMedicamento.set("")
        cmbHora.set("")
        varRecordatorio.set(True)

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
                f.write(f"Nombre: {nombre}\n")
                f.write(f"Edad: {edad_txt}\n")
                f.write(f"Fecha: {entFecha.get()}\n")
                f.write(f"Medicamento: {cmbMedicamento.get()}\n")
                f.write(f"Dosis: {entDosis.get()}\n")
                f.write(f"Horario: {cmbHora.get()}\n")
                f.write(f"Recordatorio: {'Sí' if varRecordatorio.get() else 'No'}\n")
            messagebox.showinfo("OK", "Datos guardados.")

    # Botones
    botones = ttk.Frame(frm)
    botones.pack(side="bottom", anchor="e", pady=10)
    btnLimpiar = ttk.Button(botones, text="Limpiar", style="Limpiar.TButton",
                            command=limpiar)
    btnLimpiar.pack(side="left", padx=5)
    btnGuardar = ttk.Button(botones, text="Guardar registro",
                            style="Guardar.TButton", command=validar_y_guardar)
    btnGuardar.pack(side="left", padx=5)

    return win


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    w = open_win_form(root)
    w.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()