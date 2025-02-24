import numpy
import random


a = numpy.loadtxt('test2.txt', dtype=str)
a1=numpy.zeros((9,9),dtype=int)
z=[1,2,3,4,5,6,7,8,9]
 

(an,b,c,d,e,f,g,h,ir)=random.sample(z,9)

i=0
while i<9:
	n=0
	while n<9:

		if a[i][n]== "A":
			a1[i][n]=an 
		elif a[i][n]== "B":
			a1[i][n]=b
		elif a[i][n]== "C":
			a1[i][n]=c
		elif a[i][n]== "D":
			a1[i][n]=d
		elif a[i][n]== "E":
			a1[i][n]=e
		elif a[i][n]== "F":
			a1[i][n]=f
		elif a[i][n]== "G":
			a1[i][n]=g
		elif a[i][n]== "H":
			a1[i][n]=h
		elif a[i][n]== "I":
			a1[i][n]=ir
		n=n+1
	i=i+1
numpy.savetxt('test1.txt', a1, fmt='%d')
print(a1)