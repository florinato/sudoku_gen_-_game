import tkinter as tk

import numpy as np

from sudoku_game import SudokuLogic

# Constantes de estilo y configuración
FONT = ("Roboto Cn", 18)
COLORS = {
    "initial": "#06b838",        # Números fijos (iniciales)
    "default": "black",          # Color por defecto para números ingresados
    "highlight": "gold",         # Celda seleccionada (cursor)
    "cursor_initial": "#ff8f18", # Celda fija seleccionada
    "error": "#ffce9e",          # Fondo para errores (duplicados)
    "diagonal": "#8cfffb",       # Fondo para celdas en las diagonales
    "button": "silver",          # Color de los botones
}

class SudokuGUI:
    def __init__(self):
        self.logic = SudokuLogic('test1.txt')
        self.k = 0  # Fila actual del cursor
        self.y = 0  # Columna actual del cursor
        self.hint_flags = np.zeros((9, 9), dtype=bool)
        self.labels = {}  # Diccionario para almacenar los labels del grid
        self.setup_ui()

    # Métodos helper para acceder y actualizar labels
    def get_label_key(self, i, j):
        return f"strg{i}{j}"

    def update_label(self, i, j, **kwargs):
        key = self.get_label_key(i, j)
        self.labels[key].config(**kwargs)

    def reset_labels(self):
        """Actualiza el estilo de todos los labels según el estado actual del juego."""
        for i in range(9):
            for j in range(9):
                if self.hint_flags[i, j]:
                    self.update_label(i, j, background="white")
                elif self.logic.a1[i, j] != 0:
                    self.update_label(i, j, fg=COLORS["initial"], background="white")
                else:
                    self.update_label(i, j, fg=COLORS["default"], background="white")
        # Resalta la celda actual (cursor)
        self.update_label(self.k, self.y, background=COLORS["highlight"], bd=2, font=FONT)
        if self.logic.a1[self.k, self.y] != 0:
            self.update_label(self.k, self.y, background=COLORS["cursor_initial"], bd=2, font=FONT)
        # Marcar las diagonales
        for n in range(9):
            self.update_label(n, n, background=COLORS["diagonal"])
            self.update_label(n, 8 - n, background=COLORS["diagonal"])

    def new_game(self, num_initial):
        """Inicia un nuevo juego y actualiza la vista."""
        self.logic.new_game(num_initial)
        self.hint_flags = np.zeros((9, 9), dtype=bool)
        self.reset_labels()
        # Actualiza los labels con los números fijos
        for i in range(9):
            for j in range(9):
                if self.logic.a1[i, j] != 0:
                    self.update_label(i, j, text=str(self.logic.a1[i, j]), fg=COLORS["initial"])
                else:
                    self.update_label(i, j, text="")

    def setup_ui(self):
        """Configura la interfaz de usuario completa (ventana, grid, botones y menú)."""
        self.root = tk.Tk()
        self.root.title("sudokan")
        self.root.geometry('380x540')

        # Menú de dificultad
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        dificultad_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Dificultad", menu=dificultad_menu)
        dificultad_menu.add_command(label="Fácil", command=lambda: self.new_game(42))
        dificultad_menu.add_command(label="Medio", command=lambda: self.new_game(36))
        dificultad_menu.add_command(label="Difícil", command=lambda: self.new_game(30))
        dificultad_menu.add_command(label="Experto", command=lambda: self.new_game(24))
        dificultad_menu.add_command(label="Infernal", command=lambda: self.new_game(20))

        # Imagen de fondo
        bg = tk.PhotoImage(file="sudokumask.png")
        label_bg = tk.Label(self.root, image=bg)
        label_bg.place(x=0, y=0)
        label_bg.image = bg  # Conservar referencia

        # Creación del grid de labels
        for i in range(9):
            for j in range(9):
                x_pos = (j * 40) + 15
                y_pos = (i * 40) + 15
                key = self.get_label_key(i, j)
                if self.logic.a1[i, j] != 0:
                    self.labels[key] = tk.Label(self.root, text=str(self.logic.a1[i, j]),
                                                fg=COLORS["initial"], font=FONT, width=2)
                else:
                    self.labels[key] = tk.Label(self.root, text="",
                                                fg=COLORS["default"], font=FONT, width=2)
                self.labels[key].place(x=x_pos - 1, y=y_pos)

        # Marcar las diagonales
        for n in range(9):
            self.update_label(n, n, background=COLORS["diagonal"])
            self.update_label(n, 8 - n, background=COLORS["diagonal"])

        self.reset_labels()

        # Creación de botones numéricos
        botones = [
            {"text": "1", "x": 40, "y": 380},
            {"text": "2", "x": 80, "y": 380},
            {"text": "3", "x": 120, "y": 380},
            {"text": "4", "x": 40, "y": 420},
            {"text": "5", "x": 80, "y": 420},
            {"text": "6", "x": 120, "y": 420},
            {"text": "7", "x": 40, "y": 460},
            {"text": "8", "x": 80, "y": 460},
            {"text": "9", "x": 120, "y": 460},
        ]
        for btn in botones:
            tk.Button(self.root, text=btn["text"], width=2, bd=5, font=FONT,
                      background=COLORS["button"],
                      command=lambda c=btn["text"]: self.intronum(c)).place(x=btn["x"], y=btn["y"])

        # Botones de movimiento del cursor
        tk.Button(self.root, text="<", width=2, bd=5, font=FONT, background=COLORS["button"],
                  command=lambda: self.cursor("<")).place(x=220, y=420)
        tk.Button(self.root, text=">", width=2, bd=5, font=FONT, background=COLORS["button"],
                  command=lambda: self.cursor(">")).place(x=300, y=420)
        tk.Button(self.root, text="^", width=2, bd=5, font=FONT, background=COLORS["button"],
                  command=lambda: self.cursor("^")).place(x=260, y=380)
        tk.Button(self.root, text="v", width=2, bd=5, font=FONT, background=COLORS["button"],
                  command=lambda: self.cursor("v")).place(x=260, y=460)
        self.botonc = tk.Button(self.root, text="C", width=2, bd=5, font=FONT,
                                 background=COLORS["button"], command=self.borrar)
        self.botonc.place(x=260, y=420)

        # Botón de pista (Hint)
        self.hint_button = tk.Button(self.root, text="Hint", width=5, bd=5, font=FONT,
                                     background=COLORS["button"], command=self.give_hint)
        self.hint_button.place(x=150, y=500)

        self.root.mainloop()

    def give_hint(self):
        """Marca en rojo las celdas con números incorrectos (pistas)."""
        hint_cells = self.logic.get_hint_cells()
        for i, j in hint_cells:
            self.update_label(i, j, fg="red")
            self.hint_flags[i, j] = True

    def intronum(self, c):
        """Inserta el número en la celda actual (si no es un número fijo) y actualiza la vista."""
        if self.logic.a1[self.k, self.y] == 0:
            self.logic.insert_number(self.k, self.y, c)
            self.hint_flags[self.k, self.y] = False
            self.reset_labels()
            self.evaluate_and_update()
            self.update_label(self.k, self.y, background=COLORS["highlight"], text=c)
            if self.logic.a2[self.k, self.y] == self.logic.a[self.k, self.y]:
                if self.logic.a1[self.k, self.y] == 0:
                    self.update_label(self.k, self.y, fg=COLORS["default"])
                else:
                    self.update_label(self.k, self.y, fg=COLORS["initial"])
            np.savetxt('9x9.txt', self.logic.a2, fmt='%d')

    def borrar(self):
        """Borra el número en la celda actual (si no es un número fijo) y actualiza la vista."""
        if self.logic.a1[self.k, self.y] == 0:
            self.logic.delete_number(self.k, self.y)
            self.hint_flags[self.k, self.y] = False
            # Se realiza la limpieza inmediata de la interfaz
            self.reset_labels()
            self.evaluate_and_update()
            self.update_label(self.k, self.y, background=COLORS["highlight"], text="")
            self.update_label(self.k, self.y, fg=COLORS["default"])
        else:
            self.evaluate_and_update()
            self.update_label(self.k, self.y, background=COLORS["cursor_initial"], bd=2, font=FONT)

    def evaluate_and_update(self):
        """Ejecuta la evaluación lógica y actualiza las celdas en conflicto."""
        duplicate_found, error_cells = self.logic.evaluate()
        for i in range(9):
            for j in range(9):
                if (i, j) in error_cells:
                    self.update_label(i, j, background=COLORS["error"])
        self.botonc.config(background="#f17176" if duplicate_found else COLORS["button"])

    def cursor(self, direction):
        """Mueve el cursor en la dirección indicada y actualiza la vista."""
        moves = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
        if self.logic.a1[self.k, self.y] != 0:
            self.update_label(self.k, self.y, fg="green", background="white", font=FONT)
        else:
            self.update_label(self.k, self.y, fg=COLORS["default"], background="white", font=FONT)
        dx, dy = moves.get(direction, (0, 0))
        self.k = (self.k + dx) % 9
        self.y = (self.y + dy) % 9
        self.evaluate_and_update()
        #self.reset_labels()
        self.update_label(self.k, self.y, background=COLORS["highlight"], bd=2, font=FONT)
        if self.logic.a1[self.k, self.y] != 0:
            self.update_label(self.k, self.y, background="#fde186", bd=2, font=FONT)

if __name__ == "__main__":
    gui = SudokuGUI()
