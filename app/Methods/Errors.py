"""
  Absolute Error shows us the difference between the true value x and the approximation x'
    ° Depending on the sign of E we say that x' is greater or lower approximation of x
    ° The absolute error uses the same units as the approximated value
    ° In a practical sense, absolute error is used to constrain the value of x:
      x ϵ [ x' - E, x' + E] (Also written like: x = x' +- E)
    ° Absolute Error is normally written in the form: E = 0.d1d2*10^-d
"""
def absolute_error(x, x1, interval = False):
  return x - x1

def limit_value_x(x, E):
  return [x - E, x + E]


"""
  Relative Error is defined by the following: e = E / x ó e' = E / x'
  ° Relative Error does not have a unit, which is why it is common to present it in
    terms of percentage e = (E / x) * 100%
  ° The error is usually written in the format: e = d1.d2*10^-k
"""
def relative_error(x, E):
  return E / x
