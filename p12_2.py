from collections import Counter
edges = []

def exits(n: str) -> set[str]:
  return {e[1] for e in edges if e[0] == n}

def traverse(n: str, path: list[list[str]]) -> list[str]:
  paths = []
  if n == 'end':
    paths.append(','.join(path + [n]))
    return paths
  lower_path = [p for p in path if p.lower() == p]
  for e in exits(n):
    if e == 'start': continue
    c = dict(Counter(lower_path + [e, n]))
    exclusions = [v for v in c.values() if v > 1]
    if exclusions not in [[],[2]]: continue
    paths.extend(traverse(e, path + [n]))
  return paths

"""
  >>> do('''start-A
  ... start-b
  ... A-c
  ... A-b
  ... b-d
  ... A-end
  ... b-end''')
  """
def do(data: str) -> int:
  """
  >>> do('''dc-end
  ... HN-start
  ... start-kj
  ... dc-start
  ... dc-HN
  ... LN-dc
  ... HN-end
  ... kj-sa
  ... kj-HN
  ... kj-dc''')
  19 
  """
  for line in data.splitlines():
    edge = line.split('-')
    edges.append(edge)
    if not (edge[0] == 'start' or edge[1] == 'end'):
      edges.append(edge[::-1])

  paths = traverse('start', [])
  for p in sorted(paths):
    print(p)
  return len(paths)

if __name__ == "__main__":
  import doctest
  doctest.testmod()