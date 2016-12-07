import re
import sys

from itertools import permutations

data = '''\
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn'''

data = sys.stdin.read()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pairs = [''.join(p) for p in permutations(alphabet, 2)]
abbas = [p + p[::-1] for p in pairs]
findall = re.compile(r'\[([a-z]+)\]').findall

def has_tls(ip):
    return any(abba in ip for abba in abbas)

def hypernet_sequences(ip):
    return findall(ip)

support_tls = sum(
    1 for ip in data.splitlines()
    if not any(has_tls(h) for h in hypernet_sequences(ip))
    and has_tls(ip))

print(support_tls)
