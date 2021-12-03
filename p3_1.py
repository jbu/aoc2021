from typing import List
import numpy as np
from io import StringIO

def do(measures: List[str]) -> int:
  """
  >>> do(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"])
  198
  """
  d = np.array(list(''.join(measures))).astype(int).reshape(len(measures), len(measures[0]))
  ɣ = int(''.join((np.mean(d, axis=0) > 0.5).astype(int).astype(str)), 2)
  ε = int(''.join((np.mean(d, axis=0) < 0.5).astype(int).astype(str)), 2)
  return ɣ * ε

if __name__ == "__main__":
    import doctest
    doctest.testmod()