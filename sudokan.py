""" sudokan refactorizado"""
import tkinter as tk
import numpy as np
import random


class SudokuGame:
    """Clase principal para el juego de Sudoku."""
    def __init__(self):
        """Inicializa el juego de Sudoku."""
        self.k = 0
        self.y = 0
        self.a = np.loadtxt('test1.txt', dtype=int)
        self.a1 = np.zeros((9, 9), dtype=int)
        self.a2 = np.zeros((9, 9), dtype=int)
        self.fill_initial_numbers()
        self.setup_ui()

    def fill_initial_numbers(self):
        """Llena el tablero con números iniciales aleatorios."""
        b = 0
        while b < 25:
            c = random.randint(0, 80)
            j, g = divmod(c, 9)
            if self.a1[g, j] == 0:
                self.a1[g, j] = self.a[g, j]
                self.a2[g, j] = self.a[g, j]
                b += 1

    def setup_ui(self):
        """
        Configura la interfaz de usuario para el juego de Sudoku.

        Este método inicializa la ventana principal de Tkinter, 
        coloca todos los elementos de la interfaz de usuario, 
        como botones y etiquetas, y establece su comportamiento.
        """

        self.raiz = tk.Tk()
        self.raiz.title("sudokan")
        self.raiz.geometry('380x540')
        bg = tk.PhotoImage(file="sudokumask.png")
        label1 = tk.Label(self.raiz, image=bg)
        label1.place(x=0, y=0)

        self.labels = {}
        for n in range(9):
            for m in range(9):
                i, z = (n * 40) + 15, (m * 40) + 15
                if self.a1[n, m] != 0:
                    self.labels[f"strg{str(n) + str(m)}"] = tk.Label(self.raiz, text=str(self.a1[n, m]), fg="#06b838", font=("Roboto Cn", 18), width=2)
                else:
                    self.labels[f"strg{str(n) + str(m)}"] = tk.Label(self.raiz, text="", fg="black", width=2, font=("Roboto Cn", 18))
                self.labels[f"strg{str(n) + str(m)}"].place(x=z - 1, y=i)
                
        # Marcado de las diagonales
        for n in range(9):
            self.labels[f"strg{str(n) + str(n)}"].config(background="#8cfffb")
            self.labels[f"strg{str(n) + str(8-n)}"].config(background="#8cfffb")

        self.limpieza()
        


        botons = ("1", 40, 380, "2", 80, 380, "3", 120, 380, "4", 40, 420, "5", 80, 420, "6", 120, 420, "7", 40, 460, "8", 80, 460, "9", 120, 460)
        for i in range(0, len(botons), 3):
            c, l, j = botons[i], botons[i + 1], botons[i + 2]
            tk.Button(self.raiz, text=c, width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda c=c: self.intronum(c)).place(x=l, y=j)

        tk.Button(self.raiz, text="<", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: self.cursor("<")).place(x=220, y=420)
        tk.Button(self.raiz, text=">", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: self.cursor(">")).place(x=300, y=420)
        tk.Button(self.raiz, text="^", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: self.cursor("^")).place(x=260, y=380)
        tk.Button(self.raiz, text="v", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: self.cursor("v")).place(x=260, y=460)
        self.botonc = tk.Button(self.raiz, text="C", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: self.borrar())
        self.botonc.place(x=260, y=420)

        self.raiz.mainloop()

    def limpieza(self):
        """Actualiza la interfaz de usuario basada en el estado del juego."""
        for ss in range(9):
            for sc in range(9):
                if self.a1[ss, sc] != 0:
                    self.labels[f"strg{str(ss) + str(sc)}"].config(fg="#06b838", background="white")
                else:
                    self.labels[f"strg{str(ss) + str(sc)}"].config(fg="black", background="white")
        self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="gold", width=2, font=("Roboto Cn", 18), bd=2)
        if self.a1[self.k, self.y] != 0:
            self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="#ff8f18", width=2, font=("Roboto Cn", 18), bd=2)
        for n in range(9):
            self.labels[f"strg{str(n) + str(n)}"].config(background="#8cfffb")
            self.labels[f"strg{str(n) + str(8-n)}"].config(background="#8cfffb")

    def evalsqr(self):
        """Evalúa si hay números duplicados en cada cuadro 3x3 del tablero."""
        cuadrados = (0, 3, 0, 3, 0, 3, 3, 6, 0, 3, 6, 9, 3, 6, 0, 3, 3, 6, 3, 6, 3, 6, 6, 9, 6, 9, 0, 3, 6, 9, 3, 6, 6, 9, 6, 9)
        cuadrados_iter = iter(cuadrados)
        t = False

        for _ in range(9):
            a = next(cuadrados_iter)
            b = next(cuadrados_iter)
            c = next(cuadrados_iter)
            d = next(cuadrados_iter)
            aux = ""

            for i in range(a, b):
                for n in range(c, d):
                    if self.a2[i][n] != 0:
                        if str(self.a2[i][n]) in aux:
                            t = True
                            for s in range(a, b):
                                for ss in range(c, d):
                                    self.labels[f"strg{str(s) + str(ss)}"].config(background="#ffce9e")
                        aux += str(self.a2[i][n])
        return t

    def eval(self):
        """
        Evalúa el estado actual del tablero de Sudoku para comprobar si hay algún conflicto.

        Esta función realiza varias comprobaciones:
        - Verifica si hay números repetidos en cada fila.
        - Verifica si hay números repetidos en cada columna.
        - Verifica si hay números repetidos en cada cuadrado de 3x3.
        - Verifica si hay números repetidos en ambas diagonales.

        Si se encuentra algún número repetido, se cambia el color de fondo de las celdas afectadas.

        El estado del botón 'C' también se actualiza según el resultado de la evaluación.

        Devuelve:
        t (bool): Verdadero si hay un conflicto, Falso en caso contrario.
        """
        t = False
        self.limpieza()
        t = self.evalsqr()
        for c in range(9):
            aux = ""
            for s in range(9):
                if self.a2[s][c] != 0:
                    if str(self.a2[s][c]) in aux:
                        t = True
                        for ss in range(9):
                            self.labels[f"strg{str(ss) + str(c)}"].config(background="#ffce9e")
                    aux += str(self.a2[s][c])

        for c in range(9):
            aux = ""
            for s in range(9):
                if self.a2[c][s] != 0:
                    if str(self.a2[c][s]) in aux:
                        t = True
                        for ss in range(9):
                            self.labels[f"strg{str(c) + str(ss)}"].config(background="#ffce9e")
                    aux += str(self.a2[c][s])

        aux = ""
        for e in range(9):
            if self.a2[e][e] != 0:
                if str(self.a2[e][e]) in aux:
                    t = True
                    for ss in range(9):
                        self.labels[f"strg{str(ss) + str(ss)}"].config(background="#ffce9e")
                aux += str(self.a2[e][e])

        aux = ""
        for e in range(9):
            if self.a2[e][8 - e] != 0:
                if str(self.a2[e][8 - e]) in aux:
                    t = True
                    for ss in range(9):
                        self.labels[f"strg{str(ss) + str(8 - ss)}"].config(background="#ffce9e")
                aux += str(self.a2[e][8 - e])

        if not t:
            self.botonc.config(background="silver")
        else:
            self.botonc.config(background="#f17176")

        return t


    def intronum(self, c):
        """Inserta un número en la posición actual del cursor."""
        if self.a1[self.k][self.y] == 0:
            self.a2[self.k][self.y] = c
            self.eval()
            self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="gold", text=c)
            np.savetxt('9x9.txt', self.a2, fmt='%d')


    def borrar(self):
        """Borra el número en la posición actual del cursor."""
        if self.a1[self.k][self.y] == 0:
            self.a2[self.k][self.y] = 0
            self.eval()
            self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="gold", text="")
        
        if self.a1[self.k][self.y] != 0:
            self.eval()
            self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="#ff8f18",
                                                                width=2, font=("Roboto Cn", 18), bd=2)


    def cursor(self, x):
        """Mueve el cursor en la dirección especificada."""
        if self.eval() == False:
            self.botonc.config(background="silver")
            if x == "^" and self.k > 0:
                if self.a1[self.k][self.y] != 0:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="green", background="white", font=("Roboto Cn", 18), width=2)
                else:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="black", background="white", width=2, font=("Roboto Cn", 18))
                self.k -= 1
            elif x == "v" and self.k < 8:
                if self.a1[self.k][self.y] != 0:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="green", background="white", font=("Roboto Cn", 18), width=2)
                else:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="black", background="white", width=2, font=("Roboto Cn", 18))
                self.k += 1
            elif x == ">" and self.y < 8:
                if self.a1[self.k][self.y] != 0:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="green", background="white", font=("Roboto Cn", 18), width=2)
                else:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="black", background="white", width=2, font=("Roboto Cn", 18))
                self.y += 1
            elif x == "<" and self.y > 0:
                if self.a1[self.k][self.y] != 0:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="green", background="white", font=("Roboto Cn", 18), width=2)
                else:
                    self.labels[f"strg{str(self.k) + str(self.y)}"].config(fg="black", background="white", width=2, font=("Roboto Cn", 18))
                self.y -= 1

        self.eval()
        self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="gold", width=2, font=("Roboto Cn", 18), bd=2)
        if self.a1[self.k][self.y] != 0:
            self.labels[f"strg{str(self.k) + str(self.y)}"].config(background="#fde186", width=2, font=("Roboto Cn", 18), bd=2)


if __name__ == "__main__":
    game = SudokuGame()
