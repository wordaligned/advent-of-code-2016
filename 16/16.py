seq, size = [int(c) for c in '10001001100000001'], 35651584

while len(seq) <= size:
    seq = seq + [0] + [not v for v in reversed(seq)]

seq = seq[:size]

while len(seq) % 2 == 0:
    seq = [a==b for a,b in zip(*[iter(seq)]*2)]

print(*[int(s) for s in seq], sep='')
