from typing import List, Callable
import operator

def skriffle(measures: List[str], 
             cmp_fn: Callable[[int, int], bool]) -> int:
  i = 1 << len(measures[0])-1
  m = [int(i, 2) for i in measures]
  while i and len(m) > 1:
    a = [x for x in m if x & i]
    b = [x for x in m if not (x & i)]
    m = a if cmp_fn(len(a), len(b)) else b
    i = i >> 1
  return m[0]

def do(measures: List[str]) -> int:
  """
  >>> do(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"])
  230
  """
  oxygen = skriffle(measures, operator.ge)
  co2 = skriffle(measures, operator.lt)
  return oxygen * co2

if __name__ == "__main__":
    import doctest
    doctest.testmod()