import itertools
from collections import defaultdict
import tkinter as tk
from tkinter import ttk, messagebox

class AFNDtoAFDConverter:
    def __init__(self):
        self.afnd = defaultdict(dict)
        self.afd = {}
        self.initial_state = None
        self.final_states = set()

    def input_afnd(self, afnd_input, initial_state_input, final_states_input):
        afnd_lines = afnd_input.strip().split('\n')
        for line in afnd_lines:
            from_state, transitions = line.strip().split('/')
            transitions = transitions.split(' ')
            self.afnd[from_state.strip()] = {chr(65 + i): set(states.split(',')) for i, states in enumerate(transitions)}
        
        self.initial_state = initial_state_input.strip()
        self.final_states = set(final_states_input.strip().split(','))

    def convert(self):
        unmarked_states = []
        afd_states = {}

        initial_afd_state = frozenset([self.initial_state])
        unmarked_states.append(initial_afd_state)
        afd_states[initial_afd_state] = {}

        while unmarked_states:
            current = unmarked_states.pop()
            current_dict = {}

            for symbol in map(chr, range(65, 91)):  # For A-Z
                next_state = frozenset(itertools.chain.from_iterable(self.afnd[state][symbol] for state in current if symbol in self.afnd[state]))
                
                if next_state and next_state not in afd_states:
                    unmarked_states.append(next_state)
                    afd_states[next_state] = {}
                
                if next_state:
                    current_dict[symbol] = next_state

            afd_states[current] = current_dict

        self.afd = afd_states

    def display_step_by_step_conversion(self):
        steps = ""
        for state, transitions in self.afd.items():
            steps += f"Estado: {','.join(state)}\n"
            for symbol, result in transitions.items():
                steps += f"  {symbol} -> {','.join(result)}\n"
        return steps

    def display_afd(self):
        afd_result = "AFD resultante:\n"
        afd_result += "Estados: " + ', '.join([','.join(state) for state in self.afd.keys()]) + "\n"
        for state, transitions in self.afd.items():
            afd_result += f"{','.join(state)}:\n"
            for symbol, result in transitions.items():
                afd_result += f"  {symbol} -> {','.join(result)}\n"
        return afd_result

    def is_final_state(self, state):
        return any(substate in self.final_states for substate in state)

    def display_final_states(self):
        afd_final_states = [state for state in self.afd.keys() if self.is_final_state(state)]
        return "Estados finales del AFD: " + ', '.join([','.join(state) for state in afd_final_states])

class AFNDToAFDApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor AFND a AFD 1152262 & 1152270")
        self.geometry("600x600")
        self.configure(bg="#333333")  # Fondo gris oscuro
        
        self.converter = AFNDtoAFDConverter()

        # Estilos
        style = ttk.Style()
        style.configure("TFrame", background="#333333", foreground="#ffffff")
        style.configure("TLabel", background="#333333", foreground="#ffffff")
        style.configure("TButton", background="#007acc", foreground="#ffffff", font=('Helvetica', 10, 'bold'))
        style.configure("TEntry", fieldbackground="#1e1e1e", foreground="#ffffff")
        
        # Input AFND Frame
        self.input_frame = ttk.LabelFrame(self, text="Definición del AFND", style="TFrame")
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.afnd_input = tk.Text(self.input_frame, height=10, width=50, bg="#1e1e1e", fg="#ffffff", insertbackground="white", highlightbackground="#007acc", highlightcolor="#007acc", highlightthickness=1)
        self.afnd_input.pack(padx=10, pady=5)

        self.initial_state_label = ttk.Label(self.input_frame, text="Estado inicial:", style="TLabel")
        self.initial_state_label.pack(padx=10, pady=5)
        self.initial_state_input = ttk.Entry(self.input_frame, style="TEntry")
        self.initial_state_input.pack(padx=10, pady=5)

        self.final_states_label = ttk.Label(self.input_frame, text="Estados finales (separados por coma):", style="TLabel")
        self.final_states_label.pack(padx=10, pady=5)
        self.final_states_input = ttk.Entry(self.input_frame, style="TEntry")
        self.final_states_input.pack(padx=10, pady=5)

        self.convert_button = ttk.Button(self.input_frame, text="Convertir", command=self.convert, style="TButton")
        self.convert_button.pack(padx=10, pady=10)

        # Output Frame
        self.output_frame = ttk.LabelFrame(self, text="Resultados de la Conversión", style="TFrame")
        self.output_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.output_text = tk.Text(self.output_frame, height=20, width=70, state="disabled", bg="#1e1e1e", fg="#ffffff", insertbackground="white", highlightbackground="#007acc", highlightcolor="#007acc", highlightthickness=1)
        self.output_text.pack(padx=10, pady=10)

    def convert(self):
        afnd_input = self.afnd_input.get("1.0", "end").strip()
        initial_state_input = self.initial_state_input.get().strip()
        final_states_input = self.final_states_input.get().strip()

        if not afnd_input or not initial_state_input or not final_states_input:
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos de entrada.")
            return

        self.converter.input_afnd(afnd_input, initial_state_input, final_states_input)
        self.converter.convert()

        step_by_step = self.converter.display_step_by_step_conversion()
        afd_result = self.converter.display_afd()
        final_states = self.converter.display_final_states()

        output = step_by_step + "\n" + afd_result + "\n" + final_states
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", output)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    app = AFNDToAFDApp()
    app.mainloop()
