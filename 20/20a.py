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

n = 0

while exclude:
    hits = {r for r in exclude if r[0] <= n <= r[1]}
    if not hits:
        break
    n = max(r[1] for r in hits) + 1
    exclude -= hits

print(n)
