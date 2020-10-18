def base_rounding(n, figure):
  if '.' not in n:
    return f'{n}.{str(0)*int(figure)}'
  
  if len(list(n.split('.')[1])) < int(figure):
    sub = int(figure) - len(list(n.split('.')[1]))
    return f'{n}{str(0)*int(sub)}'

  if len(list(n.split('.')[1])) == int(figure):
    return n
  
  return False

def default_rounding(n, figure):
  result = base_rounding(n, figure)
  if not result:
    [integer, decimal] = n.split('.')
    result = f'{"".join(integer)}.{"".join(decimal[:int(figure)])}'
  return result

def excess_rounding(n, figure):
  result = base_rounding(n, figure)
  if not result:
    [integer, decimal] = n.split('.')
    decimal = list(decimal)[:int(figure)]
    decimal = ''.join(decimal)
    decimal = int(decimal) + 1
    result = f'{integer}.{decimal}'
  return result

def symmetrical_rounding_statistics(n, figure):
  result = base_rounding(n, figure)
  if not result:
    [integer, decimal] = n.split('.')
    decimal = list(decimal)[:int(figure)+1]
    up = True if decimal[-1] >= '5' else False
    decimal.pop()
    decimal = ''.join(decimal)
    decimal = int(decimal) + 1 if up else int(decimal)
    result = f'{integer}.{decimal}'
  return result

def symmetrical_rounding_distance(n, figure):
  result = base_rounding(n, figure)
  if not result:
    [integer, decimal] = n.split('.')
    decimal = list(decimal)[:int(figure)+2]
    up = False
    odd = False
    if decimal[-2] == '5':
      odd = True if int(decimal[-1]) % 2 != 0 else False
    else:
      up = True if int(decimal[-1]) > '5' else False
    decimal.pop()
    decimal.pop()
    decimal = ''.join(decimal)
    decimal = int(decimal) + 1 if up or odd else int(decimal)
    result = f'{integer}.{decimal}'
  return result