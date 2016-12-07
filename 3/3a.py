import sys

def triangle(sides):
    sides.sort()
    return sides[0] + sides[1] > sides[2]

def sides(line):
    return [int(w) for w in line.split()]

print(sum(triangle(sides(line)) for line in sys.stdin))
