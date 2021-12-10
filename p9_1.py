def point_at(strmap, dimensions, x, y) -> int:
  return(strmap[y * dimensions[0] + x])

def peers(depthmap: list[int], dimensions: tuple[int,int], x:int, y:int) -> list[int]:
  p = y * dimensions[0] + x
  up = depthmap[p - dimensions[0]] if y > 0 else None
  down = depthmap[p + dimensions[0]] if y < dimensions[1]-1 else None
  left = depthmap[p - 1] if x > 0 else None
  right = depthmap[p + 1] if x < dimensions[0]-1 else None
  return([i for i in (up,down,left,right) if i is not None])

def is_minimum(depthmap: list[int], dimensions: tuple[int,int], x: int, y: int) -> bool:
  around = peers(depthmap, dimensions, x, y)
  return point_at(depthmap, dimensions, x, y) < min(around)

def do(data: str) -> int:
  """
  >>> do('''2199943210
  ... 3987894921
  ... 9856789892
  ... 8767896789
  ... 9899965678''')
  15
  """
  depthmap = []
  dimensions = (0,0)
  for line in data.splitlines():
    dimensions = (len(line), dimensions[1]+1)
    depthmap += [int(l) for l in line]

  # for test in [(0,0), (1,1), (9,0), (9,4), (8,0)]:
  #   print(test,peers(depthmap, dimensions, *test))

  risk = 0
  mins = [(x,y) for x in range(dimensions[0]) for y in range(dimensions[1]) if is_minimum(depthmap, dimensions, x,y)]
  risk = sum(1 + point_at(depthmap, dimensions, x, y) for x,y in mins)
  return risk

if __name__ == "__main__":
  import doctest
  doctest.testmod()