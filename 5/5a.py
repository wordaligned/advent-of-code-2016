from hashlib import md5
from itertools import count

start = 'abc'
start = 'ojvtpuvg'

password = ''

n = count()

while len(password) < 8:
    m = md5()
    m.update((start + str(next(n))).encode())
    d = m.hexdigest()
    if d.startswith('00000'):
        password = password + d[5]

print(password)
