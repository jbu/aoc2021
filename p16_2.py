from more_itertools import take
from typing import Iterable
from operator import mul
from functools import reduce

def stake(n: int, i: Iterable) -> str:
  s = take(n, i)
  return ''.join(s)

def parse_packet(bits: list[str]) -> tuple[list, int, str]:
  version, bits = int(bits[:3], 2), bits[3:]
  typeid, bits = int(bits[:3], 2), bits[3:]
  print(version, typeid, bits)
  if typeid == 4:
    literal = ''
    head, bits = bits[:5], bits[5:]
    while head[0] == '1':
      literal += head[1:]
      head, bits = bits[:5], bits[5:]
    literal += head[1:]
    return (int(literal, 2), version, bits)

  length_type, bits = int(bits[:1], 2), bits[1:]
  vs = version
  match length_type:
    case 0:
      nb, bits = int(bits[:15],2), bits[15:]
      subp, bits = bits[:nb], bits[nb:]
      lts = []
      while subp:
        lt, v, subp = parse_packet(subp)
        vs += v
        lts.append(lt)
    case 1:
      nb, bits = int(bits[:11], 2), bits[11:]
      lts = []
      for _ in range(nb):
        lt, v, bits = parse_packet(bits)
        vs += v
        lts.append(lt)
  match typeid:
    case 0: return (sum(lts), v, bits)
    case 1: return (reduce(mul, lts, 1), v, bits)
    case 2: return (min(lts), v, bits)
    case 3: return (max(lts), v, bits)
    case 5: return (int(lts[0] > lts[1]), v, bits)
    case 6: return (int(lts[0] < lts[1]), v, bits)
    case 7: return (int(lts[0] == lts[1]), v, bits)

          
def do(data: str) -> int:
  bits = ''.join(["{:0=4b}".format(int(d, base=16)) for d in data])
  print(bits)
  # bits = (i for i in bits)
  a, v, b = parse_packet(bits)
  return a
        


if __name__ == "__main__":
  assert do('C200B40A82') == 3
  assert do('04005AC33890') == 54
  assert do('880086C3E88112') == 7
  assert do('CE00C43D881120') == 9
  assert do('D8005AC2A8F0') == 1
  assert do('F600BC2D8F') == 0
  assert do('9C005AC2F8F0') == 0
  assert do('9C0141080250320F1802104A08') == 1

  data = open('data_16.txt').read()
  print(do(data))