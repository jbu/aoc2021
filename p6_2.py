from collections import Counter

def parse_input(s: str) -> list[int]:
    return [int(i) for i in s.split(',')]


def do(data: str) -> int:
  fish = {i:0 for i in range(9)}
  fish.update(dict(Counter(parse_input(data))))
  print(fish)
  # fish will be days: count
  for _ in range(256):  
    f0 = fish[0]
    fish = {f-1:n for f, n in fish.items() if f > 0}
    fish[6] += f0
    fish[8] = f0
  return sum(fish.values())