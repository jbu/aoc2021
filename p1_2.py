from more_itertools import pairwise, triplewise
from typing import List

def do(dlist: List[str]) -> int:
  """
  >>> do(['199','200','208','210','200','207','240','269','260','263'])
  5
  """
  depths = [int(d) for d in dlist]
  triples = [sum(d) for d in triplewise(depths)]
  pairs = pairwise(triples)
  pairs_diff = [p[1] > p[0] for p in pairs]
  return sum(pairs_diff)

if __name__ == "__main__":
    import doctest
    doctest.testmod()