import sys
from itertools import count

data = sys.stdin.read()

cmds = [line.split() for line in data.splitlines()]

def tgl(cmds, pos):
    if 0 <= pos < len(cmds):
        cmd = cmds[tpos]
        if len(cmd) == 2:
            cmd[0] = 'dec' if cmd[0]=='inc' else 'inc'
        elif len(cmd) == 3:
            cmd[0] = 'cpy' if cmd[0]=='jnz' else 'jnz'

def val(v):
    return regs[v] if v in regs else int(v)

signal = [i % 2 for i in range(100)]

for n in count():
    print(n)
    regs = {r: 0 for r in 'bcd'}
    regs['a'] = n
    output = []
    pos = 0
    while 0 <= pos < len(cmds) and output == signal[:len(output)] and len(output) < len(signal):
        cmd = cmds[pos]
        if cmd[0] == 'tgl':
            tpos = pos + val(cmd[1])
            tgl(cmds, tpos)
            pos += 1
        elif cmd[0] == 'cpy':
            regs[cmd[2]] = val(cmd[1])
            pos += 1
        elif cmd[0] == 'inc':
            regs[cmd[1]] += 1
            pos += 1
        elif cmd[0] == 'dec':
            regs[cmd[1]] -= 1
            pos += 1
        elif cmd[0] == 'jnz':
            test = val(cmd[1])
            step = val(cmd[2])
            pos = pos + (step if test else 1)
        else:
            assert cmd[0] == 'out'
            output.append(val(cmd[1]))
            pos += 1

    if output == signal:
        break

print(n)
