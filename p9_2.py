from collections import deque
from functools import reduce
from operator import mul


def depth_at(depthmap: list[str], dimensions: tuple[int,int], x:int, y:int) -> int:
  return(depthmap[y * dimensions[0] + x])

def peer_depths(depthmap: list[str], dimensions: tuple[int,int], x:int, y:int) -> set[int]:
  return {depth_at(depthmap, dimensions, *p) for p in peers(dimensions, x, y)}

def peers(dimensions: tuple[int,int], x:int, y:int) -> set[tuple[int,int]]:
  up = (x,y-1) if y > 0 else None
  down = (x,y+1) if y < dimensions[1]-1 else None
  left = (x-1,y) if x > 0 else None
  right = (x+1, y) if x < dimensions[0] -1 else None
  return {i for i in (up,down,left,right) if i is not None}

def is_minimum(depthmap: list[int], dimensions: tuple[int,int], x: int, y: int) -> bool:
  around = peer_depths(depthmap, dimensions, x, y)
  return depth_at(depthmap, dimensions, x, y) < min(around)

def do(data: str) -> int:
  """
  >>> do('''2199943210
  ... 3987894921
  ... 9856789892
  ... 8767896789
  ... 9899965678''')
  1134
  """
  depthmap = []
  dimensions = (0,0)
  for line in data.splitlines():
    dimensions = (len(line), dimensions[1]+1)
    depthmap += [int(l) for l in line]

  # for test in [(0,0), (1,1), (9,0), (9,4), (8,0)]:
  #   print(test,peers(depthmap, dimensions, *test))

  local_mins = [(x,y) for x in range(dimensions[0]) for y in range(dimensions[1]) if is_minimum(depthmap, dimensions, x,y)]
  print(local_mins)
  basins = []
  for local_min in local_mins:
    visited = set()
    to_visit = deque([local_min])
    while to_visit:
      v = to_visit.pop()
      prs = peers(dimensions, *v)
      prs = {p for p in prs if depth_at(depthmap, dimensions, *p) < 9}
      prs -= visited
      visited.add(v)
      to_visit.extend(prs)
    basins.append(visited)
  return reduce(mul, sorted([len(b) for b in basins])[-3:], 1)


if __name__ == "__main__":
  import doctest
  doctest.testmod()