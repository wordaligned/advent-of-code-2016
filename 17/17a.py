import hashlib
from itertools import product

code = 'hhhxzeay'

grid = [complex(*p) for p in product(range(4), repeat=2)]

pos = grid[0]
end = grid[-1]

fringe = {(pos, '')}

def open(c):
    return c in 'bcdef'

def add(steps, p, route):
    if p in grid:
        steps.add((p, route))

while not any(p == end for p, _ in fringe):
    steps = set()
    for p, route in fringe:
        digest = hashlib.md5((code + route).encode()).hexdigest()
        U, D, L, R = [open(c) for c in digest[:4]]
        if U: add(steps, p - 1j, route + 'U')
        if D: add(steps, p + 1j, route + 'D')
        if L: add(steps, p - 1,  route + 'L')
        if R: add(steps, p + 1,  route + 'R')
    fringe = steps

print(next(route for p, route in fringe if p == end))
