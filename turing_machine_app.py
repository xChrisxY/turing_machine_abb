import tkinter as tk
from tkinter import ttk

# Configuración de la máquina de Turing: (estado, símbolo) -> (nuevo_estado, símbolo_escrito, dirección)
RIGHT = 1  
STAY = 0  

transitions = {
    ('q0', 'a'): ('q1', 'a', RIGHT),
    ('q1', 'b'): ('q2', 'b', RIGHT),
    ('q2', 'b'): ('q3', 'b', RIGHT),
    ('q3', 'a'): ('q1', 'a', RIGHT),
    ('q3', '□'): ('q_accept', '□', STAY)
}

def turing_machine(tape):
    tape = list(tape) + ['□']  
    head = 0  
    state = 'q0'

    while state != 'q_accept':
        symbol = tape[head]
        if (state, symbol) in transitions:
            new_state, write_symbol, direction = transitions[(state, symbol)]
            tape[head] = write_symbol  
            head += direction  
            state = new_state  
        else:
            return False  
    return True  

def check_tapes():
   
    for tape in tapes:
        accepted = turing_machine(tape)


        row = len(result_frame.grid_slaves()) // 2 + 1  
        bg_color = "#A7F3D0" if accepted else "#FECACA"  

        tk.Label(result_frame, text=tape, font=('Arial', 10), bg=bg_color, width=25, relief="solid").grid(
            row=row, column=0, padx=5, pady=2)

        result_text = "ACEPTADA" if accepted else "RECHAZADA"
        tk.Label(result_frame, text=result_text, font=('Arial', 10), bg=bg_color, width=25, relief="solid").grid(
            row=row, column=1, padx=5, pady=2)

    tapes.clear()  

def add_entry():
    """Agrega una entrada a la lista de cadenas."""
    tape = entry_var.get()
    if tape:  
        tapes.append(tape)
        entry_var.set("")  

root = tk.Tk()
root.title("Simulación de Máquina de Turing - Patrón 'abb'")
root.geometry("600x600")
root.configure(bg="#1E293B")

tapes = []  
style = ttk.Style()
style.theme_use("clam")  # Usar tema moderno 'clam'
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TEntry", font=("Arial", 12), padding=5)

title_label = tk.Label(root, text="Máquina de Turing", font=("Arial", 20, "bold"), bg="#1E293B", fg="#F1F5F9")
title_label.pack(pady=10)

entry_var = tk.StringVar()
entry_field = ttk.Entry(root, textvariable=entry_var, width=40)
entry_field.pack(pady=10)

button_frame = tk.Frame(root, bg="#1E293B")
button_frame.pack(pady=5)

add_button = ttk.Button(button_frame, text="Agregar Cadena", command=add_entry)
add_button.grid(row=0, column=0, padx=5)

check_button = ttk.Button(button_frame, text="Validar Cadenas", command=check_tapes)
check_button.grid(row=0, column=1, padx=5)

result_frame = tk.Frame(root, bg="#1E293B")
result_frame.pack(pady=20)

tk.Label(result_frame, text="Cadena", font=('Arial', 12, 'bold'), width=25, bg="#374151", fg="#F1F5F9", relief="solid").grid(
    row=0, column=0, padx=5, pady=5)
tk.Label(result_frame, text="Resultado", font=('Arial', 12, 'bold'), width=25, bg="#374151", fg="#F1F5F9", relief="solid").grid(
    row=0, column=1, padx=5, pady=5)

root.mainloop()

