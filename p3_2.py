from typing import List
import bisect

def do(measures: List[str]) -> int:
  """
  >>> do(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"])
  230
  """
  i = 1 << len(measures[0])-1
  m = [int(i, 2) for i in measures]
  while i and len(m) > 1:
    a = [x for x in m if x & i]
    b = [x for x in m if not (x & i)]
    if len(a) >= len(b):
      m = a
    else:
      m = b
    i = i >> 1
  oxygen = m[0]

  i = 1 << len(measures[0])-1
  m = [int(i, 2) for i in measures]
  while i and len(m) > 1:
    a = [x for x in m if x & i]
    b = [x for x in m if not (x & i)]
    if len(a) < len(b):
      m = a
    else:
      m = b
    i = i >> 1
  co2 = m[0]
  return oxygen * co2


if __name__ == "__main__":
    import doctest
    doctest.testmod()