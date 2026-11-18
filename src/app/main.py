import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Proyecto Integrador - Medilink")
    root.geometry("780x340")


    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)
    
    

    ttk.Label(frame, text="MediLink", font=("Segoe UI", 12, "bold")).pack(pady=(0, 12))
    ttk.Button(frame, text="1) Usuario", command=lambda: open_win_home(root)).pack(pady=8)

    fila = ttk.Frame (frame)
    fila.pack(pady=8)
    ttk.Button(fila, text="2) Registro médico", width=20, padding=(10, 15), command=lambda: open_win_form(root)).pack(side="left", padx=5)
    ttk.Button(fila, text="3) Lista de síntomas",width=20, padding=(10, 15), command=lambda: open_win_list(root)).pack(side="left", padx=5)
    ttk.Button(fila, text="4) Historial Médico",width=20, padding=(10, 15), command=lambda: open_win_table(root)).pack(side="left", padx=5)
    ttk.Button(fila, text="5) Canvas (Gráficas)",width=20, padding=(10, 15), command=lambda: open_win_canvas(root)).pack(side="left", padx=5)
    ttk.Separator(frame).pack(pady=6, fill="x")
    ttk.Button(frame, text="Salir", command=root.destroy).pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    main()