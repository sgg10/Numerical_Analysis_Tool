from numpy import *
from sympy import *
import math
import numpy as np
L = []
U = []
Z = []
X = []
class Dolittle:
  def __init__(self, n, A, B):
    X.clear()
    U.clear()
    Z.clear()
    L.clear()

    self.n = int(n)
    self.A = A
    self.B = B

  def run(self):
    L = np.zeros([self.n, self.n])
    U = np.zeros([self.n, self.n])
    for i in range(self.n):      #Initial values for the diagonal L are 1's
      L[i][i] = 1
    for k in range(self.n):      #Operation to calculate the L and U matrices correspondent to A
      for j in range(k,self.n):
        sum = 0
        for p in range(k):
          sum += L[k][p]*U[p][j]
        U[k][j] = (self.A[k][j] - sum)/L[k][k]
      for i in range(k,self.n):
        sum = 0
        for p in range(k):
          sum += L[i][p]*U[p][k]
        L[i][k] = (self.A[i][k] - sum)/U[k][k]
    #------Calculate Lz = B ----------#
    for i in range(self.n):
      sum = 0
      for j in range(i):
        sum += L[i][j]*Z[j]
      Z.append(self.B[i]-sum)

#------------Calculate Ux=Z----------------------#
    for i in range(self.n):
      X.append(0)
    for i in range(self.n-1,0-1,-1):
      sum = 0
      for j in range(i,self.n):
        sum += U[i][j]*X[j]
      X[i] = ((Z[i]-sum)/U[i][i])
    return(X)
