from numpy import *
from sympy import *

class EliminacionGaussiana:
  def __init__(self, n, A):
    self.n = int(n)
    self.A = A
    self.vector = []
    self.matrices = []
    self.objetivos = []
    self.multiplicadores = []

  def sustitucionRegresiva(self, A, n):
    x = [[0]] * n
    for i in range(n, 0, -1):
      sumatoria = 0
      for p in range(i+1, n+1, 1):
        sumatoria += A[i-1][p-1] * x[p-1]
      x[i-1] = (A[i-1][n] - sumatoria) / A[i-1][i-1]
    return x

  def run(self):
    A2 = self.A
    for i in range(1, self.n):
      self.objetivos.append(f'Etapa {i}. Objetivo: poner ceros bajo el elemento A {i}{i} = {A2[i-1][i-1]}')
      for j in range(i, self.n):
        multiplicador = float(A2[j][i-2] / A2[i-1][i-1])
        self.multiplicadores.append(f'M{j}{i} = {multiplicador}')
        for k in range(i, self.n+2):
          A2[j][k-1] = A2[i][k-1] - multiplicador * A2[i-1][k-1]
        self.matrices.append(str(A2))
    return { 'result': self.sustitucionRegresiva(A2, self.n) }
