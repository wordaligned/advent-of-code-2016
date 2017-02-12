import sys
from itertools import permutations

def node(line):
    w = line.split()
    return int(w[2].strip('T')), int(w[3].strip('T'))

def viable(A, B):
    return A[0] > 0 and A[0] <= B[1]

nodes = [node(line) for line in sys.stdin]

print(sum(1 for A, B in permutations(nodes, 2)
          if viable(A, B)))
