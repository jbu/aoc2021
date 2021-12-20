from heapq import heapify, heappop, heappush
from math import inf, ceil

cave = []
height = width = 0

def peers(x:int, y:int) -> tuple[tuple[int, int]]:
  up = (x, y-1) if y > 0 else None
  down = (x, y+1) if y < height-1 else None
  left = (x-1, y) if x > 0 else None
  right = (x+1, y) if x < width-1 else None
  return tuple(p for p in (up, down, left, right) if p is not None)

def at(p: tuple[int,int]) -> int:
  x, y = p
  return cave[y][x]

def cave_expand(cave: list[list[int]]) -> list[list[int]]:
  # addoors = [[x for x in range(y, 5+y)] for y in range(0, 5)]
  r = [[0 for x in range(width * 5)] for y in range(height * 5)]
  w = len(cave[0])
  h = len(cave)
  for xw in range(5):
    for yh in range(5):
      for y in range(len(cave)):
        for x in range(len(cave[0])):
          c = cave[y][x]
          c = c + xw + yh
          r[y + (h*yh)][x + (w*xw)] = 1+(c-1) % 9
  return r

def do(data: str) -> int:
  global cave, width, height
  for line in data.splitlines():
    cave.append([int(l) for l in line])
  width = len(cave[0])
  height = len(cave)
  fullcave = cave_expand(cave)

  cave = fullcave
  height = len(cave)
  width = len(cave[0])
  predecessors = {(x, y): None for x in range(width) for y in range(height) if not (x == 0 and y == 0)}
  distances = {(x, y): inf for x in range(width) for y in range(height) if not (x == 0 and y == 0)}
  distances[(0,0)] = 0
  Q = []
  heapify(Q)
  heappush(Q, (0, (0,0)))

  while Q:
    u = heappop(Q)
    for v in peers(*u[1]):
      alt = u[0] + at(v)
      if alt < distances[v]:
        distances[v] = alt
        predecessors[v] = u[1]
        if v not in Q:
          heappush(Q, (alt, v))

  S = []
  u = (width-1, height-1)
  if u in predecessors:
    while u:
      S.append(u)
      if u == (0,0): break
      u = predecessors[u]
  return sum([at(p) for p in S]) - at((0,0))


if __name__ == "__main__":
  data = open('data_15.txt').read()
  print(do(data))