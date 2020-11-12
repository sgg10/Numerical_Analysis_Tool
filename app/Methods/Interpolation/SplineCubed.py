import numpy as np
from sympy import symbols, Function, Symbol, diff, solve
import math
functions = []
functionsValues = []
constants = []
constantsUseds = []
a1, a2, a3, a4 = symbols('a1 a2 a3 a4')
b1, b2, b3, b4 = symbols('b1 b2 b3 b4')
c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
d1, d2, d3, d4 = symbols('d1 d2 d3 d4')
e1, e2, e3, e4 = symbols('e1 e2 e3 e4')
f1, f2, f3, f4 = symbols('f1 f2 f3 f4')
g1, g2, g3, g4 = symbols('g1 g2 g3 g4')
h1, h2, h3, h4 = symbols('h1 h2 h3 h4')
i1, i2, i3, i4 = symbols('i1 i2 i3 i4')
j1, j2, j3, j4 = symbols('j1 j2 j3 j4')
k1, k2, k3, k4 = symbols('k1 k2 k3 k4')
l1, l2, l3, l4 = symbols('l1 l2 l3 l4')
m1, m2, m3, m4 = symbols('m1 m2 m3 m4')
n1, n2, n3, n4 = symbols('n1 n2 n3 n4')
constants.append(a1)
constants.append(a2)
constants.append(a3)
constants.append(a4)
constants.append(b1)
constants.append(b2)
constants.append(b3)
constants.append(b4)
constants.append(c1)
constants.append(c2)
constants.append(c3)
constants.append(c4)
constants.append(d1)
constants.append(d2)
constants.append(d3)
constants.append(d4)
constants.append(e1)
constants.append(e2)
constants.append(e3)
constants.append(e4)
constants.append(f1)
constants.append(f2)
constants.append(f3)
constants.append(f4)
constants.append(g1)
constants.append(g2)
constants.append(g3)
constants.append(g4)
constants.append(h1)
constants.append(h2)
constants.append(h3)
constants.append(h4)
constants.append(i1)
constants.append(i2)
constants.append(i3)
constants.append(i4)
constants.append(j1)
constants.append(j2)
constants.append(j3)
constants.append(j4)
constants.append(k1)
constants.append(k2)
constants.append(k3)
constants.append(k4)
constants.append(l1)
constants.append(l2)
constants.append(l3)
constants.append(l4)
constants.append(m1)
constants.append(m2)
constants.append(m3)
constants.append(m4)
constants.append(n1)
constants.append(n2)
constants.append(n3)
constants.append(n4)
f = Function('f') #Define the function 'f'
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
  n = len(x_values)
  for i in range(n):
    points.append([float(x_values[i]),float(y_values[i])])
  for i in range(1,n):
    intervales.append([points[i-1][0],points[i][0]])
  dictionaryPoints = dict(points)
  for i in intervales:
    f = constants[constantNum]*x**3 +constants[constantNum+1]*x**2 +constants[constantNum+2]*x + constants[constantNum+3] 
    functions.append(f)
    f = constants[constantNum]*x**3 +constants[constantNum+1]*x**2 +constants[constantNum+2]*x + constants[constantNum+3]   - dictionaryPoints[i[0]]
    functionsValues.append(f.subs(x,i[0]))
    f = constants[constantNum]*x**3 +constants[constantNum+1]*x**2 +constants[constantNum+2]*x + constants[constantNum+3]   - dictionaryPoints[i[1]]
    functionsValues.append(f.subs(x,i[1])) 
    constantsUseds.append(constants[constantNum])
    constantsUseds.append(constants[constantNum+1])
    constantsUseds.append(constants[constantNum+2])
    constantsUseds.append(constants[constantNum+3])
    constantNum += 4  
  for i in range(0,len(functions)-1,1):
    f = diff(functions[i],x).subs(x,intervales[i][1]) - diff(functions[i+1],x).subs(x,intervales[i+1][0])
    functionsValues.append(f)
  for i in range(0,len(functions)-1,1):
    f = diff(functions[i],x,2).subs(x,intervales[i][1]) - diff(functions[i+1],x,2).subs(x,intervales[i+1][0])
    functionsValues.append(f)
  functionsValues.append(diff(functions[0],x,2).subs(x,intervales[0][0]))
  functionsValues.append(diff(functions[len(functions)-1],x,2).subs(x,intervales[len(intervales)-1][1]))
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
    if counter%4 == 0:
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-1],valuesOfA[3])
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-2],valuesOfA[2])
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-3],valuesOfA[1])
      functions[funcActual] = functions[funcActual].subs(constantsUseds[counter-4],valuesOfA[0])
      #print(str(functions[funcActual]) + "             " + str(intervales[funcActual][0]) + " <=  X <= " + str(intervales[funcActual][1]))
      valuesOfA = []
      funcActual += 1
  return { 'result': constantValues }
