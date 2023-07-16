from tkinter import *
import numpy
import random

# Variables globales
k = 0
y = 0
a = numpy.loadtxt('test1.txt', dtype=int)
a1 = numpy.zeros((9, 9), dtype=int)
a2 = numpy.zeros((9, 9), dtype=int)

def limpieza():
    """Limpia el tablero y restaura los colores de las celdas."""
    for ss in range(0, 9):
        for sc in range(0, 9):
            if a1[ss][sc] != 0:
                globals()[f"strg{str(ss) + str(sc)}"].config(fg="blue", background="white")
            else:
                globals()[f"strg{str(ss) + str(sc)}"].config(fg="black", background="white")

    globals()[f"strg{str(k) + str(y)}"].config(background="gold", width=2, font=("Roboto Cn", 18), bd=2)
    if a1[k][y] != 0:
        globals()[f"strg{str(k) + str(y)}"].config(background="#ff8f18", width=2, font=("Roboto Cn", 18), bd=2)

    for n in range(0, 9):
        globals()[f"strg{str(n) + str(n)}"].config(background="#8cfffb")
        globals()[f"strg{str(n) + str(8 - n)}"].config(background="#8cfffb") 

def evaluar_tablero():
    """Evalúa el tablero y verifica si hay números repetidos."""
    limpieza()
    verificar_cuadrados()
    verificar_filas()
    verificar_columnas()

def verificar_cuadrados():
    """Verifica si hay números repetidos en los cuadrados de 3x3."""
    t = False
    cuadrados = (0, 3, 0, 3, 0, 3, 3, 6, 0, 3, 6, 9, 3, 6, 0, 3, 3, 6, 3, 6, 3, 6, 6, 9, 6, 9, 0, 3, 6, 9, 3, 6, 6, 9, 6, 9)
    cuadrados_iter = iter(cuadrados)

    for l in range(0, 9):
        a = next(cuadrados_iter)
        b = next(cuadrados_iter)
        c = next(cuadrados_iter)
        d = next(cuadrados_iter)
        aux = ""

        for i in range(a, b):
            for n in range(c, d):
                if a2[i][n] != 0:
                    if str(a2[i][n]) in aux:
                        t = True
                        for s in range(a, b):
                            for ss in range(c, d):
                                globals()[f"strg{str(s) + str(ss)}"].config(background="#ffce9e")
                    aux += str(a2[i][n])

    return t

def verificar_filas():
    """Verifica si hay números repetidos en las filas."""
    t = False
    for c in range(0, 9):
        aux = ""
        for s in range(0, 9):
            if a2[s][c] != 0:
                if str(a2[s][c]) in aux:
                    t = True
                    for ss in range(0, 9):
                        globals()[f"strg{str(ss) + str(c)}"].config(background="#ffce9e")
                aux += str(a2[s][c])
    return t

def verificar_columnas():
    """Verifica si hay números repetidos en las columnas."""
    t = False
    for c in range(0, 9):
        aux = ""
        for s in range(0, 9):
            if a2[c][s] != 0:
                if str(a2[c][s]) in aux:
                    t = True
                    for ss in range(0, 9):
                        globals()[f"strg{str(c) + str(ss)}"].config(background="#ffce9e")
                aux += str(a2[c][s])
    return t

def insertar_numero(c):
    """Inserta un número en la celda actual y evalúa el tablero."""
    if a1[k][y] == 0:
        a2[k][y] = c
        evaluar_tablero()
        globals()[f"strg{str(k) + str(y)}"].config(background="gold", text=c, fg="black")
        numpy.savetxt('9x9.txt', a2, fmt='%d')

def borrar():
    """Borra el número de la celda actual y evalúa el tablero."""
    if a1[k][y] == 0:
        a2[k][y] = 0
        evaluar_tablero()
        globals()[f"strg{str(k) + str(y)}"].config(background="gold", text="")
  
    if a1[k][y] != 0:
        evaluar_tablero()
        globals()[f"strg{str(k) + str(y)}"].config(background="#ff8f18", width=2, font=("Roboto Cn", 18), bd=2)

def mover_cursor(direccion):
    """Mueve el cursor a la celda adyacente y evalúa el tablero."""
    global k, y

    evaluar_tablero()
    if direccion == "^" and k > 0:
        k -= 1
    elif direccion == "v" and k < 8:
        k += 1
    elif direccion == ">" and y < 8:
        y += 1
    elif direccion == "<" and y > 0:
        y -= 1

    evaluar_tablero()
    globals()[f"strg{str(k) + str(y)}"].config(background="gold", width=2, font=("Roboto Cn", 18), bd=2)
    if a1[k][y] != 0:
        globals()[f"strg{str(k) + str(y)}"].config(background="#fde186", width=2, font=("Roboto Cn", 18), bd=2)

def cargar_numeros_iniciales():
    """Carga los números iniciales en el tablero de forma aleatoria."""
    b = 0
    while b < 25:
        c = random.randint(0, 80)
        j = int(c / 9)
        g = c % 9
        if a1[g][j] == 0:
            a1[g][j] = a[g][j]
            a2[g][j] = a[g][j]
            b += 1

# Crear la ventana principal
raiz = Tk()
raiz.title("Sudokan")
raiz.geometry('380x540')
bg = PhotoImage(file="sudokumask.png")
label1 = Label(raiz, image=bg)
label1.place(x=0, y=0)

# Cargar números iniciales en el tablero
cargar_numeros_iniciales()

# Crear las etiquetas del tablero
for n in range(0, 9):
    for m in range(0, 9):
        i = (n * 40) + 15
        z = (m * 40) + 15
        if a1[n][m] == 0:
            globals()[f"strg{str(n) + str(m)}"] = Label(raiz, text="")
            globals()[f"strg{str(n) + str(m)}"].place(x=z-1, y=i)
            globals()[f"strg{str(n) + str(m)}"].config(fg="black", width=2, font=("Roboto Cn", 18))
        else:
            globals()[f"strg{str(n) + str(m)}"] = Label(raiz, text=str(a1[n][m]))
            globals()[f"strg{str(n) + str(m)}"].place(x=z-1, y=i)
            globals()[f"strg{str(n) + str(m)}"].config(fg="blue", font=("Roboto Cn", 18), width=2)

limpieza()
globals()[f"strg{str(0) + str(0)}"].config(background="gold", width=2, font=("Roboto Cn", 18), bd=2)
if a1[k][y] != 0:
    globals()[f"strg{str(0) + str(0)}"].config(background="#ff8f18", width=2, font=("Roboto Cn", 18), bd=2)

# Crear los botones del teclado numérico
botones = ("1", 40, 380, "2", 80, 380, "3", 120, 380, "4", 40, 420, "5", 80, 420, "6", 120, 420, "7", 40, 460, "8", 80, 460, "9", 120, 460)
botones_iter = iter(botones)
def crear_boton():
    c = next(botones_iter)
    l = next(botones_iter)
    j = next(botones_iter)
    boton = Button(raiz, text=c, width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: insertar_numero(c))
    boton.place(x=l, y=j)
    return boton

boton1 = crear_boton()
boton2 = crear_boton()
boton3 = crear_boton()
boton4 = crear_boton()
boton5 = crear_boton()
boton6 = crear_boton()
boton7 = crear_boton()
boton8 = crear_boton()
boton9 = crear_boton()

# Crear los botones de movimiento del cursor
botonl = Button(raiz, text="<", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: mover_cursor("<"))
botonl.place(x=220, y=420)
botonr = Button(raiz, text=">", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: mover_cursor(">"))
botonr.place(x=300, y=420)
botonu = Button(raiz, text="^", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: mover_cursor("^"))
botonu.place(x=260, y=380)
botond = Button(raiz, text="v", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: mover_cursor("v"))
botond.place(x=260, y=460)

# Crear el botón de borrado
botonc = Button(raiz, text="C", width=2, bd=5, font=("Roboto Cn", 18), background="silver", command=lambda: borrar())
botonc.place(x=260, y=420)

raiz.mainloop()

