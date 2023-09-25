import random
import numpy as np

class NewSudokuGeneratorWithDiagonals:
    """Clase para generar y resolver tableros de Sudoku con reglas adicionales para diagonales."""

    def __init__(self):
        """Inicializa un nuevo tablero de Sudoku con ceros."""
        self.board = np.zeros((9, 9), dtype=int)

    def is_valid(self, num, pos):
        """
        Verifica si un número se puede colocar en una posición específica.

        Args:
        - num (int): El número que se va a colocar.
        - pos (tuple): La posición en el tablero donde se colocará el número.

        Returns:
        - bool: True si el número se puede colocar, False de lo contrario.
        """
        # Verificar fila
        if num in self.board[pos[0]]:
            return False

        # Verificar columna
        if num in self.board[:, pos[1]]:
            return False

        # Verificar cuadrado 3x3
        x_start = (pos[1] // 3) * 3
        y_start = (pos[0] // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i + y_start][j + x_start] == num:
                    return False

        # Verificar diagonal principal
        if pos[0] == pos[1]:
            for i in range(0, 9):
                if self.board[i][i] == num:
                    return False

        # Verificar diagonal secundaria
        if pos[0] + pos[1] == 8:
            for i in range(0, 9):
                if self.board[i][8 - i] == num:
                    return False

        return True

    def solve(self):
        """
        Resuelve el tablero de Sudoku utilizando backtracking.

        Returns:
        - bool: True si el tablero se resuelve con éxito, False de lo contrario.
        """
        empty = np.where(self.board == 0)
        empty_positions = list(zip(empty[0], empty[1]))
        if len(empty_positions) == 0:
            return True
        row, col = empty_positions[0]
        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def generate_sudoku(self):
        """Genera un nuevo tablero de Sudoku resuelto."""
        self.board[0] = random.sample(range(1, 10), 9)
        self.solve()

    def save_to_file(self, file_path):
        """
        Guarda el tablero de Sudoku en un archivo de texto.

        Args:
        - file_path (str): La ruta del archivo donde se guardará el tablero.
        """
        np.savetxt(file_path, self.board, fmt='%d')

# Ejemplo de uso
new_sudoku_with_diagonals = NewSudokuGeneratorWithDiagonals()
new_sudoku_with_diagonals.generate_sudoku()
print(new_sudoku_with_diagonals.board)


file_path1 = 'test1.txt'
new_sudoku_with_diagonals.save_to_file(file_path1)





