from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class PuntoFijo:

  f = Function('fx')
  g = Function('gx')

  def __init__(self, xa, tol, iter, f, g):
    self.xa = float(xa)
    self.tol = float(tol)
    self.iter = float(iter)
    self.f = f
    self.g = g
    self.vector = []

  def run(self):
    f = parse_expr(self.f)
    g = parse_expr(self.g)
    x = Symbol('x')
    fx = f.subs(x, self.xa)
    i = 0
    errorAbs = self.tol + 1
    self.vector.append([str(i), str(self.xa), str(fx), str(errorAbs)])
    while fx != 0 and errorAbs > self.tol and i < self.iter:
      xn = g.subs(x, self.xa)
      xn = float(xn)
      fx = f.subs(x, xn)
      errorAbs = abs(xn - self.xa)
      self.xa = xn
      i += 1
      self.vector.append([str(i), str(xn), str(fx), str(errorAbs)])

    if fx == 0:
      return { 'result': f'{self.xa} es una raiz', "iters": self.vector }
    elif errorAbs < self.tol:
      return { 'result': f'{self.xa} se aproxima a una raiz de la función, con una tolerancia de: {self.tol}', "iters": self.vector }
    else:
      return  { 'result': 'No hay raiz con estos parametros' }
