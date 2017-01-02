FAVE = 1350

def dest(x, y):
    return x >= 0 and y >= 0 and bin(
        x*x + 3*x + 2*x*y + y + y*y + FAVE).count('1') % 2 == 0

visited = {(1,1)}
fringe = {(1,1)}

def step(x, y):
    return (p for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
            if p not in visited and dest(*p))

for _ in range(50):
    fringe = {v for f in fringe for v in step(*f)}
    visited |= fringe

print(len(visited))
