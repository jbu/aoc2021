def parse_input(s: str) -> list[int]:
    return [int(i) for i in s.split(',')]


def do(data: str) -> int:
  fish = parse_input(data)
  print(fish)
  for _ in range(18):
    n = [8] * len([f for f in fish if f == 0])
    fish = [6 if f == 0 else f-1 for f in fish] + n
  return len(fish)