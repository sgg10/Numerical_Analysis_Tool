class GaussSeidel:
  def __init__(self, n, A, b, x0, numIterations, tolerance):
    self.n = int(n)
    self.A = A
    self.b = b
    self.x0 = x0
    self.tolerance = float(tolerance)
    self.numIterations = float(numIterations)
    self.vector = []

  def calculateGaussSeidel(self, x0, n, b, A):
    x1 = []
    for i in range(n):
      total = 0
      for j in range(n):
        if j != i:
          value = x0.pop(j)
          x0.insert(j, value)
          total += A[i][j] * value
      value = b.pop(i)
      b.insert(i, value)
      element = (value - total) / A[i][i]
      x1.append(element)
      x0.pop(i)
      x0.insert(i, element)
    return x1

  def normMatrix(self, x1, x0, n):
    largest = -1
    for i in range(n):
      value0 = x0[i]
      value1 = x1[i]
      if abs(value1 - value0) > largest:
        largest = abs(value1 - value0)/abs(value1)
    return largest

  def run(self):
    counter = 0
    dispersion = self.tolerance + 1
    x1 = []
    self.vector.append([str(counter), str(self.x0), str(dispersion)])
    while counter < self.numIterations:
      x1 = self.calculateGaussSeidel(self.x0, self.n, self.b, self.A)
      dispersion = self.normMatrix(x1, self.x0, self.n)
      self.x0 = x1
      counter += 1
      self.vector.append([str(counter), str(self.x0), str(dispersion)])
    return (x1)