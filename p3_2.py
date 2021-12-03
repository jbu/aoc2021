from typing import List
import numpy as np
from io import StringIO

def do(measures: List[str]) -> int:
  """
  >>> do(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"])
  230
  """
  i = 1 << len(measures[0])-1
  m = [int(i, 2) for i in measures]
  while i:
    a = [x for x in m if x & i]
    b = [x for x in m if not (x & i)]
    print('a', [x&i for x in m])
    print('b', [f"{(x&~(i-1)):b}" for x in m])
    print('c', [f"{x:b}" for x in a], [f"{(x|i):b}" for x in b])
    if len(a) > len(b):
      m = a
    else:
      m = b
    i = i >> 1

  print(f"{i:b}, {m}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()