from sympy import Function, expand
from sympy.parsing.sympy_parser import parse_expr
import math

class InterpolacionNewton:
  def __init__(self, n, tabla):
    self.n = int(n)
    self.tabla = tabla

  def run(self):
    polinimio = f'P(X) = {self.tabla[0][1]}'
    F = Function('F')
    for j in range(2, self.n + 1):
      for i in range(j - 1, self.n):
        self.tabla[i][j] = (self.tabla[i][j-1] - self.tabla[i-1][j-1]) / (self.tabla[i][0] - self.tabla[i-j+1][0])
        if i == j:
          polinimio += f' + {self.tabla[i][j]}'
          for k in range(0, i):
            polinimio += f'(x - {self.tabla[k][0]})'
    F = parse_expr(polinimio.replace('P(X) = ', '').replace('(', '*('))
    return {
      'result': f'P(x) = {expand(F)}',
      'schematic_form': polinimio
    }