import numpy as np
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Triangle sides
b = 7

#Equation of line AB: 1.73x-y=0
#Equation of line BC: 2.747x+y-19.23=0
arr1=np.array([1.73,-1,0])
arr2=np.array([2.747,1,-19.23])
q = (arr2[0]*arr1[2]-arr1[0]*arr2[2])/(arr1[0]*arr2[1]-arr2[0]*arr1[1])
p = (arr1[1]*arr2[2]-arr2[1]*arr1[2])/(arr1[0]*arr2[1]-arr2[0]*arr1[1])

#Coordinates of A

print(p,q)
#Triangle vertices
A = np.array([0,0])
B = np.array([p,q])
C = np.array([b,0])

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()