from itertools import permutations, repeat

digit_to_wires = {
  '0': {'a','b','c','e','f','g'},
  '1': {'c','f'},
  '2': {'a','c','d','e','g'},
  '3': {'a','c','d','f','g'},
  '4': {'b','c','d','f'},
  '5': {'a','b','d','f','g'},
  '6': {'a','b','d','e','f','g'},
  '7': {'a','c','f'},
  '8': {'a','b','c','d','e','f','g'},
  '9': {'a','b','c','d','f','g'}
}
wires_to_digit = {frozenset(v):k for k,v in digit_to_wires.items()}


all_wires = {chr(i) for i in range(ord('a'), ord('g') + 1)}
all_possible_wirings = [{(a,b) for a, b in zip(a,b)} for a, b in zip(repeat(sorted(list(all_wires))), permutations(all_wires))]

length_to_digit = {}
for k,v in digit_to_wires.items():
  vl = len(v)
  if vl in length_to_digit:
    length_to_digit[vl].add(k)
  else:
    length_to_digit[vl] = {k}

def constrain_on_evidence(possibilities: list[set], evidence: set[str]) -> dict[chr,set]:
  possible_digits = length_to_digit[len(evidence)] # it's one of these
  remaining_possibilities = []
  for possible_digit in possible_digits:
    possible_wires = digit_to_wires[possible_digit]
    attempts = []
    # generate options consistent with this evidence.
    for p in permutations(evidence):
      attempts.append({(p, w) for p, w in zip(possible_wires, p)})
    # remove possibilities that are not consistent with any of these options
    for attempt in attempts:
      for possibility in possibilities:
        if attempt <= possibility:
          remaining_possibilities.append(possibility)

  return remaining_possibilities


def do(data: str) -> int:
  """
  >>> do('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
  5353
  """
  total = 0
  for line in data.splitlines():
    possibilities = all_possible_wirings
    input, output = [d.split() for d in line.split('|')]
    for evidence in sorted(input + output, key=len):
      possibilities = constrain_on_evidence(possibilities, {e for e in evidence})
    # we now have a mapping from original -> messed up wires. Reverse so we can decode.
    decode_map = {v:k for k, v in possibilities[0]}
    numerals = []
    for digit in output:
      decoded_digits = frozenset({decode_map[d] for d in digit})
      d = wires_to_digit[decoded_digits]
      numerals.append(d)
    total += int(''.join(numerals))
  return total

if __name__ == "__main__":
  import doctest
  doctest.testmod()