import importlib
import random

import numpy as np

import random_sudoku  # Este módulo, al importarse, genera la nueva plantilla en test1.txt


class SudokuLogic:
    def __init__(self, filename='test1.txt'):
        # Carga inicial (aunque se actualizará al iniciar un nuevo juego)
        self.a = np.loadtxt(filename, dtype=int)
        # Números fijos iniciales (proporcionados en cada partida)
        self.a1 = np.zeros((9, 9), dtype=int)
        # Números ingresados por el usuario durante la partida
        self.a2 = np.zeros((9, 9), dtype=int)

    def new_game(self, num_initial):
        """Inicia un nuevo juego generando una plantilla nueva y llenando el tablero inicial."""
        # Forzamos la recarga del módulo para que se ejecute su código y se actualice test1.txt
        importlib.reload(random_sudoku)
        # Recarga el archivo con la nueva plantilla
        self.a = np.loadtxt('test1.txt', dtype=int)
        # Reinicia los tableros de números fijos y jugados
        self.a1 = np.zeros((9, 9), dtype=int)
        self.a2 = np.zeros((9, 9), dtype=int)
        # Llena el tablero con 'num_initial' números fijos
        self.fill_initial_numbers(num_initial)

    def fill_initial_numbers(self, num_initial):
        """Llena el tablero con 'num_initial' números fijos aleatorios."""
        count = 0
        while count < num_initial:
            pos = random.randint(0, 80)
            i, j = divmod(pos, 9)
            if self.a1[i, j] == 0:
                self.a1[i, j] = self.a[i, j]
                self.a2[i, j] = self.a[i, j]
                count += 1


    def mark_duplicates(self, coords):
        """
        Revisa un conjunto de celdas (lista de tuplas) en busca de duplicados.
        Devuelve un flag indicando si se encontró duplicado y una lista con las celdas afectadas.
        """
        seen = {}
        duplicate_found = False
        duplicates = []
        for i, j in coords:
            val = self.a2[i, j]
            if val != 0:
                if val in seen:
                    seen[val].append((i, j))
                    duplicate_found = True
                else:
                    seen[val] = [(i, j)]
        for cells in seen.values():
            if len(cells) > 1:
                duplicates.extend(cells)
        return duplicate_found, duplicates

    def evaluate(self):
        """
        Evalúa duplicados en filas, columnas, cuadros 3x3 y diagonales.
        Devuelve un flag y la lista de celdas en conflicto.
        """
        duplicate_found = False
        error_cells = set()
        # Cuadros 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                coords = [(x, y) for x in range(i, i + 3) for y in range(j, j + 3)]
                found, dup = self.mark_duplicates(coords)
                if found:
                    duplicate_found = True
                    error_cells.update(dup)
        # Filas
        for i in range(9):
            coords = [(i, j) for j in range(9)]
            found, dup = self.mark_duplicates(coords)
            if found:
                duplicate_found = True
                error_cells.update(dup)
        # Columnas
        for j in range(9):
            coords = [(i, j) for i in range(9)]
            found, dup = self.mark_duplicates(coords)
            if found:
                duplicate_found = True
                error_cells.update(dup)
        # Diagonal principal
        coords = [(i, i) for i in range(9)]
        found, dup = self.mark_duplicates(coords)
        if found:
            duplicate_found = True
            error_cells.update(dup)
        # Diagonal secundaria
        coords = [(i, 8 - i) for i in range(9)]
        found, dup = self.mark_duplicates(coords)
        if found:
            duplicate_found = True
            error_cells.update(dup)
        return duplicate_found, list(error_cells)

    def insert_number(self, i, j, num):
        """Inserta el número en la posición (i, j) si no es un valor fijo."""
        if self.a1[i, j] == 0:
            self.a2[i, j] = int(num)

    def delete_number(self, i, j):
        """Borra el número en la posición (i, j) si no es un valor fijo."""
        if self.a1[i, j] == 0:
            self.a2[i, j] = 0

    def get_hint_cells(self):
        """
        Devuelve una lista de coordenadas donde el número ingresado no coincide con la solución.
        Estas celdas se pueden marcar para dar una pista.
        """
        hint_cells = []
        for i in range(9):
            for j in range(9):
                if self.a2[i, j] != 0 and self.a2[i, j] != self.a[i, j]:
                    hint_cells.append((i, j))
        return hint_cells