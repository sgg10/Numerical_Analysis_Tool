"""
  El error absoluto establece la diferencia que existe entre el valor verdadero x y el valor aproximado x'
    ° Dependiendo del signo de E decimos que x' se subaproxima o se sobreaproxima a x
    ° El error absoluto posee las mismas unidades que el valor aproximado
    ° En un sentido practico, el error absoluto se usa para acotar el valor de x:
      x ϵ [ x' - E, x' + E] (Tambien se escribe x = x' +- E)
    ° Usualmente el error absoluto se expresa como E = 0.d1d2*10^-d
"""
def absolute_error(x, x1, interval = False):
  return x - x1

def limit_value_x(x, E):
  return [x - E, x + E]


"""
  El error relativo se define como e = E / x ó e' = E / x'
  ° El error relativo no posee unidades, por lo que es comín que se presente su valor en
    terminos de porcentaje e = (E / x) * 100%
  ° Usualmente el error se expresa como e = d1.d2*10^-k
"""
def relative_error(x, E):
  return E / x
