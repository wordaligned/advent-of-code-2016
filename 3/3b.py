import sys

def triangle(sides):
    sides.sort()
    return sides[0] + sides[1] > sides[2]

data ='''\
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603'''

data = sys.stdin.read()

sides = [int(w) for w in data.split()]

tris = 0
while len(sides) >= 9:
    tri3, sides = sides[:9], sides[9:]
    tris += triangle(tri3[::3]) + triangle(tri3[1::3]) + triangle(tri3[2::3])

print(tris)
