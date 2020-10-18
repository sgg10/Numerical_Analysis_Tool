from numpy import *
from sympy import *

class Gaussian_Elimination:
  def __init__(self, n, A):
    self.n = int(n)
    self.A = A
    self.vector = []
    self.matrices = []
    self.objectives = []
    self.multiplier = []

  def regressive_substitution(self, A, n):
    x = [[0]] * n
    for i in range(n, 0, -1):
      summation = 0
      for p in range(i+1, n+1, 1):
        summation += A[i-1][p-1] * x[p-1]
      x[i-1] = (A[i-1][n] - summation) / A[i-1][i-1]
    return x

  def run(self):
    A2 = self.A
    for i in range(1, self.n):
      self.objectives.append(f'Step {i}. Objective: entire column under element A are zeros {i}{i} = {A2[i-1][i-1]}')
      for j in range(i, self.n):
        multiplier = float(A2[j][i-2] / A2[i-1][i-1])
        self.multiplier.append(f'M{j}{i} = {multiplier}')
        for k in range(i, self.n+2):
          A2[j][k-1] = A2[i][k-1] - multiplier * A2[i-1][k-1]
        self.matrices.append(str(A2))
    return { 'result': self.regressive_substitution(A2, self.n) }
