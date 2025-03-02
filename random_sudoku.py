import random

import numpy as np


def load_random_template(filename="sudoku_templates.txt"):
    """
    Lee el archivo de plantillas y devuelve una plantilla elegida al azar.
    Se asume que cada plantilla está separada por dos saltos de línea.
    """
    with open(filename, "r") as f:
        content = f.read().strip()
    templates = content.split("\n\n")
    chosen = random.choice(templates)
    # Convierte la plantilla elegida en una matriz de letras (lista de listas)
    letter_grid = [list(line.strip()) for line in chosen.splitlines() if line.strip()]
    return letter_grid

def convert_template_to_grid(letter_grid):
    """
    Convierte la plantilla (matriz de letras) en una matriz numérica.
    Genera un mapeo aleatorio de letras ("A" a "I") a números (1 a 9).
    """
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    numeros = random.sample(range(1, 10), 9)
    mapping = dict(zip(letras, numeros))
    
    grid = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            char = letter_grid[i][j]
            if char == ".":
                grid[i, j] = 0
            else:
                grid[i, j] = mapping.get(char, 0)
    return grid

# Ejecución inmediata del proceso:
letter_grid = load_random_template("sudoku_templates.txt")
numeric_grid = convert_template_to_grid(letter_grid)
np.savetxt("test1.txt", numeric_grid, fmt="%d")

