from hashlib import md5
from itertools import count

start = 'abc'
start = 'ojvtpuvg'

n = count()
password = {}

while len(password) < 8:
    m = md5()
    m.update((start + str(next(n))).encode())
    d = m.hexdigest()
    if d.startswith('00000'):
        pos = d[5]
        if pos not in password and pos in '01234567':
            password[pos] = d[6]

print(''.join(password[c] for c in '01234567'))

