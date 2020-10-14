from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class BusquedasIncrementales:
  f = Function('fx')
  def __init__(self, x0, delta, iteraciones, function):
    self.x0 = float(x0)
    self.delta = float(delta)
    self.iteracion = float(iteraciones)
    self.function = function

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fx0 = f.subs(x, self.x0)
    if fx0 == 0:
      return { 'result': f'{self.x0} es una raiz' }
    else:
      x1 = self.x0 + self.delta
      i = 1
      fx1 = f.subs(x, x1)
      while fx0*fx1 > 0 and i < self.iteracion:
        self.x0 = x1
        fx0 = fx1
        x1 = self.x0 + self.delta
        fx1 = f.subs(x, x1)
        i = i + 1
      if fx1 == 0:
        return { 'result': f'{x1} es una raiz' }
      elif fx0 * fx1 < 0:
        return { 'result': f'Hay una raiz entre {self.x0} y {x1}' }
      else:
        return { 'result': 'Excedio el numero de iteraciones posible' }
