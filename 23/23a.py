import sys

data = '''\
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''

data = sys.stdin.read()

regs = {r: 0 for r in 'abcd'}
regs['a'] = int(sys.argv[1])
pos, cmds = 0, [line.split() for line in data.splitlines()]

def tgl(cmds, pos):
    if 0 <= pos < len(cmds):
        cmd = cmds[tpos]
        if len(cmd) == 2:
            cmd[0] = 'dec' if cmd[0]=='inc' else 'inc'
        elif len(cmd) == 3:
            cmd[0] = 'cpy' if cmd[0]=='jnz' else 'jnz'

def val(v):
    return regs[v] if v in regs else int(v)

while 0 <= pos < len(cmds):
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
    else:
        assert(cmd[0]) == 'jnz'
        test = val(cmd[1])
        step = val(cmd[2])
        pos = pos + (step if test else 1)

print(regs['a'])
