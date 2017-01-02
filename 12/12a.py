import sys

data = '''\
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

data = sys.stdin.read()

regs = {r: 0 for r in 'abcd'}
pos, cmds = 0, data.splitlines()

while pos < len(cmds):
    cmd = cmds[pos].split()
    if cmd[0] == 'cpy':
        regs[cmd[2]] = regs[cmd[1]] if cmd[1] in regs else int(cmd[1])
        pos += 1
    elif cmd[0] == 'inc':
        regs[cmd[1]] += 1
        pos += 1
    elif cmd[0] == 'dec':
        regs[cmd[1]] -= 1
        pos += 1
    else:
        assert(cmd[0]) == 'jnz'
        test = regs[cmd[1]] if cmd[1] in regs else int(cmd[1])
        pos = pos + (int(cmd[2]) if test else 1)

print(regs['a'])
