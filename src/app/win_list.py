import time
import tkinter as tk
from tkinter import ttk, messagebox


FONDO = "#EAF3FF"      
BLANCO = "#FFFFFF"   
BOTON = "#D6E7FF"     
BORDE = "#243B5A"    
TEXTO = "#1F2937"      
DETALLE = "#6B9BD2"    
GRIS = "#7A8699"      
FUENTE = "Segoe UI"

PLACEHOLDER = "Escribe aquí..."


DATOS_INICIALES = [
    ("Dolor de cabeza", "12/11/2026"),
    ("Cansancio", "13/11/2026"),
    ("Mareos", "15/11/2026"),
    ("Náuseas", "16/11/2026"),
]


def _crear_boton(padre, texto, comando, ancho=14):
    """Botón plano con borde azul marino y un efecto simple al pasar el mouse."""
    b = tk.Button(padre, text=texto, command=comando, width=ancho,
                  bg=BOTON, fg=TEXTO, activebackground=BLANCO,
                  activeforeground=TEXTO, relief="flat", bd=0,
                  highlightthickness=2, highlightbackground=BORDE,
                  font=(FUENTE, 10, "bold"), cursor="hand2", pady=6)
    b.bind("<Enter>", lambda e: b.config(bg=BLANCO))
    b.bind("<Leave>", lambda e: b.config(bg=BOTON))
    return b


def open_win_list(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("MediLink - Lista de seguimiento")
    win.geometry("560x640")
    win.minsize(480, 560)
    win.configure(bg=FONDO)

   
    sintomas = list(DATOS_INICIALES)

    
    encabezado = tk.Frame(win, bg=BLANCO)
    encabezado.pack(fill="x")
    tk.Label(encabezado, text="MediLink - Lista de seguimiento", bg=BLANCO,
             fg=TEXTO, font=(FUENTE, 11, "bold"), pady=10).pack()
    tk.Frame(win, bg=BORDE, height=2).pack(fill="x")

   
    tk.Label(win, text="Lista de seguimiento", bg=FONDO, fg=TEXTO,
             font=(FUENTE, 24, "bold")).pack(pady=(18, 4))
    tk.Frame(win, bg=DETALLE, height=3, width=90).pack(pady=(0, 14))

    cuerpo = tk.Frame(win, bg=FONDO)
    cuerpo.pack(fill="both", expand=True, padx=32, pady=(0, 16))

   
    tk.Label(cuerpo, text="Síntoma", bg=FONDO, fg=TEXTO,
             font=(FUENTE, 11, "bold")).pack(anchor="w")

    ent = tk.Entry(cuerpo, font=(FUENTE, 11), bg=BLANCO, fg=GRIS, relief="flat",
                   highlightthickness=2, highlightbackground=BORDE,
                   highlightcolor=DETALLE, insertbackground=TEXTO)
    ent.pack(fill="x", pady=(6, 8), ipady=6)

    estado = {"placeholder": False}           

    def mostrar_placeholder(event=None):
        if not ent.get():
            ent.insert(0, PLACEHOLDER)
            ent.config(fg=GRIS)
            estado["placeholder"] = True

    def quitar_placeholder(event=None):
        if estado["placeholder"]:
            ent.delete(0, "end")
            ent.config(fg=TEXTO)
            estado["placeholder"] = False

    def texto_ingresado():
        """Texto escrito por el usuario (vacío si solo está el placeholder)."""
        return "" if estado["placeholder"] else ent.get().strip()

    ent.bind("<FocusIn>", quitar_placeholder)
    ent.bind("<FocusOut>", mostrar_placeholder)
    mostrar_placeholder()

    
    _crear_boton(cuerpo, "Agregar", lambda: agregar()).pack(fill="x", pady=(0, 14))

   
    marco_lista = tk.Frame(cuerpo, bg=BLANCO, highlightthickness=2,
                           highlightbackground=BORDE)
    marco_lista.pack(fill="both", expand=True)

    scroll = ttk.Scrollbar(marco_lista, orient="vertical")
    scroll.pack(side="right", fill="y", padx=(0, 2), pady=2)
    lb = tk.Listbox(marco_lista, font=(FUENTE, 11), bg=BLANCO, fg=TEXTO,
                    bd=0, highlightthickness=0, relief="flat",
                    selectbackground=BOTON, selectforeground=TEXTO,
                    activestyle="none", exportselection=False,
                    yscrollcommand=scroll.set)
    lb.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=8)
    scroll.config(command=lb.yview)


    def refrescar():
        """Redibuja el Listbox: cada síntoma lleva número y fecha de registro."""
        lb.delete(0, "end")
        for n, (texto, fecha) in enumerate(sintomas, start=1):
            lb.insert("end", f"{n}.  {texto}   ·   {fecha}")

    def agregar(event=None):
        texto = texto_ingresado()
        if not texto:                          
            messagebox.showwarning("Aviso", "Escribe un síntoma antes de agregar.",
                                   parent=win)
            ent.focus_set()
            return
        sintomas.append((texto, time.strftime("%d/%m/%Y")))
        refrescar()
        lb.see("end")
        ent.delete(0, "end")                   
        messagebox.showinfo("Registro agregado",
                            "Síntoma agregado correctamente a la lista.", parent=win)
        ent.focus_set()

    def eliminar():
        sel = lb.curselection()
        if not sel:                           
            messagebox.showinfo("Aviso", "Selecciona un síntoma de la lista "
                                "para eliminarlo.", parent=win)
            return
        del sintomas[sel[0]]                 
        refrescar()                            

    def limpiar():
        if not sintomas:
            messagebox.showinfo("Aviso", "La lista ya está vacía.", parent=win)
            return
        if messagebox.askyesno("Limpiar lista",
                               "¿Seguro que deseas eliminar todos los síntomas?",
                               parent=win):
            sintomas.clear()
            refrescar()

    def regresar():
        win.destroy()

    ent.bind("<Return>", agregar)              
    
    inferior = tk.Frame(cuerpo, bg=FONDO)
    inferior.pack(fill="x", pady=(14, 0))
    inferior.columnconfigure(0, weight=1)
    inferior.columnconfigure(1, weight=1)
    _crear_boton(inferior, "Eliminar", eliminar).grid(row=0, column=0, sticky="w")
    _crear_boton(inferior, "Limpiar lista", limpiar).grid(row=0, column=1, sticky="e")
    _crear_boton(inferior, "Regresar", regresar).grid(row=1, column=0, sticky="w",
                                                      pady=(10, 0))

    refrescar()                                

if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Prueba win_list")
    ttk.Button(raiz, text="Abrir lista",
               command=lambda: open_win_list(raiz)).pack(padx=40, pady=40)
    raiz.mainloop()
