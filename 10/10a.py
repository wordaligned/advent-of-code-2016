import re
import sys
from collections import defaultdict

data = '''\
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''

data = sys.stdin.read()

bots = defaultdict(list)
outs = defaultdict(list)
gives = {}

class bot(int): pass
class out(int): pass

def ints(s):
    return list(map(int, re.compile('\d+').findall(s)))

def dests(s):
    return re.compile('bot|output').findall(s)

def assign(v, b):
    bots[b].append(v)

def distribute(ds, vs):
    gives[vs[0]] = (bot(vs[1]) if ds[1]=='bot' else out(vs[1]),
                    bot(vs[2]) if ds[2]=='bot' else out(vs[2]))

def read_instruction(line):
    if line.startswith('value'):
        return assign(*ints(line))
    elif line.startswith('bot'):
        return distribute(dests(line), ints(line))
    assert 0

def read():
    for line in data.splitlines():
        read_instruction(line)

assert(all(len(vs) < 3 for vs in bots.values()))

def operate():
    try:
        while True:
            b, vs = next((b, vs) for b, vs in bots.items() if len(vs)==2)
            lo, hi = min(vs), max(vs)
            if (lo, hi) == (17, 61):
                print('bot', b)
            bots[b].clear()
            dlo, dhi = gives[b]
            if isinstance(dlo, bot):
                bots[dlo].append(lo)
            else:
                outs[dlo].append(lo)
            if isinstance(dhi, bot):
                bots[dhi].append(hi)
            else:
                outs[dhi].append(hi)
    except StopIteration:
        pass

def dump():
    for o, v in sorted(outs.items()):
        print(o, v)

read()
operate()
dump()
