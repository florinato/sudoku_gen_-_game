from tkinter import *
import numpy
import random
global k
global y
k=0
y=0
a = numpy.loadtxt('test1.txt', dtype=int)
a1=numpy.zeros((9,9),dtype=int)
a2=numpy.zeros((9,9),dtype=int)

def limpieza():
  for ss in range(0, 9):
    
    for sc in range(0, 9): 
      if a1[ss][sc]!=0:
        globals()[f"strg{str(ss)+str(sc)}"].config(fg="#06b838",background="white")
      else:
        globals()[f"strg{str(ss)+str(sc)}"].config(fg="black",background="white")

  globals()[f"strg{str(k)+str(y)}"].config(background="gold",
  width=2,font=("Roboto Cn",18),bd=2)
  if a1[k][y]!=0:
    globals()[f"strg{str(k)+str(y)}"].config(background="#ff8f18",
    width=2,font=("Roboto Cn",18),bd=2)
  for n in range(0, 9):
    globals()[f"strg{str(n)+str(n)}"].config(background="#8cfffb")
    globals()[f"strg{str(n)+str(8-n)}"].config(background="#8cfffb") 
 
      

def eval(): 
  t=False
  limpieza()
 
  t=evalsqr()
  for c in range(0, 9):
    aux=""
    for s in range(0, 9):
      if a2[s][c]!=0:

        if (str(a2[s][c]) in aux)==True:
          t=True
          
          for ss in range(0, 9):
            
              globals()[f"strg{str(ss)+str(c)}"].config(background="#ffce9e")
            
        aux=aux+(str(a2[s][c]))
  
  for c in range(0, 9):
    aux=""
    for s in range(0, 9):
      if a2[c][s]!=0:

        if (str(a2[c][s]) in aux)==True:
          t=True
          
          for ss in range(0, 9):
            
              globals()[f"strg{str(c)+str(ss)}"].config(background="#ffce9e")
            
        aux=aux+(str(a2[c][s]))
  aux=""
  for e in range(0, 9):
    
    if a2[e][e]!=0:

        if (str(a2[e][e]) in aux)==True:
          t=True
          
          for ss in range(0, 9):
            
              globals()[f"strg{str(ss)+str(ss)}"].config(background="#ffce9e")
            
        aux=aux+(str(a2[e][e]))
  aux=""
  for e in range(0, 9):
    
    if a2[e][(8-e)]!=0:

        if (str(a2[e][(8-e)]) in aux)==True:
          t=True
          
          for ss in range(0, 9):
            
              globals()[f"strg{str(ss)+str(8-ss)}"].config(background="#ffce9e")
           
        aux=aux+(str(a2[e][(8-e)]))
  
  
  if t==False:  
    botonc.config(background="silver") 
  else:
    botonc.config(background="#f17176")
  
  
  return(t)
  
  if t==False:
    limpieza()

def evalsqr():
  cuadrados=(0,3,0,3,0,3,3,6,0,3,6,9,3,6,0,3,3,6,3,6,3,6,6,9,6,9,0,3,6,9,3,6,6,9,6,9)
  cuadrados_iter=iter(cuadrados)
  t=False
  for l in range(0, 9):
    a=next(cuadrados_iter)
    b=next(cuadrados_iter)
    c=next(cuadrados_iter)
    d=next(cuadrados_iter)
    aux=""
    for i in range(a,b):
      for n in range(c,d):
        if a2[i][n]!=0:
          if (str(a2[i][n]) in aux)==True:
              t=True
              for s in range(a,b):
                for ss in range(c,d):
                    
                    globals()[f"strg{str(s)+str(ss)}"].config(background="#ffce9e")
                  
            
          aux=aux+(str(a2[i][n]))
  return(t)
  
   
      
      
        
      
          
          
       
 
  
  
def intronum(c):
 
  if a1[k][y]==0:
    a2[k][y]=c
    eval()
    globals()[f"strg{str(k)+str(y)}"].config(background="gold",text=c)
    numpy.savetxt('9x9.txt', a2, fmt='%d')
    
def borrar():
  if a1[k][y]==0:
    a2[k][y]=0
    eval()
    globals()[f"strg{str(k)+str(y)}"].config(background="gold",text="")
    
  if a1[k][y]!=0:
    eval()
    globals()[f"strg{str(k)+str(y)}"].config(background="#ff8f18",
    width=2,font=("Roboto Cn",18),bd=2)
    
      
      
  

  
def cursor(x):
  global k
  global y
 
  if eval()==False:
    botonc.config(background="silver")
    if x=="^"and k>0:
      if a1[k][y]!=0:
        globals()[f"strg{str(k)+str(y)}"].config(fg="green",background="white",font=("Roboto Cn",18),width=2)
      else:
        globals()[f"strg{str(k)+str(y)}"].config(fg="black",background="white",
        width=2,font=("Roboto Cn",18))
      k=k-1
    elif x=="v"and k<8:
      if a1[k][y]!=0:
        globals()[f"strg{str(k)+str(y)}"].config(fg="green",background="white",font=("Roboto Cn",18),width=2)
      else:
        globals()[f"strg{str(k)+str(y)}"].config(fg="black",background="white",
        width=2,font=("Roboto Cn",18))
      k=k+1

    elif x==">"and y<8:
      if a1[k][y]!=0:
        globals()[f"strg{str(k)+str(y)}"].config(fg="green",background="white",font=("Roboto Cn",18),width=2)
      else:
        globals()[f"strg{str(k)+str(y)}"].config(fg="black",background="white",
        width=2,font=("Roboto Cn",18))
      y=y+1
    elif x=="<"and y>0:
      if a1[k][y]!=0:
        globals()[f"strg{str(k)+str(y)}"].config(fg="green",background="white",font=("Roboto Cn",18),width=2)
      else:
        globals()[f"strg{str(k)+str(y)}"].config(fg="black",background="white",
        width=2,font=("Roboto Cn",18))
      y=y-1

  
  eval() 
  globals()[f"strg{str(k)+str(y)}"].config(background="gold",
    width=2,font=("Roboto Cn",18),bd=2)
  if a1[k][y]!=0:
    globals()[f"strg{str(k)+str(y)}"].config(background="#fde186",
    width=2,font=("Roboto Cn",18),bd=2)
  
 

 
  


        
b=0
while b<36:
  
  c=random.randint(0, 80)
  j= int(c/9)
  g=(c%9)
  if a1[g][j]==0:
    a1[g][j]=a[g][j]
    a2[g][j]=a[g][j]
    b=b+1
 



raiz=Tk()

raiz.title("                        sudokan")

raiz.geometry('380x540')
bg = PhotoImage(file = "sudokumask.png") 
label1 = Label( raiz, image = bg) 
label1.place(x = 0, y = 0) 



for n in range(0, 9):
  for m in range(0, 9):
    i=(n*40)+15
    z=(m*40)+15
    if a1[n][m]==0:
      globals()[f"strg{str(n)+str(m)}"]=Label(raiz,text="")
      globals()[f"strg{str(n)+str(m)}"].place(x=z-1 , y=i)
      globals()[f"strg{str(n)+str(m)}"].config(fg="black",
      width=2,font=("Roboto Cn",18))
    else:
      globals()[f"strg{str(n)+str(m)}"]=Label(raiz,text=str(a1[n][m]))
      globals()[f"strg{str(n)+str(m)}"].place(x=z-1 , y=i)
      globals()[f"strg{str(n)+str(m)}"].config(fg="#06b838",font=("Roboto Cn",18),width=2)


limpieza()
globals()[f"strg{str(0)+str(0)}"].config(background="gold",
    width=2,font=("Roboto Cn",18),bd=2)
if a1[k][y]!=0:
  globals()[f"strg{str(0)+str(0)}"].config(background="#ff8f18",
  width=2,font=("Roboto Cn",18),bd=2)

botones=("1",40,380,"2",80,380,"3",120,380,"4",40,420,"5",80,420,"6",120,420,"7",40,460,"8",80,460,"9",120,460)
botones_iter = iter(botones)
def botones():
    c=next(botones_iter)
    l=next(botones_iter)
    j=next(botones_iter)
    boton=Button(raiz,text=c,width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: intronum(c))
    boton.place(x=l,y=j)
    return(boton)

boton1=botones()
boton2=botones()
boton3=botones()
boton4=botones()
boton5=botones()
boton6=botones()
boton7=botones()
boton8=botones()
boton9=botones()
botonl=Button(raiz,text="<",width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: cursor("<"))
botonl.place(x=220 ,y=420)
botonr=Button(raiz,text=">",width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: cursor(">"))
botonr.place(x=300,y=420)
botonu=Button(raiz,text="^",width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: cursor("^"))
botonu.place(x=260,y=380)
botond=Button(raiz,text="v",width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: cursor("v"))
botond.place(x=260,y=460)
botonc=Button(raiz,text="C",width=2,bd=5,font=("Roboto Cn",18),background="silver",command=lambda: borrar())
botonc.place(x=260,y=420)

raiz.mainloop()

