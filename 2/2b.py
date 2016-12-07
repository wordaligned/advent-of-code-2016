import sys

data = '''ULL
RRDDD
LURDL
UUUUD'''

data = sys.stdin.read()

pad = {                0   :'1',
           -1+1j:'2',  0+1j:'3',   1+1j:'4',
-2+2j:'5', -1+2j:'6',    2j:'7',   1+2j:'8',  2+2j:9,
           -1+3j:'A',  0+3j:'B',   1+3j:'C',
                         4j:'D'}

pos = -2+2j
code = ''
for line in data.splitlines():
    for d in line:
        step = {'U':-1j, 'L':-1, 'D':1j, 'R':1}[d]
        if pos+step in pad:
            pos += step
    code += pad[pos]

print(code)
