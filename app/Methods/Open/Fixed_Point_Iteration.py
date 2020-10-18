from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Fixed_Point_Iteration:

  f = Function('fx')
  g = Function('gx')

  def __init__(self, xa, tolerance, iteration, f, g):
    self.xa = float(xa)
    self.tolerance = float(tolerance)
    self.iteration = float(iteration)
    self.f = f
    self.g = g
    self.vector = []

  def run(self):
    f = parse_expr(self.f)
    g = parse_expr(self.g)
    x = Symbol('x')
    fx = f.subs(x, self.xa)
    i = 0
    absolute_error = self.tolerance + 1
    self.vector.append([str(i), str(self.xa), str(fx), str(absolute_error)])
    while fx != 0 and absolute_error > self.tolerance and i < self.iteration:
      xn = g.subs(x, self.xa)
      xn = float(xn)
      fx = f.subs(x, xn)
      absolute_error = abs(xn - self.xa)
      self.xa = xn
      i += 1
      self.vector.append([str(i), str(xn), str(fx), str(absolute_error)])

    if fx == 0:
      return { 'result': f'{self.xa} is a root', "iterations": self.vector }
    elif absolute_error < self.tolerance:
      return { 'result': f'{self.xa} is an approximate root, with a tolerance of: {self.tolerance}', "iterations": self.vector }
    else:
      return  { 'result': 'No root found with the given parameters.' }
