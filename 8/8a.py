from collections import deque
import re
import sys

W, H = 7, 3

data = '''\
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1'''

data = sys.stdin.read()
W, H = 50, 6

screen = [0] * W*H

def rect(w, h):
    for y in range(h):
        screen[y*W:y*W + w] = [1]*w

def rotate(s, r):
    rc = deque(screen[s])
    rc.rotate(r)
    screen[s] = rc

def column(x, r):
    rotate(slice(x,-1,W), r)

def row(y, r):
    rotate(slice(y*W,(y+1)*W), r)

mrect=re.compile('(rect) (\d+)x(\d+)').match
mcol=re.compile('rotate (column) x=(\d+) by (\d+)').match
mrow=re.compile('rotate (row) y=(\d+) by (\d+)').match

for op in data.splitlines():
    m = mrect(op) or mcol(op) or mrow(op)
    f = {'rect': rect, 'column': column, 'row': row}[m.group(1)]
    f(int(m.group(2)), int(m.group(3)))
    print('\n'.join(
        ''.join('.#'[screen[v]] for v in range(p, p+W))
        for p in range(0, W*H, W)))
    print()

print(sum(screen))
