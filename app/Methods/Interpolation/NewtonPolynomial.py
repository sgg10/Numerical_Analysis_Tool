from sympy import Function, expand
from sympy.parsing.sympy_parser import parse_expr
import math

class NewtonInterpolation:
  def __init__(self, n, table):
    self.n = int(n)
    self.table = table

  def run(self):
    polynomial = f'P(X) = {self.table[0][1]}'
    F = Function('F')
    for j in range(2, self.n + 1):
      for i in range(j - 1, self.n):
        self.table[i][j] = (self.table[i][j-1] - self.table[i-1][j-1]) / (self.table[i][0] - self.table[i-j+1][0])
        if i == j:
          polynomial += f' + {self.table[i][j]}'
          for k in range(0, i):
            polynomial += f'(x - {self.table[k][0]})'
    F = parse_expr(polynomial.replace('P(X) = ', '').replace('(', '*('))
    return {
      'result': f'P(x) = {expand(F)}',
      'schematic_form': polynomial
    }