import re
import sys
from collections import namedtuple
from a_star import a_star

def ints(s):
    return list(map(int, re.findall(r'\d+', s)))

grid = {}
for line in sys.stdin:
    x, y, size, used, *_ = ints(line)
    grid[(x,y)] = size, used

data_pos = max(x for x, y in grid if y == 0), 0
empty_pos = next(p for p, (s, u) in grid.items() if u == 0)

State = namedtuple('State', 'data_pos empty_pos')

def heuristic(s):
    return sum(s.data_pos)

def moves(s):
    for step in ((1,0), (-1,0), (0,1), (0,-1)):
        p = s.empty_pos[0] + step[0], s.empty_pos[1] + step[1]
        if p in grid and grid[p][1] <= grid[s.empty_pos][0]:
            yield State(data_pos=s.empty_pos if p==s.data_pos else s.data_pos,
                        empty_pos=p)


start = State(data_pos, empty_pos)            
path = a_star(start, heuristic, moves)
print(len(path) - 1)
