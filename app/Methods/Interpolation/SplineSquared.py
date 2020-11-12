import numpy as np
from sympy import symbols, Function, Symbol, diff, solve
import math

functions = []
functionsValues = []
constants = []
constantsUseds = []
a1, a2, a3 = symbols('a1 a2 a3')
b1, b2, b3 = symbols('b1 b2 b3')
c1, c2, c3 = symbols('c1 c2 c3')
d1, d2, d3 = symbols('d1 d2 d3')
e1, e2, e3 = symbols('e1 e2 e3')
f1, f2, f3 = symbols('f1 f2 f3')
g1, g2, g3 = symbols('g1 g2 g3')
h1, h2, h3 = symbols('h1 h2 h3')
i1, i2, i3 = symbols('i1 i2 i3')
j1, j2, j3 = symbols('j1 j2 j3')
k1, k2, k3 = symbols('k1 k2 k3')
l1, l2, l3 = symbols('l1 l2 l3')
m1, m2, m3 = symbols('m1 m2 m3')
n1, n2, n3 = symbols('n1 n2 n3')
constants.append(a1)
constants.append(a2)
constants.append(a3)
constants.append(b1)
constants.append(b2)
constants.append(b3)
constants.append(c1)
constants.append(c2)
constants.append(c3)
constants.append(d1)
constants.append(d2)
constants.append(d3)
constants.append(e1)
constants.append(e2)
constants.append(e3)
constants.append(f1)
constants.append(f2)
constants.append(f3)
constants.append(g1)
constants.append(g2)
constants.append(g3)
constants.append(h1)
constants.append(h2)
constants.append(h3)
constants.append(i1)
constants.append(i2)
constants.append(i3)
constants.append(j1)
constants.append(j2)
constants.append(j3)
constants.append(k1)
constants.append(k2)
constants.append(k3)
constants.append(l1)
constants.append(l2)
constants.append(l3)
constants.append(m1)
constants.append(m2)
constants.append(m3)
constants.append(n1)
constants.append(n2)
constants.append(n3)
f = Function('f') #Define 'f'as a function
df = Function('df')
x = Symbol('x')
y = Symbol('y')
pointsXAxis = []
pointsYAxis = []
n = 0
points = []
dictionaryPoints = {}
intervales = []
constantValues = {}
def run(x_values, y_values):
  constantNum = 0
  n = len(x)
  for i in range(n):
    points.append([float(x_values[i]),float(y_values[i])])
  for i in range(1,n):
    intervales.append([points[i-1][0],points[i][0]])
  dictionaryPoints = dict(points)
  for i in intervales:
    f = constants[constantNum]*x**2 +constants[constantNum+1]*x +constants[constantNum+2]
    functions.append(f)
    f = constants[constantNum]*x**2 +constants[constantNum+1]*x +constants[constantNum+2]  - dictionaryPoints[i[0]]
    functionsValues.append(f.subs(x,i[0]))
    f = constants[constantNum]*x**2 +constants[constantNum+1]*x +constants[constantNum+2]  - dictionaryPoints[i[1]]
    functionsValues.append(f.subs(x,i[1]))
    constantsUseds.append(constants[constantNum])
    constantsUseds.append(constants[constantNum+1])
    constantsUseds.append(constants[constantNum+2])
    constantNum += 3
  for i in range(0,len(functions)-1,1):
    #print(diff(functions[i],x))
    #print(diff(functions[i+1],x))
    f = diff(functions[i],x).subs(x,intervales[i][1]) - diff(functions[i+1],x).subs(x,intervales[i+1][0])
    functionsValues.append(f)
  functionsValues.append(diff(functions[0],x,2).subs(x,intervales[0][0]))
  #for i in range(0,len(functionsValues)):
  #  print(str(i + 1)+") " +str(functionsValues[i]))
  solution = solve(functionsValues, constantsUseds)
  constantValues = dict(solution)
  counter = 0
  funcActual = 0
  valuesOfA = []
  for i in constantValues:
    counter += 1
    valuesOfA.append(constantValues[i])
    if counter%3 == 0:
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-1],valuesOfA[2])
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-2],valuesOfA[1])
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-3],valuesOfA[0])
      #print(str(functions[funcActual]) + "             " + str(intervales[funcActual][0]) + " <=  X <= " + str(intervales[funcActual][1]))
      valuesOfA = []
      funcActual += 1
  return { 'result': constantValues }

