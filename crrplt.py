import numpy

a = numpy.loadtxt('test1.txt', dtype=int)
a1=numpy.zeros((9,9),dtype=str)
i=0
while i<9:
	n=0
	while n<9:

		if a[i][n]== 1:
			a1[i][n]="A"
		elif a[i][n]== 2:
			a1[i][n]="B"
		elif a[i][n]== 3:
			a1[i][n]="C"
		elif a[i][n]== 4:
			a1[i][n]="D"
		elif a[i][n]== 5:
			a1[i][n]="E"
		elif a[i][n]== 6:
			a1[i][n]="F"
		elif a[i][n]== 7:
			a1[i][n]="G"
		elif a[i][n]== 8:
			a1[i][n]="H"
		elif a[i][n]== 9:
			a1[i][n]="I"
		n=n+1
	i=i+1

print(a)
print(a1)
numpy.savetxt('test2.txt', a1,'%s')
a2 = numpy.loadtxt('test2.txt', dtype=str)
print(a2)
 