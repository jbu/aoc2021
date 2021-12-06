from operator import itemgetter
import itertools
import collections

def parse_input(s: str) -> list[list[list[int, int]]]:
    lines = s.splitlines()
    r = [[[int(i) for i in p[0].split(",")], [int(j) for j in p[1].split(",")]] for p in  [l.split(" -> ") for l in lines]]
    return r

def inclusive_range(a, b) -> list[int]:
  if a < b:
    return list(range(a, b+1))
  return list(range(b, a+1))

def do(data: str) -> int:
  lines = parse_input(data)
  map = collections.Counter()

  for line in lines:
    ((ax, ay), (bx, by)) = line
    if not (ax == bx or ay == by):
      continue
    hrange = itertools.repeat(ax) if ax == bx else inclusive_range(ax, bx)
    vrange = itertools.repeat(ay) if ay == by else inclusive_range(ay, by)
    map.update([z for z in zip(hrange, vrange)])

  total = len([v for v in map.values() if v > 1])
  return total
