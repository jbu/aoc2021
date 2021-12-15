from functools import reduce
from itertools import accumulate

points_map = {'(': 1 , '[': 2, '{': 3, '<': 4}
pairs = {"()", "<>", "{}", "[]"}

def do(data: str) -> int:
  """
  >>> do('''[({(<(())[]>[[{[]{<()<>>
  ... [(()[<>])]({[<{<<[]>>(
  ... {([(<{}[<>[]}>{[]{[(<()>
  ... (((({<>}<{<{<>}{[]{[]{}
  ... [[<[([]))<([[{}[[()]]]
  ... [{[{({}]{}}([{[{{{}}([]
  ... {<[[]]>}<{[{[{[]{()[[[]
  ... [<(<(<(<{}))><([]([]()
  ... <{([([[(<>()){}]>(<<{{
  ... <{([{{}}[<[[[<>{}]]]>[]]''')
  288957
  """

  points = []
  for line in data.splitlines():
    stack = []
    for l in line:
      match l:
        case '(' | '<' | '{' | '[': stack.append(l)
        case ')' | '>' | '}' | ']':
          t = stack.pop()
          if f"{t}{l}" not in pairs:
            stack = []
            break
    if stack:
      stack = [points_map[s] for s in stack[::-1]]
      points.append(reduce(lambda x, y: x*5 + y, stack, 0))
  return sorted(points)[int(len(points)/2)]


if __name__ == "__main__":
  import doctest
  doctest.testmod()