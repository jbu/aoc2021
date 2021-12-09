def do(data: str) -> int:
  """
  >>> do('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe')
  2
  """
  total_d = 0
  digits = {
    '0': ('a','b','c','e','f','g'),
    '1': ('c','f'),
    '2': ('a','c','d','e','g'),
    '3': ('a','c','d','f','g'),
    '4': ('b','c','d','f'),
    '5': ('a','b','d','f','g'),
    '6': ('a','b','d','e','f','g'),
    '7': ('a','c','f'),
    '8': ('a','b','c','d','e','f','g'),
    '9': ('a','b','c','d','f','g')
  }
  for line in data.splitlines():
    inp, outp = [d.split() for d in line.split('|')]
    l = [(i, len(i)) for i in outp if len(i) in [len(digits[d]) for d in ['1', '4', '7', '8']]]
    total_d += len(l)
  return total_d


if __name__ == "__main__":
  import doctest
  doctest.testmod()