from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class FixedPointIteration:

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
    absoluteError = self.tolerance + 1
    self.vector.append([str(i), str(self.xa), str(fx), str(absoluteError)])
    while fx != 0 and absoluteError > self.tolerance and i < self.iteration:
      xn = g.subs(x, self.xa)
      xn = float(xn)
      fx = f.subs(x, xn)
      absoluteError = abs(xn - self.xa)
      self.xa = xn
      i += 1
      self.vector.append([str(i), str(xn), str(fx), str(absoluteError)])

    if fx == 0:
      return { 'result': f'{self.xa} is a root', "iterations": self.vector }
    elif absoluteError < self.tolerance:
      return { 'result': f'{self.xa} is an approximate root, with a tolerance of: {self.tolerance}', "iterations": self.vector }
    else:
      return  { 'result': 'No root found with the given parameters.' }
