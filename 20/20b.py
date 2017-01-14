import sys

data = '''\
5-8
0-2
4-7
'''

data = sys.stdin.read()

def range(line):
    lo, hi = line.split('-')
    return int(lo), int(hi)

exclude = set(map(range, data.splitlines()))

include = 0
n = 0
M = 1<<32

while n < M:
    hits = {r for r in exclude if r[0] <= n <= r[1]}
    if not hits:
        m = min((r[0] for r in exclude if r[0] > n), default=M)
        include += m - n
        n = m
    else:
        exclude -= hits
        n = max(r[1] for r in hits) + 1

print(include)
