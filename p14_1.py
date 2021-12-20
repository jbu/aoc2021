import numpy as np
from collections import Counter
from more_itertools import pairwise


def do(data: str) -> int:
  pair_insertions = []
  lines = data.splitlines()
  polymer_template = lines[0]
  for line in lines[2:]:
    pair_insertions.append(line.split(" -> "))
  pair_map = {k:v for k,v in pair_insertions}
  current_template = polymer_template
  for i in range(1,11):
    stepl = [current_template[0]]
    for p in [''.join(p) for p in pairwise(current_template)]:
      stepl.append(f"{pair_map[p]}{p[1]}")
    current_template = ''.join(stepl)
  c = Counter(current_template)
  commons = c.most_common()
  return commons[0][1] - commons[-1][1]

if __name__ == "__main__":
  data = open('data_14.txt').read()
  print(do(data))