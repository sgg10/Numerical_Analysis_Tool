def conver_to_base_10(n, b):
  n = float(n)
  negativo = True if n < 0 else False
  if negativo:
    n = abs(n)
  [entero, decimal] = str(n).split('.')
  [entero, decimal] = [list(entero), list(decimal)]
  # Parte entera
  for i in range(len(entero)):
    entero[len(entero)-i-1] = int(entero[len(entero)-i-1]) * b**i
  # Parte Decimal
  for i in range(len(decimal)):
    decimal[i] = int(decimal[i]) * b**-(i+1)
  result = sum(entero) + sum(decimal)
  return result if not negativo else result * -1

def float_point_notation(n, b=10, exp=0):
  move = 0
  if '0.' == n[:2]:
    copyN = list(n[2:])
    while True:
      if copyN[move] == '0':
        move += 1
        continue
      break 
    for _ in range(move):
      copyN.pop(0)
    copyN = ''.join(copyN) 
    move *= -1
    n = f'0.{copyN}'
  else:
    move = len(list(n.split('.')[0]))
    n = '0.' + n.replace('.', '')
  return {
    'number': n,
    'base': f'{b}^{int(exp) + move}'
  }

def decimal_to_binary(n):
  negativo = True if float(n) < 0 else False
  if negativo:
    n = n.replace('-', '')
  [entero, decimal] = n.split('.')
  [entero, decimal] = [int(entero), decimal]
  # Parte entera
  b_entero = []
  while True:
    if entero == 0:
      break
    residuo = entero % 2
    entero = entero // 2
    b_entero.append(str(residuo))
  b_entero.reverse()
  b_entero = int(''.join(b_entero))
  # Parte decimal
  decimal = float(f'0.{decimal}')
  b_decimal = []
  resultados = []
  while True:
    result = decimal * 2
    decimal = result % 1
    b_decimal.append(str(int(result - decimal)))
    if decimal == 0 or result in resultados:
      break
    else:
      resultados.append(result)
    
  b_decimal = float(f"0.{''.join(b_decimal)}")
  return -(b_entero + b_decimal) if negativo else b_entero + b_decimal

