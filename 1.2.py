from more_itertools import pairwise, triplewise

depths = open('data_1.txt').readlines()
depths = [int(d) for d in depths]
triples = [sum(d) for d in triplewise(depths)]
pairs = pairwise(triples)
pairs = [p[1] > p[0] for p in pairs]
print(sum(pairs))
