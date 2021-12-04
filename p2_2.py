from typing import List

def do(instructions: List[str]) -> int:
  """
  >>> do(['forward 5','down 5','forward 8','up 3','down 8','forward 2'])
  900
  """
  h = 0
  d = 0
  a = 0
  for i in instructions:
    match i.split():
      case ["forward", x]:
        h = h + int(x)
        d = d + a * int(x)
      case ["up", x]:
        a = a - int(x)
      case ["down", x]:
        a = a + int(x)
  return d * h

if __name__ == "__main__":
    import doctest
    doctest.testmod()