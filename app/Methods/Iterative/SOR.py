from numpy import *
from sympy import *
import math

class SOR:
  def __init__(self, n, A, b, x0, omega, numIterations, tolerance):
    self.n = int(n)
    self.A = A
    self.b = b
    self.x0 = x0
    self.omega = float(omega)
    self.numIterations = int(numIterations)
    self.tolerance = float(tolerance)

  def calculateNewJacobi(self, x0, n, b, A, omega):
    x1 = []
    for i in range(n):
      total = 0
      for j in range(n):
        if i != j:
          value = x0.pop(j)
          x0.insert(j, value)
          total += A[i][j] * value
        
        value = b[i]
        original = x0[i]
        element = (value - total) / A[i][i]
        r = omega * element + (1 - omega) * original
        x1.append(r)
    return x1

  def normEuclidean(self, x1, x0, n):
    totalSquared = 0
    for i in range(n):
      valor0 = x0[i]
      valor1 = x1[i]
      totalSquared += (valor1 - valor0)**2

    return sqrt(totalSquared)

  def run(self):
    cpointer = 0
    dispersion = self.tolerance + 1
    x1 = []
    print('Orden de los datos: n, x1, x2, x3, ... xn, dispersion')
    iteration = [{ 'cpointer': cpointer, 'x0': self.x0}]
    while dispersion > self.tolerance and cpointer < self.numIterations:
      x1 = self.calculateNewJacobi(self.x0, self.n, self.b, self.A, self.omega)
      dispersion = self.normEuclidean(x1, self.x0, self.n)
      self.x0 = x1
      cpointer += 1
      iteration.append({ 'cpointer': cpointer, 'x0': self.x0, 'dispersion': dispersion})
    if dispersion < self.tolerance:
      return { 'result': f'{x1} is an approximation with a tolerance of: {self.tolerance}', 'iteration': iteration }
    else:
      return { 'result': f'Failure at {self.numIterations} iterations', 'iteration: ': iteration }