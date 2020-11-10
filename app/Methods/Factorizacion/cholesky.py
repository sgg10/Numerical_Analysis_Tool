import numpy as np
from sympy import *
import math

L = []
U = []
Z = []
X = []

class Cholesky:
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
    return self.conversionL(self.A, L, U, self.B, self.n)

  def resolverMatriz(self, L,U,B,n):
    Y =  [0] * n
    X = [0] * n
    for p in range(n):
      for k in range(n):
        if k == 0 and p == 0:
          Ymn = B[k] / L[k][p]
          Y[k] = Ymn
        elif k == p:
          Ymn = B[k]
          for t in range(k):
              Ymn = Ymn - Y[t]*L[k][t]                 
          Ymn = Ymn / L[k][p]
          Y[k] = Ymn

    for p in range(n-1,-1,-1):
      for k in range(n-1,-1,-1):
        if k == 3 and p == 3:
          Xmn = Y[k] / U[k][p]
          X[k] = Xmn                
        elif k == p:
          Xmn = Y[k]
          for t in range(1,4):                    
            Xmn = Xmn - X[t]*U[k][t]               
          Xmn = Xmn / U[k][p]
          X[k] = Xmn
    return(X)

  def conversionL(self, A,L,U,B,n):
    for y in range(n):        
      for x in range(n):              
        if y == x:
          if y == 0:
            Lmn = float(math.sqrt(A[x][y]))
            L[x][y] = Lmn 
            U[x][y] = Lmn
          else:
            Umn = A[x][y]
            for t in range(y):
              Umn = Umn - L[x][t]*U[t][x]                        
            Umn = float(math.sqrt(Umn))
            L[x][y] = Umn
            U[x][y] = Umn

        elif x > y:
          if y == 0:
            Lxy = A[x][y] / Lmn
            L[x][y] = Lxy
          else:
            Lxy = A[x][y]
            for t in range(y):
              Lxy = Lxy - L[x][t]*U[t][y]
            Lxy = Lxy / U[y][y]
            L[x][y] = Lxy


        elif y > x:
          if x == 0:
            Uxy = A[x][y] / Lmn
            U[x][y] = Uxy
          else:
            Uxy = A[x][y]
            for t in range(y):
                Uxy = Uxy - L[x][t]*U[t][y]
            Uxy = Uxy / L[x][x]
            U[x][y] = Uxy         

    return self.resolverMatriz(L,U,B,n)
