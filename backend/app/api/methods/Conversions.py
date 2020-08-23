def conver_to_base_10(n, b):
  [entero, decimal] = n.split('.')
  [entero, decimal] = [list(entero), list(decimal)]
  # Parte entera
  for i in range(len(entero)):
    entero[len(entero)-i-1] = int(entero[len(entero)-i-1]) * b**i
  for i in range(len(decimal)):
    decimal[i] = int(decimal[i]) * b**-(i+1)
  return sum(entero) + sum(decimal)
