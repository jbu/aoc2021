edges = []

def exits(n: str) -> set[str]:
  return {e[1] for e in edges if e[0] == n}

def traverse(n: str, visited: set[str], path: list[list[str]]) -> list[list[str]]:
  paths = []
  if n == 'end':
    paths.append(path + [n])
    return paths
  if n.lower() == n:
    visited.add(n)
  for e in exits(n) - visited:
    paths.extend(traverse(e, visited.copy(), path + [n]))
  return paths

'''start-A
  ... start-b
  ... A-c
  ... A-b
  ... b-d
  ... A-end
  ... b-end'''



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

  paths = traverse('start', set(), [])
  for p in paths:
    print(p)
  return len(paths)

if __name__ == "__main__":
  import doctest
  doctest.testmod()