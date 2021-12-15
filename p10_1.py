points_map = {')': 3 , ']': 57, '}': 1197, '>': 25137}
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
  26397
  """

  errors = []
  points = 0
  for line in data.splitlines():
    stack = []
    for l in line:
      match l:
        case '(' | '<' | '{' | '[': stack.append(l)
        case ')' | '>' | '}' | ']':
          t = stack.pop()
          if f"{t}{l}" not in pairs:
            errors.append(line)
            points += points_map[l]
  return points

if __name__ == "__main__":
  import doctest
  doctest.testmod()