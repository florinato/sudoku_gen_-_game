import numpy 
import random

# Función que controla los índices i y n.
def cont():
       global i
       global n

       if n==0:
              i=i-1
              n=8
       else:
              n=n-1  

# Función que evalúa las reglas del Sudoku para la celda actual.         
def eval():
       global i
       global n

       b=1
       
       # Comprueba si el número b ya existe en la fila y columna actual.
       while b<10:
              c=0
              t=False
              # Comprobación en la fila.
              while c<n:        
                     if a[i][c]==b:
                            t=True
                     c=c+1         
              d=0  
              # Comprobación en la columna.            
              while d<i:               
                     if a[d][n]==b:
                            t=True              
                     d=d+1  
              e=0  
              # Comprobación en la diagonal principal si i=n.            
              if i==n:            
                     while e<i:
                            if a[e][e]==b:
                                   t=True              
                            e=e+1  
              f=0  
              # Comprobación en la diagonal secundaria si i=(8-n).
              if i==(8-n):
                     f=0
                     while f<i:
                            if a[f][(8-f)]==b:
                                   t=True              
                            f=f+1
              
              # Determina en qué subgrid de 3x3 se encuentra la celda actual.
              if i<3 and n<3:
                     j=0
                     k=0
              if i<3 and n>2 and n<6:
                     j=0
                     k=3
              if i<3 and n>5:
                     j=0
                     k=6
              if i>2 and i<6 and n<3:
                     j=3
                     k=0
              if i>2 and i<6 and n>2 and n<6: 
                     j=3
                     k=3 
              if i>2 and i<6 and n>5: 
                     j=3
                     k=6
              if i>5  and n<3: 
                     j=6
                     k=0
              if i>5 and  n>2 and n<6:  
                     j=6
                     k=3
              if i>5 and  n>5 :
                     j=6
                     k=6
              
              # Comprobación en el subgrid de 3x3.
              if t==False:
                     g=j       
                     while g<(j+3):         
                            h=k
                            while h<(k+3):
                                   if a[g][h]==b:
                                          t=True 
                                   h=h+1
                            g=g+1
              
              # Si el número b no existe en la fila, columna y subgrid, se coloca en la celda.
              if t==False:
                     a[i][n]=b
                     b=9
                     
              # Si el número b existe y es 9, se vacía la celda y se retrocede a la celda anterior.       
              if t==True and b==9:
                     a[i][n]=0
                     cont()
                     b=a[i][n]
                     a[i][n]=0
                     while b==9:
                            a[i][n]=0 
                            cont()
                            b=a[i][n]
                           
              b=b+1               
                            
# Inicializa una matriz de 9x9 con todos ceros, que será el tablero de Sudoku.
a=numpy.zeros((9,9),dtype=int)

global i
global n
z=[1,2,3,4,5,6,7,8,9]
# Llena la primera fila de la matriz con una permutación aleatoria de números del 1 al 9.
a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]=random.sample(z,9)


i=1
# Recorre el resto de las celdas en la matriz y llena cada celda con un número del 1 al 9 que cumpla las reglas del Sudoku.
while i<9:
       n=0
       while n<9:
              eval()

              n=n+1 
       i=i+1
       
# Imprime el tablero de Sudoku y lo guarda en un archivo de texto llamado 'test1.txt'.
print(a)

numpy.savetxt('test1.txt', a, fmt='%d')

