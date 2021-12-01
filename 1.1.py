from more_itertools import pairwise

depths = open('data_1.txt').readlines()
depths = [int(d) for d in depths]
deltas = pairwise(depths)
deltas = [int(i[0] < i[1]) for i in deltas]
print(sum(deltas))
