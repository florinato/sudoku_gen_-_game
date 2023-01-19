import numpy 
import random



def cont():
       global i
       global n

       if n==0:
              i=i-1
              n=8
       else:
              n=n-1  
       

def eval():
       global i
       global n

       b=1
       
       while b<10:
              c=0
              t=False
              while c<n:
                      
                     if a[i][c]==b:
                            t=True
                     c=c+1         
              d=0              
              while d<i:
                      
                     if a[d][n]==b:
                            t=True              
                     d=d+1  
              e=0  
              if i==n:            
              
                     while e<i:
                      
                            if a[e][e]==b:
                                   t=True              
                            e=e+1  
              f=0  
              if i==(8-n):
                     f=0
                     while f<i:
                      
                            if a[f][(8-f)]==b:
                                   t=True              
                            f=f+1
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
              
              if t==False:
                     g=j       
                     while g<(j+3):
                            
                            h=k
                            while h<(k+3):
                                   #print(h,g,k,j)
                                   if a[g][h]==b:
                                          t=True 
                                   h=h+1
                            g=g+1
              
              if t==False:
                     a[i][n]=b
                     
                     b=9
                     
                      
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
                            
              

a=numpy.zeros((9,9),dtype=int)
global i
global n
z=[1,2,3,4,5,6,7,8,9]
a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]=random.sample(z,9)



i=1

while i<9:
       n=0
       while n<9:
              eval()

              n=n+1 
       
     #  print (a)
      # print("             ")      
       i=i+1       
    
print (a)
numpy.savetxt('test1.txt', a, fmt='%d')
#a1 = numpy.loadtxt('test1.txt',dtype=int)
#print (a1==a)
