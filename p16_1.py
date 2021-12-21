from more_itertools import take
from typing import Iterable

def stake(n: int, i: Iterable) -> str:
  s = take(n, i)
  return ''.join(s)

def parse_packet(bits: list[str]) -> tuple[int, list, int, str]:
  version, bits = int(bits[:3], 2), bits[3:]
  typeid, bits = int(bits[:3], 2), bits[3:]
  print(version, typeid, bits)
  match typeid:
    case 4:
      literal = ''
      head, bits = bits[:5], bits[5:]
      while head[0] == '1':
        literal += head[1:]
        head, bits = bits[:5], bits[5:]
      literal += head[1:]
      print(literal, int(literal, 2), version, bits)
      return (4, [int(literal, 2)], version, bits)
    case _:
      length_type, bits = int(bits[:1], 2), bits[1:]
      vs = version
      match length_type:
        case 0:
          nb, bits = int(bits[:15],2), bits[15:]
          subp, bits = bits[:nb], bits[nb:]
          lts = []
          while subp:
            t, lt, v, subp = parse_packet(subp)
            vs += v
            lts.append(lt)
        case 1:
          nb, bits = int(bits[:11], 2), bits[11:]
          lts = []
          for _ in range(nb):
            t, lt, v, bits = parse_packet(bits)
            vs += v
            lts.append(lt)
      print(6, [lts], bits)
      return (6, [lts], vs, bits)

          
def do(data: str) -> int:
  bits = ''.join(["{:0=4b}".format(int(d, base=16)) for d in data])
  print(bits)
  # bits = (i for i in bits)
  _, _, v, _ = parse_packet(bits)
  print(v)
  return v
        


if __name__ == "__main__":
  data = 'D2FE28'
  data = '38006F45291200'
  data = 'EE00D40C823060'
  assert do('8A004A801A8002F478') == 16
  assert do('620080001611562C8802118E34') == 12
  assert do('C0015000016115A2E0802F182340') == 23
  assert do('A0016C880162017C3686B18A3D4780') == 31
  data = open('data_16.txt').read()
  print(do(data))