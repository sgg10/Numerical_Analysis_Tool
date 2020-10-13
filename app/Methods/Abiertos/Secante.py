from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Secante:
  f = Function('fx')

  def __init__(self, x0, x1, tol, iter, function):
    self.x0 = float(x0)
    self.x1 = float(x1)
    self.tol = float(tol)
    self.ietr = float(iter)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fx0 = f.subs(x, self.x0)

    if fx0 == 0:
      return { 'result': f'{self.x0} es una raiz' }
    else:
      fx1 = f.subs(x, self.x1)
      i = 0
      errorAbs = self.tol + 1
      denominador = fx1 - fx0
      self.vector.append([str(i), str(self.x0), str(fx0), "0"])
      while fx1 != 0 and errorAbs > self.tol and denominador != 0 and i < self.ietr:
        x2 = (self.x1 - fx1 * (self.x1-self.x0)) / denominador
        errorAbs = abs(x2 - self.x1)
        errorRel = errorAbs / x2  
        self.x0 = self.x1
        self.x1  = x2
        fx1 = f.subs(x, self.x1)
        denominador = fx1 - fx0
        i += 1
        self.vector.append([str(i), str(self.x0), str(fx0), str(errorRel)])
      if fx1 == 0:
        return { 'result': f'{self.x1} es una raiz', "iters": self.vector }
      elif errorAbs < self.tol:
        return  { 'result': f'{self.x1} se aproxima a una raiz de la función, con una tolerancia de: {self.tol}', "iters": self.vector }
      elif denominador == 0:
        return { 'result': f'Hay una raiz multiple en {self.x1}', "iters": self.vector }
      else:
        return { 'result': 'Excedio el numero de iteraciones posibles', 'iters': self.vector }
