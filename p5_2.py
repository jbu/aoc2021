from operator import itemgetter
import itertools
import collections

def parse_input(s: str) -> list[list[list[int, int]]]:
    lines = s.splitlines()
    r = [[[int(i) for i in p[0].split(",")], [int(j) for j in p[1].split(",")]] for p in  [l.split(" -> ") for l in lines]]
    return r

def inclusive_range(ax, ay, bx, by) -> list[tuple[int, int]]:
  if ax == bx:
    return zip(itertools.repeat(ax), range(min(ay, by), max(ay, by) + 1))
  if ay == by:
    return zip(range(min(ax, bx), max(ax, bx) + 1), itertools.repeat(ay))
  vr = range(ay, by+1) if ay < by else range(ay, by-1, -1)
  return zip(range(ax, bx+1), vr)


def do(data: str) -> int:
  lines = parse_input(data)
  map = collections.Counter()

  for line in lines:
    ((ax, ay), (bx, by)) = sorted(line, key=itemgetter(0))
    points = inclusive_range(ax, ay, bx, by)
    map.update(points)
  total = len([v for v in map.values() if v > 1])
  return total
