from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Newton:
  f = Function('fx')
  df = Function('dfx')
  #comment to try push

  def __init__(self, x0, tol, iter, function):
    self.x0 = float(x0)
    self.tol = float(tol)
    self.iter = float(iter)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    df = diff(f, x)
    fx = f.subs(x, self.x0)
    dfx = df.subs(x, self.x0)
    i = 0
    errorAbs = self.tol + 1
    self.vector.append([str(i), str(self.x0), str(fx), str(dfx), "0"])
    while fx != 0 and errorAbs > self.tol and dfx != 0 and i < self.iter:
      x1 = self.x0 - (fx/dfx)
      fx = f.subs(x, x1)
      dfx = df.subs(x, x1)
      errorAbs = (x1 - self.x0)
      errorRel = errorAbs / x1
      self.x0 = x1
      i += 1
      self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(errorRel)])
    if fx == 0:
      return { 'result': f'{self.x0} es una raiz', "iters": self.vector }
    elif errorAbs < self.tol:
      return { 'result': f'{self.x0} se aproxima a una raiz de la función, con una tolerancia de: {self.tol}', "iters": self.vector }
    elif dfx == 0:
      return { 'result': f'{self.x0} es una posible raiz multiple', "iters": self.vector }
    else:
      return  { 'result': 'Excedio el numero de iteraciones posibles', 'iters': self.vector }