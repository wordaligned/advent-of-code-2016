import sys
import a_star

data = sys.stdin.read()

maze = {(i,j): c
        for i, r in enumerate(data.splitlines())
        for j, c in enumerate(r)}

to_visit = set(maze.values()) & set('0123456789')
zero = next(v for v, c in maze.items() if c=='0')

def neighbours(x, y):
    return [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]

def moves(s):
    v, visited = s
    for w in neighbours(*v):
        c = maze.get(w, '#')
        if c != '#':
            yield w, visited | {c} & to_visit

def heuristic(s):
    _, visited = s
    return len(to_visit) - len(visited)

def heuristic_circuit(s):
    (x, y), visited = s
    return len(to_visit) - len(visited) + abs(x - zero[0]) + abs(y - zero[1])

start = zero, frozenset({'0'})

path = a_star.a_star(start, heuristic, moves)
print(len(path) - 1)

path = a_star.a_star(start, heuristic_circuit, moves)
print(len(path) - 1)
