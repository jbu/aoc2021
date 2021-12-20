from collections import Counter
from more_itertools import pairwise
from math import ceil

def do(data: str) -> int:
  pair_insertions = []
  lines = data.splitlines()
  polymer_template = lines[0]
  for line in lines[2:]:
    pair_insertions.append(line.split(" -> "))
  pair_map = {tuple(kk for kk in k):v for k,v in pair_insertions}
  current_template = polymer_template
  pcounter = Counter(p for p in pairwise(current_template))
  for _ in range(1,41):
    next_gen = Counter()
    for pair, count in pcounter.most_common():
      sbst = pair_map[pair]
      next_gen = next_gen + Counter({(pair[0], sbst): count}) + Counter({(sbst, pair[1]): count})
    pcounter = next_gen

  a2 = 'NBCCNBBBCBHCB'
  a4 = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
  print(''.join(sorted(a4)), len(a4))

  ccounter = Counter()
  for p, cnt in pcounter.most_common():
    ccounter = ccounter + Counter({p[0]: cnt}) +  + Counter({p[1]: cnt})
  ccounter = Counter({k:ceil(v/2) for k, v in ccounter.most_common()})
  print(ccounter.total())
  commons = ccounter.most_common()
  return commons[0][1] - commons[-1][1]

if __name__ == "__main__":
  data = open('data_14.txt').read()
  print(do(data))