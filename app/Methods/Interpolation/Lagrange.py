import numpy as np
from sympy import expand, Function
from sympy.parsing.sympy_parser import parse_expr
import math

class LagrangeInterpolation:
  def __init__(self, n, x, y):
    self.n = int(n)
    self.x = x
    self.y = y
    self.process = []

  def run(self):
    polynomial| = ""
    F = Function('F')
    G = Function('G')
    """
      Schematic Form of Lagrange polynomial
      P(X) = L0(X)F(X0) + L1(X)F(X1) + L2(X)F(X2) + ... + LN(X)F(XN)
    """
    for i in range(self.n):
      L = '('
      for j in range(self.n):
        if j != i:
          L += f'(x - {self.x[j]})' 
      L += ') / ('
      for j in range(self.n):
        if j != i:
          L += f'({self.x[i]} - {self.x[j]}'
      L += ')'
      L = L.replace(')(', ')*(')
      F = parse_expr(L)
      self.process.append(f'\n L{i} (x) = {L.replace("((", "(").replace("))", ")")} = {expand(F)}')
      if i == self.n - 1:
        polynomial| += f'({expand(F)})*{self.y[i]}'
      else:
        polynomial| += f'({expand(F)})*{self.y[i]} + '

    G = (f'P(x) = {expand(polynomial|)}')
    print(f'''polynomial| Lagrange Interpolating
      P(x) = {G}
    ''')
    return { 'result': G }