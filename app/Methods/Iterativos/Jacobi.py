class Jacobi:
  def __init__(self, n, A, b, x0, niter, tolerancia):
    self.n = int(n)
    self.A = A
    self.b = b
    self.x0 = x0
    self.niter = float(niter)
    self.tolerancia = float(tolerancia)
    self.vector = []

  def run(self):
    contador = 0
    dispersion = self.tolerancia + 1
    x1 = []
    #print("\nOrden de los datos: n, x1, x2, x3, ... xn, dispersion " )
    #print(str(contador) + "    " + str(self.x0) + "\n")
    self.vector.append([str(contador), str(self.x0), str(dispersion)])
    while dispersion > self.tolerancia and contador < self.niter:
      x1 = self.calcularNuevoJacobi(self.x0, self.n, self.b, self.A)
      dispersion = self.norma(x1, self.x0, self.n)
      self.x0 = x1
      contador += 1
      #print(str(contador) + "   " + str(self.x0) + "   " + str(dispersion) + "\n")
      self.vector.append([str(contador), str(self.x0), str(dispersion)])

    if dispersion < self.tolerancia:
      return(f'{x1} es una aproximación con una tolerancia: {self.tolerancia}')
    else:
      # return("Fracaso en " + str(self.niter) + " iteraciones")
      return(x1)


  def calcularNuevoJacobi(self, x0, n, b, A):
    x1 = []
    for i in range(n):
      suma = 0.0
      for j in range(n):
        if j != i:
          valor = x0.pop(j)
          x0.insert(j, valor)
          suma += A[i][j] * valor

      valor = b.pop(i)
      b.insert(i, valor)
      elemento = (valor - suma)/A[i][i]
      x1.append(elemento)
    return x1


  def norma(self, x1, x0, n):
    mayor = -1
    for i in range(n):
      valor0 = x0.pop(i)
      valor1 = x1.pop(i)
      x0.insert(i, valor0)
      x1.insert(i, valor1)
      if abs(valor1 - valor0) > mayor:
        mayor = abs(valor1 - valor0)/abs(valor1)
    return mayor
