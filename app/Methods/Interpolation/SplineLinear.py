class SplineLinear:
  def __init__(self, n, x, y):
    self.n = int(n)
    self.x = x
    self.y = y

  def run(self):
    resultArray = []
    for i in range(1, self.n):
      slope = (self.y[i] - self.y[i-1]) / (self.x[i] - self.x[i-1])
      resultFunction = (slope * -self.x[i]) + self.y[i]
      resultArray.append(f'P(X{i}) = {slope}X + {resultFunction}    {self.x[i-1]} <= X <= {self.x[i]}')
    return { 'resultArray': resultArray }