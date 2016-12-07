import re
import sys

from itertools import permutations, chain

data = '''\
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''

data = sys.stdin.read()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pairs = [''.join(p) for p in permutations(alphabet, 2)]
abababs = [(p+p[0],p[1]+p) for p in pairs]

findall = re.compile(r'(\w*)\[(\w*)\](\w*)').findall

def has_tls(ip):
    return any(abba in ip for abba in abbas)

def supernet_sequences(ip):
    return list(chain.from_iterable((m[0], m[2]) for m in findall(ip)))

def hypernet_sequences(ip):
    return [m[1] for m in findall(ip)]

support_ssl = 0

for ip in data.splitlines():
    ss = supernet_sequences(ip)
    hs = hypernet_sequences(ip)
    support_ssl += any(
        any(aba in s for s in ss) and any(bab in h for h in hs)
        for aba, bab in abababs)

print(support_ssl)
