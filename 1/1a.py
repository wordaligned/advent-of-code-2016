data = 'R5, L5, R5, R3'
data = input()

instructions = data.split()

direction = 1j

def turn(LR, direction):
    return direction * {'L': 1j, 'R': -1j}[LR]

pos = 0

for step in instructions:
    lr = step[:1]
    dist = int(step[1:].rstrip(','))
    direction = turn(lr, direction)
    pos += direction * dist

print(int(pos.real + pos.imag))
