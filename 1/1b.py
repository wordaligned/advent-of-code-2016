data = 'R8, R4, R4, R8'
data = input()

instructions = data.split()

direction = 1j

def turn(LR, direction):
    return direction * {'L': 1j, 'R': -1j}[LR]

pos = 0
visited = {pos}

for step in instructions:
    lr = step[:1]
    dist = int(step[1:].rstrip(','))
    direction = turn(lr, direction)
    for d in range(dist):
        pos += direction
        if pos in visited:
            print(int(pos.real + pos.imag))
        visited.add(pos)
