import hashlib
from itertools import product

code = 'hhhxzeay'

grid = [complex(*p) for p in product(range(4), repeat=2)]

def open(c):
    return c in 'bcdef'

def longest_path(start, end):
    explore, longest = [(start, '')], 0

    def add(p, route):
        if p in grid:
            explore.append((p, route))

    while explore:
        p, route = explore.pop()
        if p == end:
            longest = max(len(route), longest)
        else:
            digest = hashlib.md5((code + route).encode()).hexdigest()
            U, D, L, R = [open(c) for c in digest[:4]]
            if U: add(p - 1j, route + 'U')
            if D: add(p + 1j, route + 'D')
            if L: add(p - 1,  route + 'L')
            if R: add(p + 1,  route + 'R')

    return longest

print(longest_path(grid[0], grid[-1]))
