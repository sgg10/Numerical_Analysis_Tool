from numpy import *
from sympy import *

class Gaussian_Elimination_Total_Pivot:
  def __init__(self, n, A):
    self.n = int(n)
    self.A = A

  def total_pivot(self, A, n, k):
    largest = 0
    largest_in_row = k
    largest_in_column = k
    for r in range(k,n):
      for s in range(k,n):
        if abs(A[r][s]) > largest:
          largest = abs(A[r][s])
          largest_in_row = r
          largest_in_column = s
    if largest == 0:
      return ("The system does not have a unique solution.")
    else:
      if largest_in_row != k:
        A = self.interchange_rows(A,largest_in_row,k)
      if largest_in_column != k:
        A = self.interchange_columns(A,largest_in_column,k)
    return A

  def interchange_rows(self, A, largest_in_row, k):
    for i in range(len(A[0])):
      aux = A[k][i]
      A[k][i] = A[largest_in_row][i]
      A[largest_in_row][i] = aux
    return A

  def interchange_columns(self, A, largest_in_column, k):
    for i in range(len(A[0])-1):
      aux = A[i][k]
      A[i][k] = A[i][largest_in_column]
      A[i][largest_in_column] = aux
    return A

  def regressive_substitution(self, A, n):
    x = []
    for i in range(n):
      x.append([0])
    for i in range(n,0,-1):
      summation = 0
      for p in range(i+1, n+1, 1):
        summation += A[i-1][p-1]*x[p-1]
      x[i-1] = (A[i-1][n] - summation)/ A[i-1][i-1]
    return(x)

  def run(self):
    for k in range(1,self.n):  
      self.A = self.total_pivot(self.A,self.n,k-1)
      for i in range(k, self.n):
        multiplier = float(self.A[i][k-1]/self.A[k-1][k-1])
        for j in range(k,self.n+2):
          self.A[i][j-1] = self.A[i][j-1] - multiplier*self.A[k-1][j-1]
    return { 'result': self.regressive_substitution(self.A,self.n) }