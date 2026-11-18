import tkinter as tk
from tkinter import ttk, messagebox


def open_win_form(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Registro información médica")
    win.geometry("900x620")
    win.resizable(False, False)

    fondo = "#EAF1FC"
    blanco = "#FFFFFF"
    azul = "#2F6FE0"
    borde = "#C9D6EE"
    texto = "#1B2A4A"
    campo = "#F5F8FE"

    cv = tk.Canvas(win, width=900, height=620, bg=fondo, highlightthickness=0)
    cv.pack()

    def figura(x1, y1, x2, y2, r, color, etiqueta):
        cv.create_oval(x1, y1, x1 + 2*r, y1 + 2*r, fill=color, outline=color, tags=etiqueta)
        cv.create_oval(x2 - 2*r, y1, x2, y1 + 2*r, fill=color, outline=color, tags=etiqueta)
        cv.create_oval(x1, y2 - 2*r, x1 + 2*r, y2, fill=color, outline=color, tags=etiqueta)
        cv.create_oval(x2 - 2*r, y2 - 2*r, x2, y2, fill=color, outline=color, tags=etiqueta)
        cv.create_rectangle(x1 + r, y1, x2 - r, y2, fill=color, outline=color, tags=etiqueta)
        cv.create_rectangle(x1, y1 + r, x2, y2 - r, fill=color, outline=color, tags=etiqueta)

    def redondo(x1, y1, x2, y2, r, relleno, contorno, etiqueta=""):
        figura(x1, y1, x2, y2, r, contorno, etiqueta)
        figura(x1 + 2, y1 + 2, x2 - 2, y2 - 2, r, relleno, etiqueta)

    def boton(x1, y1, x2, y2, txt, relleno, color_txt, comando, etiqueta):
        redondo(x1, y1, x2, y2, 18, relleno, azul, etiqueta)
        cv.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=txt, fill=color_txt, font=("Verdana", 11, "bold"), tags=etiqueta)
        cv.tag_bind(etiqueta, "<Button-1>", lambda e: comando())
        cv.tag_bind(etiqueta, "<Enter>", lambda e: cv.config(cursor="hand2"))
        cv.tag_bind(etiqueta, "<Leave>", lambda e: cv.config(cursor=""))

    def regresar():
        win.destroy()
        parent.deiconify()

    def limpiar():
        entNombre.delete(0, "end")
        entEdad.delete(0, "end")
        entFecha.delete(0, "end")
        entDosis.delete(0, "end")
        cmbMedicamento.set("")
        cmbHora.set("")
        varRecordatorio.set(1)

    def validar_y_guardar():
        nombre = entNombre.get().strip()
        edad_txt = entEdad.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre es requerido.")
            return
        if not edad_txt.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return
        with open("registros.txt", "a", encoding="utf-8") as f:
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Edad: {edad_txt}\n")
            f.write(f"Fecha: {entFecha.get()}\n")
            f.write(f"Medicamento: {cmbMedicamento.get()}\n")
            f.write(f"Dosis: {entDosis.get()}\n")
            f.write(f"Horario: {cmbHora.get()}\n")
            f.write(f"Recordatorio: {'Sí' if varRecordatorio.get() else 'No'}\n")
            f.write("-" * 30 + "\n")
        messagebox.showinfo("OK", "Datos guardados.")
        limpiar()

    boton(30, 20, 160, 58, "← Regresar", blanco, azul, regresar, "btnRegresar")

    cv.create_text(30, 85, text="Registro de información médica", anchor="nw", fill=texto, font=("Verdana", 20, "bold"))
    cv.create_text(30, 125, text="Mantén un registro de tu tratamiento y cómo te sientes", anchor="nw", fill="#8A96AE", font=("Verdana", 10))

    redondo(30, 165, 870, 305, 18, blanco, borde)
    cv.create_text(50, 180, text="Información del paciente", anchor="nw", fill=texto, font=("Verdana", 13, "bold"))

    lblNombre = tk.Label(cv, text="Nombre:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblNombre.place(x=50, y=222)
    entNombre = tk.Entry(cv, font=("Verdana", 11), bg=campo, relief="flat", highlightthickness=1, highlightbackground=borde, highlightcolor=azul)
    entNombre.place(x=50, y=248, width=330, height=32)

    lblEdad = tk.Label(cv, text="Edad:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblEdad.place(x=410, y=222)
    entEdad = tk.Entry(cv, font=("Verdana", 11), bg=campo, relief="flat", highlightthickness=1, highlightbackground=borde, highlightcolor=azul)
    entEdad.place(x=410, y=248, width=100, height=32)

    lblFecha = tk.Label(cv, text="Fecha de registro:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblFecha.place(x=540, y=222)
    entFecha = tk.Entry(cv, font=("Verdana", 11), bg=campo, relief="flat", highlightthickness=1, highlightbackground=borde, highlightcolor=azul)
    entFecha.place(x=540, y=248, width=170, height=32)

    redondo(30, 325, 870, 475, 18, blanco, borde)
    cv.create_text(50, 340, text="Medicamentos", anchor="nw", fill=texto, font=("Verdana", 13, "bold"))

    lblMedicamento = tk.Label(cv, text="Medicamento:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblMedicamento.place(x=50, y=382)
    cmbMedicamento = ttk.Combobox(cv, values=["Metformina", "Losartán", "Aspirina", "Omeprazol"], font=("Verdana", 11))
    cmbMedicamento.place(x=50, y=408, width=240, height=32)

    lblDosis = tk.Label(cv, text="Dosis:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblDosis.place(x=320, y=382)
    entDosis = tk.Entry(cv, font=("Verdana", 11), bg=campo, relief="flat", highlightthickness=1, highlightbackground=borde, highlightcolor=azul)
    entDosis.place(x=320, y=408, width=140, height=32)

    lblHora = tk.Label(cv, text="Horario:", bg=blanco, fg=texto, font=("Verdana", 10, "bold"))
    lblHora.place(x=490, y=382)
    cmbHora = ttk.Combobox(cv, values=["08:00", "12:00", "16:00", "20:00"], font=("Verdana", 11))
    cmbHora.place(x=490, y=408, width=130, height=32)

    varRecordatorio = tk.IntVar(value=1)
    chkRecordatorio = tk.Checkbutton(cv, text="Activar recordatorio", variable=varRecordatorio, bg=blanco, fg=texto, activebackground=blanco, font=("Verdana", 10))
    chkRecordatorio.place(x=660, y=410)

    boton(540, 520, 700, 565, "Limpiar", blanco, azul, limpiar, "btnLimpiar")
    boton(710, 520, 870, 565, "Guardar", azul, "white", validar_y_guardar, "btnGuardar")

    return win


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    w = open_win_form(root)
    w.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()