"""
MediLink — Ventana 5: Canvas (visualización del progreso del paciente).

Se conserva la función de entrada original `open_win_canvas(parent)`, por lo
que main.py no necesita cambios si ya importaba esa función.

Solo usa librerías estándar (tkinter). Todos los datos son ficticios.
"""
import time
import tkinter as tk
from tkinter import ttk


C = {
    "fondo": "#EAF4FB",      
    "tarjeta": "#FFFFFF",    
    "borde": "#D3E4F2",
    "marino": "#12355B",    
    "azul": "#2E86C1",       
    "azul_claro": "#D6EAF8", 
    "verde": "#27AE60",
    "ambar": "#F39C12",
    "rojo": "#E74C3C",
    "texto": "#2C3E50",
    "gris": "#7F8C8D",
    "rejilla": "#E3EDF5",
}
FUENTE = "Segoe UI"


MESES = ["Junio 2026", "Julio 2026", "Agosto 2026",
         "Septiembre 2026", "Octubre 2026", "Noviembre 2026"]

DATOS = {
    "Junio 2026": {
        "bienestar": 58,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 44, 60),
                         ("Losartán", "50 mg · 1 vez al día", 20, 30),
                         ("Atorvastatina", "20 mg · en la noche", 18, 30)],
        "sintomas": [("Fatiga", 14), ("Dolor de cabeza", 10), ("Mareo", 7),
                     ("Náuseas", 5), ("Insomnio", 11)],
    },
    "Julio 2026": {
        "bienestar": 63,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 49, 62),
                         ("Losartán", "50 mg · 1 vez al día", 23, 31),
                         ("Atorvastatina", "20 mg · en la noche", 22, 31)],
        "sintomas": [("Fatiga", 12), ("Dolor de cabeza", 9), ("Mareo", 6),
                     ("Náuseas", 4), ("Insomnio", 10)],
    },
    "Agosto 2026": {
        "bienestar": 67,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 53, 62),
                         ("Losartán", "50 mg · 1 vez al día", 26, 31),
                         ("Atorvastatina", "20 mg · en la noche", 25, 31)],
        "sintomas": [("Fatiga", 10), ("Dolor de cabeza", 8), ("Mareo", 5),
                     ("Náuseas", 3), ("Insomnio", 8)],
    },
    "Septiembre 2026": {
        "bienestar": 72,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 55, 60),
                         ("Losartán", "50 mg · 1 vez al día", 27, 30),
                         ("Atorvastatina", "20 mg · en la noche", 27, 30)],
        "sintomas": [("Fatiga", 8), ("Dolor de cabeza", 6), ("Mareo", 4),
                     ("Náuseas", 2), ("Insomnio", 7)],
    },
    "Octubre 2026": {
        "bienestar": 78,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 58, 62),
                         ("Losartán", "50 mg · 1 vez al día", 29, 31),
                         ("Atorvastatina", "20 mg · en la noche", 29, 31)],
        "sintomas": [("Fatiga", 6), ("Dolor de cabeza", 5), ("Mareo", 3),
                     ("Náuseas", 1), ("Insomnio", 5)],
    },
    "Noviembre 2026": {
        "bienestar": 83,
        "medicamentos": [("Metformina", "850 mg · 2 veces al día", 28, 30),
                         ("Losartán", "50 mg · 1 vez al día", 15, 15),
                         ("Atorvastatina", "20 mg · en la noche", 14, 15)],
        "sintomas": [("Fatiga", 4), ("Dolor de cabeza", 3), ("Mareo", 2),
                     ("Náuseas", 1), ("Insomnio", 3)],
    },
}



def _tam(cv):
    """Tamaño real del canvas (usa el tamaño pedido si aún no se dibuja)."""
    w, h = cv.winfo_width(), cv.winfo_height()
    if w <= 1 or h <= 1:
        w, h = int(cv["width"]), int(cv["height"])
    return w, h


def _color_cumplimiento(pct):
    """Verde = alto, ámbar = medio, rojo = bajo."""
    if pct >= 90:
        return C["verde"]
    if pct >= 75:
        return C["ambar"]
    return C["rojo"]


def _cumplimiento_global(meds):
    tomadas = sum(m[2] for m in meds)
    programadas = sum(m[3] for m in meds)
    return round(100 * tomadas / programadas) if programadas else 0


def _crear_tarjeta(padre, titulo, subtitulo, fila, columna):
    """Tarjeta blanca con título y un Canvas; devuelve el Canvas."""
    tarjeta = tk.Frame(padre, bg=C["tarjeta"], highlightthickness=1,
                       highlightbackground=C["borde"])
    tarjeta.grid(row=fila, column=columna, sticky="nsew", padx=6, pady=6)

    tk.Label(tarjeta, text=titulo, bg=C["tarjeta"], fg=C["marino"],
             font=(FUENTE, 12, "bold"), anchor="w"
             ).pack(fill="x", padx=14, pady=(10, 0))
    tk.Label(tarjeta, text=subtitulo, bg=C["tarjeta"], fg=C["gris"],
             font=(FUENTE, 9), anchor="w").pack(fill="x", padx=14)

    cv = tk.Canvas(tarjeta, width=300, height=170, bg=C["tarjeta"],
                   highlightthickness=0)
    cv.pack(fill="both", expand=True, padx=10, pady=(4, 10))
    return cv



def dibujar_evolucion(cv, sel):
    """Línea de bienestar por mes; resalta el mes seleccionado."""
    cv.delete("all")
    w, h = _tam(cv)
    izq, der, arr, aba = 48, 24, 26, 36
    ancho, alto = w - izq - der, h - arr - aba
    if ancho < 60 or alto < 50:
        return

    
    for v in range(0, 101, 20):
        y = arr + alto - alto * v / 100
        cv.create_line(izq, y, w - der, y, fill=C["rejilla"])
        cv.create_text(izq - 8, y, text=str(v), anchor="e",
                       fill=C["gris"], font=(FUENTE, 8))
    cv.create_text(12, arr + alto / 2, text="Bienestar (%)", angle=90,
                   fill=C["gris"], font=(FUENTE, 9))
    cv.create_line(izq, arr + alto, w - der, arr + alto, fill=C["gris"])
    cv.create_line(izq, arr, izq, arr + alto, fill=C["gris"])

    
    valores = [DATOS[m]["bienestar"] for m in MESES]
    n = len(valores)
    pts = [(izq + ancho * i / (n - 1), arr + alto - alto * v / 100)
           for i, v in enumerate(valores)]

    
    base = arr + alto
    poly = [pts[0][0], base] + [k for p in pts for k in p] + [pts[-1][0], base]
    cv.create_polygon(poly, fill=C["azul_claro"], outline="")
    cv.create_line([k for p in pts for k in p], fill=C["azul"], width=3)

    
    for i, ((x, y), v) in enumerate(zip(pts, valores)):
        activo = (i == sel)
        r = 7 if activo else 4
        cv.create_oval(x - r, y - r, x + r, y + r,
                       fill=C["verde"] if activo else C["tarjeta"],
                       outline=C["verde"] if activo else C["azul"], width=2)
        cv.create_text(x, y - 16, text=str(v),
                       fill=C["verde"] if activo else C["texto"],
                       font=(FUENTE, 9, "bold" if activo else "normal"))
        cv.create_text(x, base + 14, text=MESES[i].split()[0][:3],
                       fill=C["marino"] if activo else C["gris"],
                       font=(FUENTE, 9, "bold" if activo else "normal"))


def dibujar_medicamentos(cv, meds):
    """Barras de progreso: cumplimiento reportado por medicamento."""
    cv.delete("all")
    w, h = _tam(cv)
    fila = h / len(meds)
    pad = 6
    x1, x2 = pad, w - pad - 52         
    for i, (nombre, detalle, tomadas, prog) in enumerate(meds):
        y0 = i * fila
        pct = round(100 * tomadas / prog)
        color = _color_cumplimiento(pct)
        yb = y0 + fila * 0.55           

        cv.create_text(pad, y0 + fila * 0.2, text=nombre, anchor="w",
                       fill=C["marino"], font=(FUENTE, 10, "bold"))
        cv.create_text(w - pad, y0 + fila * 0.2, text=detalle, anchor="e",
                       fill=C["gris"], font=(FUENTE, 8))
        
        cv.create_line(x1, yb, x2, yb, width=12, capstyle="round",
                       fill=C["rejilla"])
        fin = x1 + (x2 - x1) * pct / 100
        cv.create_line(x1, yb, max(fin, x1 + 0.1), yb, width=12,
                       capstyle="round", fill=color)
        cv.create_text(w - pad, yb, text=f"{pct}%", anchor="e", fill=color,
                       font=(FUENTE, 11, "bold"))
        cv.create_text(pad, y0 + fila * 0.83,
                       text=f"{tomadas} de {prog} dosis reportadas",
                       anchor="w", fill=C["gris"], font=(FUENTE, 8))


def dibujar_sintomas(cv, sintomas):
    """Gráfica de barras verticales con la frecuencia de cada síntoma."""
    cv.delete("all")
    w, h = _tam(cv)
    izq, der, arr, aba = 36, 12, 22, 40
    ancho, alto = w - izq - der, h - arr - aba
    if ancho < 60 or alto < 50 or not sintomas:
        return

    datos = sorted(sintomas, key=lambda s: s[1], reverse=True)
    tope = ((max(v for _, v in datos) // 4) + 1) * 4  

    
    for k in range(5):
        v = tope * k / 4
        y = arr + alto - alto * v / tope
        cv.create_line(izq, y, w - der, y, fill=C["rejilla"])
        cv.create_text(izq - 6, y, text=f"{v:g}", anchor="e",
                       fill=C["gris"], font=(FUENTE, 8))
    base = arr + alto
    cv.create_line(izq, base, w - der, base, fill=C["gris"])

    
    ranura = ancho / len(datos)
    ancho_barra = min(52, ranura * 0.55)
    for i, (nombre, v) in enumerate(datos):
        cx = izq + ranura * (i + 0.5)
        y = base - alto * v / tope
        color = C["azul"] if i else C["marino"]         
        cv.create_rectangle(cx - ancho_barra / 2, y, cx + ancho_barra / 2,
                            base, fill=color, outline="")
        cv.create_text(cx, y - 9, text=str(v), fill=C["marino"],
                       font=(FUENTE, 9, "bold"))
        cv.create_text(cx, base + 6, text=nombre, anchor="n",
                       width=max(ranura - 4, 30), justify="center",
                       fill=C["texto"], font=(FUENTE, 8))


def dibujar_resumen(cv, idx):
    """Indicador circular de cumplimiento + datos clave del mes."""
    cv.delete("all")
    w, h = _tam(cv)
    mes = MESES[idx]
    d = DATOS[mes]
    pct = _cumplimiento_global(d["medicamentos"])
    color = _color_cumplimiento(pct)

    
    r = max(min(h / 2 - 12, w * 0.22), 25)
    cx, cy = r + 16, h / 2
    cv.create_oval(cx - r, cy - r, cx + r, cy + r, outline=C["rejilla"], width=14)
    if pct > 0:
        cv.create_arc(cx - r, cy - r, cx + r, cy + r, start=90,
                      extent=-359.9 * pct / 100, style="arc",
                      outline=color, width=14)
    cv.create_text(cx, cy - 6, text=f"{pct}%", fill=color,
                   font=(FUENTE, int(max(12, r / 2.6)), "bold"))
    cv.create_text(cx, cy + r * 0.32, text="cumplimiento", fill=C["gris"],
                   font=(FUENTE, 8))

    
    x = cx + r + 28
    bien = d["bienestar"]
    if idx > 0:
        dif = bien - DATOS[MESES[idx - 1]]["bienestar"]
        var_txt = f"{'▲' if dif >= 0 else '▼'} {abs(dif)} pts vs. mes anterior"
        var_col = C["verde"] if dif >= 0 else C["rojo"]
    else:
        var_txt, var_col = "Primer mes registrado", C["gris"]
    total_sint = sum(v for _, v in d["sintomas"])
    if bien >= 80:
        estado, est_col = "Evolución favorable", C["verde"]
    elif bien >= 65:
        estado, est_col = "Evolución estable", C["ambar"]
    else:
        estado, est_col = "Requiere atención", C["rojo"]

    cv.create_text(x, cy - 50, text=mes, anchor="w", fill=C["marino"],
                   font=(FUENTE, 13, "bold"))
    cv.create_text(x, cy - 22, text=f"Bienestar: {bien}/100", anchor="w",
                   fill=C["texto"], font=(FUENTE, 11))
    cv.create_text(x, cy - 2, text=var_txt, anchor="w", fill=var_col,
                   font=(FUENTE, 9, "bold"))
    cv.create_text(x, cy + 20, text=f"Síntomas reportados: {total_sint}",
                   anchor="w", fill=C["texto"], font=(FUENTE, 10))
    cv.create_text(x, cy + 44, text=estado, anchor="w", fill=est_col,
                   font=(FUENTE, 11, "bold"))



def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("MediLink — Progreso del paciente")
    win.geometry("1020x700")
    win.minsize(820, 560)
    win.configure(bg=C["fondo"])

    
    encabezado = tk.Frame(win, bg=C["marino"])
    encabezado.pack(fill="x")
    titulos = tk.Frame(encabezado, bg=C["marino"])
    titulos.pack(side="left", padx=16, pady=10)
    tk.Label(titulos, text="MediLink — Seguimiento médico conectado",
             bg=C["marino"], fg="white", font=(FUENTE, 15, "bold")).pack(anchor="w")
    tk.Label(titulos, text="Progreso del paciente · datos de demostración",
             bg=C["marino"], fg=C["azul_claro"], font=(FUENTE, 9)).pack(anchor="w")

    
    controles = tk.Frame(win, bg=C["fondo"])
    controles.pack(fill="x", padx=12, pady=(10, 0))
    tk.Label(controles, text="Mes:", bg=C["fondo"], fg=C["marino"],
             font=(FUENTE, 10, "bold")).pack(side="left", padx=(6, 4))

    var_mes = tk.StringVar(value=MESES[-1])          
    combo = ttk.Combobox(controles, textvariable=var_mes, values=MESES,
                         state="readonly", width=18)
    combo.pack(side="left")

    lbl_act = tk.Label(controles, text="", bg=C["fondo"], fg=C["gris"],
                       font=(FUENTE, 9))
    lbl_act.pack(side="left", padx=14)

    
    tk.Button(controles, text="← Regresar", command=win.destroy,
              bg=C["azul"], fg="white", activebackground=C["marino"],
              activeforeground="white", relief="flat", padx=12, pady=4,
              font=(FUENTE, 10, "bold"), cursor="hand2").pack(side="right", padx=4)
    
    tk.Button(controles, text="⟳ Actualizar", command=lambda: actualizar(),
              bg=C["verde"], fg="white", activebackground="#1E8449",
              activeforeground="white", relief="flat", padx=12, pady=4,
              font=(FUENTE, 10, "bold"), cursor="hand2").pack(side="right", padx=4)

    
    cuerpo = tk.Frame(win, bg=C["fondo"])
    cuerpo.pack(fill="both", expand=True, padx=6, pady=6)
    for i in range(2):
        cuerpo.columnconfigure(i, weight=1, uniform="col")
        cuerpo.rowconfigure(i, weight=1, uniform="fila")

    cv_evo = _crear_tarjeta(cuerpo, "Evolución mensual",
                            "Índice de bienestar del paciente (0–100)", 0, 0)
    cv_med = _crear_tarjeta(cuerpo, "Seguimiento de medicamentos",
                            "Cumplimiento reportado del tratamiento", 0, 1)
    cv_sin = _crear_tarjeta(cuerpo, "Frecuencia de síntomas",
                            "Veces que se reportó cada síntoma en el mes", 1, 0)
    cv_res = _crear_tarjeta(cuerpo, "Progreso mensual",
                            "Resumen del mes seleccionado", 1, 1)

    
    def redibujar(*_):
        """Dibuja las 4 tarjetas con el mes elegido en el selector."""
        if not win.winfo_exists():
            return
        idx = MESES.index(var_mes.get())
        d = DATOS[var_mes.get()]
        dibujar_evolucion(cv_evo, idx)
        dibujar_medicamentos(cv_med, d["medicamentos"])
        dibujar_sintomas(cv_sin, d["sintomas"])
        dibujar_resumen(cv_res, idx)

    def actualizar():
        
        redibujar()
        lbl_act.config(text="Actualizado: " + time.strftime("%H:%M:%S"))

    combo.bind("<<ComboboxSelected>>", redibujar)
    
    for cv in (cv_evo, cv_med, cv_sin, cv_res):
        cv.bind("<Configure>", redibujar)

    actualizar()



if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Prueba win_canvas")
    ttk.Button(raiz, text="Abrir ventana Canvas",
               command=lambda: open_win_canvas(raiz)).pack(padx=40, pady=40)
    raiz.mainloop()
