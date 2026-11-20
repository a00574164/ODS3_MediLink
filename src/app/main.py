import tkinter as tk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas


def crear_boton_redondeado(parent, width, height, radius, bg_color, hover_color, text, text_color, font, command):
    canvas = tk.Canvas(
        parent,
        width=width,
        height=height,
        bg=parent["bg"],
        highlightthickness=0,
        cursor="hand2"
    )

    puntos = [
        radius, 0,
        width - radius, 0,
        width, 0,
        width, radius,
        width, height - radius,
        width, height,
        width - radius, height,
        radius, height,
        0, height,
        0, height - radius,
        0, radius,
        0, 0
    ]

    fondo = canvas.create_polygon(puntos, smooth=True, fill=bg_color, outline="")
    texto = canvas.create_text(width / 2, height / 2, text=text, fill=text_color, font=font)

    canvas.bind("<Button-1>", lambda e: command())
    canvas.bind("<Enter>", lambda e: canvas.itemconfig(fondo, fill=hover_color))
    canvas.bind("<Leave>", lambda e: canvas.itemconfig(fondo, fill=bg_color))

    return canvas


def main():
    root = tk.Tk()
    root.title("MediLink - Menú principal")
    root.geometry("500x410")
    root.resizable(False, False)

    COLOR_FONDO = "EEF4FA"
    COLOR_PRIMARIO = "0E3156"
    COLOR_PRIMARIO_HOVER = "174678"
    COLOR_SECUNDARIO = "D4E4F7"
    COLOR_SECUNDARIO_HOVER = "C0D7F2"
    COLOR_SUBTITULO = "4A90D9"

    root.configure(bg=f"#{COLOR_FONDO}")

    main_frame = tk.Frame(root, bg=f"#{COLOR_FONDO}")
    main_frame.pack(expand=True, fill="both", padx=35, pady=25)

    tk.Label(
        main_frame,
        text="MediLink",
        font=("Segoe UI", 24, "bold"),
        fg=f"#{COLOR_PRIMARIO}",
        bg=f"#{COLOR_FONDO}"
    ).pack(pady=(5, 0))

    tk.Label(
        main_frame,
        text="Menú principal",
        font=("Segoe UI", 13),
        fg=f"#{COLOR_SUBTITULO}",
        bg=f"#{COLOR_FONDO}"
    ).pack(pady=(0, 6))

    linea_canvas = tk.Canvas(main_frame, width=65, height=4, bg=f"#{COLOR_FONDO}", highlightthickness=0)
    linea_canvas.create_line(2, 2, 63, 2, fill="#63A4E8", width=3, capstyle=tk.ROUND)
    linea_canvas.pack(pady=(0, 25))

    grid_frame = tk.Frame(main_frame, bg=f"#{COLOR_FONDO}")
    grid_frame.pack()

    fuente_btn = ("Segoe UI", 11, "bold")
    ancho_btn = 195
    alto_btn = 54
    radio = 16

    btn_registro = crear_boton_redondeado(
        grid_frame, ancho_btn, alto_btn, radio,
        f"#{COLOR_PRIMARIO}", f"#{COLOR_PRIMARIO_HOVER}",
        "Registro médico", "white", fuente_btn,
        lambda: open_win_form(root)
    )
    btn_registro.grid(row=0, column=0, padx=10, pady=8)

    btn_sintomas = crear_boton_redondeado(
        grid_frame, ancho_btn, alto_btn, radio,
        f"#{COLOR_PRIMARIO}", f"#{COLOR_PRIMARIO_HOVER}",
        "Lista de síntomas", "white", fuente_btn,
        lambda: open_win_list(root)
    )
    btn_sintomas.grid(row=0, column=1, padx=10, pady=8)

    btn_historial = crear_boton_redondeado(
        grid_frame, ancho_btn, alto_btn, radio,
        f"#{COLOR_PRIMARIO}", f"#{COLOR_PRIMARIO_HOVER}",
        "Historial médico", "white", fuente_btn,
        lambda: open_win_table(root)
    )
    btn_historial.grid(row=1, column=0, padx=10, pady=8)

    btn_graficas = crear_boton_redondeado(
        grid_frame, ancho_btn, alto_btn, radio,
        f"#{COLOR_PRIMARIO}", f"#{COLOR_PRIMARIO_HOVER}",
        "Gráficas y reportes", "white", fuente_btn,
        lambda: open_win_canvas(root)
    )
    btn_graficas.grid(row=1, column=1, padx=10, pady=8)

    btn_salir = crear_boton_redondeado(
        main_frame, (ancho_btn * 2) + 20, 46, radio,
        f"#{COLOR_SECUNDARIO}", f"#{COLOR_SECUNDARIO_HOVER}",
        "Cerrar sesión", f"#{COLOR_PRIMARIO}", fuente_btn,
        root.destroy
    )
    btn_salir.pack(pady=(22, 0))

    root.mainloop()


if __name__ == "__main__":
    main()