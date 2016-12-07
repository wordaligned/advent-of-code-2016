import sys

data = '''ULL
RRDDD
LURDL
UUUUD'''

data = sys.stdin.read()

pad = { 0:'1',    1:'2',    2:'3',
       1j:'4', 1+1j:'5', 2+1j:'6',
       2j:'7', 1+2j:'8', 2+2j:'9'}

pos = 1+1j
code = ''
for line in data.splitlines():
    for d in line:
        step = {'U':-1j, 'L':-1, 'D':1j, 'R':1}[d]
        if pos+step in pad:
            pos += step
    code += pad[pos]

print(code)


        
