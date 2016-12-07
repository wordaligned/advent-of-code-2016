import sys
from collections import Counter

data = '''\
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''

data = sys.stdin.read()

words = data.splitlines()
N = len(words[0])
counts = [Counter(w[n] for w in words) for n in range(N)]

print(''.join(c.most_common()[-1][0] for c in counts))
