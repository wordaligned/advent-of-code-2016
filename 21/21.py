import itertools
import re
import sys

def read_ints(s):
    findall = re.compile('\d+').findall
    return list(map(int, findall(s)))

def rot(s, r):
    s[:] = s[-r:] + s[:-r]

def swi(s, i, j):
    s[i], s[j] = s[j], s[i]

def mov(s, i, j):
    s.insert(j, s.pop(i))

def rev(s, i, j):
    s[i:j+1] = s[i:j+1][::-1]

data = '''\
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
'''
data = sys.stdin.read()

def process(ops, s):
    s = list(s)
    for cmd in ops:
        ww = cmd.split()
        ii = read_ints(cmd)
        op = cmd.startswith
        if   op('swap position'): swi(s, ii[0], ii[1])
        elif op('swap letter')  : swi(s, s.index(ww[2]), s.index(ww[5]))
        elif op('rotate left')  : rot(s, -ii[0])
        elif op('rotate right') : rot(s, ii[0])
        elif op('reverse')      : rev(s, ii[0], ii[1])
        elif op('move')         : mov(s, ii[0], ii[1])
        elif op('rotate based') :
            pos = s.index(ww[6])
            rot(s, (pos + 1 + (pos >= 4)) % len(s))
    return ''.join(s)

s = list('abcde')
s = list('abcdefgh')

ops = data.splitlines()
print(process(ops, s))

print(next(''.join(s) for s in itertools.permutations('fbgdceah')
           if process(ops, s) == 'fbgdceah'))
