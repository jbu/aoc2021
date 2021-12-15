from more_itertools import chunked

points: list[int] = []
width = 0

def coord(x: int, y: int) -> int:
  return y * width + x

def coords(p: int) -> tuple[int,int]:
  y = p//width
  x = p-(y*width)
  return x, y

def around(p: int) -> list[int]:
  x, y = coords(p)
  arounds = {coord(a, b) 
              for b in range(y-1, y+2) 
              for a in range(x-1, x+2) 
              if a >= 0 
              if b >= 0 
              if a < width 
              if b < len(points)//width}
  return arounds - {p}

def can_flash() -> set():
  x = {i for i in range(len(points)) if points[i] > 9}
  return x

def print_board(b, title="---"):
  print(title)
  for l in chunked(b, width):
    print(''.join(["{:3}".format(ll) for ll in l]))

def propigate_flashes():
  flashed = set()
  while can_flash() - flashed:
    for i in range(len(points)):
      if points[i] > 9 and i not in flashed:
        flashed.add(i)
        for a in around(i) - flashed:
          points[a] += 1
  return flashed

"""
11111
  ... 19991
  ... 19191
  ... 19991
  ... 11111''')"""
def do(data: str) -> int:
  """
  >>> do('''5483143223
  ... 2745854711
  ... 5264556173
  ... 6141336146
  ... 6357385478
  ... 4167524645
  ... 2176841721
  ... 6882881134
  ... 4846848554
  ... 5283751526''')
  195
  """
  global points, width
  width=10
  for i in range(100):
    x, y = coords(i)
    print(f"({x},{y}), ",end='', flush=True)
    if x == 9:
      print(flush=True)
  
  for line in data.splitlines():
    width = len(line) if width == 0 else width
    points += [int(l) for l in line]
  print_board(points, 'initial')
  for step in range(10000):
    points = [p + 1 for p in points]
    flashes = propigate_flashes()
    for f in flashes:
      points[f] = 0
    if len(set(points)) == 1:
      return step + 1

if __name__ == "__main__":
  import doctest
  doctest.testmod()