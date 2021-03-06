from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class ReglaFalsa:
  f = Function('fx')

  def __init__(self, xi, xs, tol, iter, function):
    self.xi = float(xi)
    self.xs = float(xs)
    self.tol = float(tol)
    self.iter = float(iter)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fxi = f.subs(x, self.xi)
    fxs = f.subs(x, self.xs)
    if fxi == 0:
      return { 'result': f'{repr(self.xi)} es una raiz' }
    elif fxs == 0:
      return { 'result': f'{repr(self.xs)} es una raiz' }
    elif fxi * fxs < 0:
      xm = (self.xi - (fxi * (self.xi - self.xs))) / (fxi-fxs)
      fxm = f.subs(x, xm)
      i = 1
      error = self.tol + 1
      self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      while fxm != 0 and error > self.tol and i < self.iter:
        if fxi * fxm < 0:
          self.xs = xm
          fxs = f.subs(x, self.xi)
          self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
        else:
          self.xi = xm
          fxi = f.subs(x, self.xi)
        xaux = xm
        xm = (self.xi - (fxi * (self.xi - self.xs))) / (fxi-fxs)
        fxm = f.subs(x, xm)
        error = abs(xm - xaux)
        i += 1
        self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      if fxm == 0:
        return { 'result': f'{repr(xm)} es una raiz', 'iters': self.vector }
      elif error < self.tol:
        return { 'result': f'{repr(xm)} se aproxima a una raiz de la función con una tolerancia de: {self.tol}', 'iters': self.vector }
      else:
        return { 'result': 'Excedio el numero de iteraciones posibles', 'iters': self.vector }
    else:
      return { 'result': 'El intervalo no cumple con las condiciones para buscar una raíz' }