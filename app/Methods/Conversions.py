def convert_to_base_10(n, b):
  n = float(n)
  negative = True if n < 0 else False
  if negative:
    n = abs(n)
  [integer, decimal] = str(n).split('.')
  [integer, decimal] = [list(integer), list(decimal)]
  # Parte entera
  for i in range(len(integer)):
    integer[len(integer)-i-1] = int(integer[len(integer)-i-1]) * b**i
  # Parte Decimal
  for i in range(len(decimal)):
    decimal[i] = int(decimal[i]) * b**-(i+1)
  result = sum(integer) + sum(decimal)
  return result if not negative else result * -1

def pointing_float_notation(n, b=10, exp=0):
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

def convert_decimal_to_binary(n):
  negative = True if float(n) < 0 else False
  if negative:
    n = n.replace('-', '')
  [integer, decimal] = n.split('.')
  [integer, decimal] = [int(integer), decimal]
  # Parte entera
  b_integer = []
  while True:
    if integer == 0:
      break
    remainder = integer % 2
    integer = integer // 2
    b_integer.append(str(remainder))
  b_integer.reverse()
  b_integer = int(''.join(b_integer))
  # Decimal Part
  decimal = float(f'0.{decimal}')
  b_decimal = []
  results = []
  while True:
    result = decimal * 2
    decimal = result % 1
    b_decimal.append(str(int(result - decimal)))
    if decimal == 0 or result in results:
      break
    else:
      results.append(result)
    
  b_decimal = float(f"0.{''.join(b_decimal)}")
  return -(b_integer + b_decimal) if negative else b_integer + b_decimal

