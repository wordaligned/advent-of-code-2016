import collections
import hashlib
import itertools
import re

salt = 'zpqevtbw'
#salt = 'abc'

def find_3(s):
    m = re.compile(r'(\w)\1\1').search(s)
    return m and m.group(1)

def find_5(s):
    return re.compile(r'(\w)\1\1\1\1').findall(s)

def _hash(s):
    return hashlib.md5(s.encode()).hexdigest()

def _stretched_hash(s):
    for _ in range(2017):
        s = _hash(s)
    return s

def generate_keys():
    keyq = collections.deque()
    for n in itertools.count():
        if keyq and n > keyq[0][1] + 1000:
            keyq.popleft()
        h = hash(salt + str(n))
        tr = find_3(h)
        qn = find_5(h)
        for k in keyq:
            if k[0] in qn:
                yield k
        keyq = collections.deque(k for k in keyq if k[0] not in qn)
        if tr:
            keyq.append((tr, n))

def answer():
    keys = [k for k,_ in zip(generate_keys(), range(64))]
    return keys[-1][1]

hash = _hash
print(answer())

hash = _stretched_hash
print(answer())


