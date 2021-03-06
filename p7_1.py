def parse_input(s: str) -> list[int]:
    return [int(i) for i in s.split(',')]


def do(data: str) -> int:
  """
  >>> do('16,1,2,0,4,2,7,1,2,14')
  37
  """
  positions = parse_input(data)
  fuels = []
  for i in range(min(positions), max(positions) + 1):
      f = sum([abs(p-i) for p in positions])
      fuels.append(f)
  return min(fuels)

if __name__ == "__main__":
  import doctest
  doctest.testmod()