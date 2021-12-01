from more_itertools import pairwise
from typing import List

def do(dlist: List[str]) -> int:
  """
  >>> do(['199','200','208','210','200','207','240','269','260','263'])
  7
  """
  depths = [int(d) for d in dlist]
  deltas = pairwise(depths)
  deltas = [int(i[0] < i[1]) for i in deltas]
  return sum(deltas)

if __name__ == "__main__":
    import doctest
    doctest.testmod()