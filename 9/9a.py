import sys
data = ('ADVENT'
        'A(1x5)BC'
        '(3x3)XYZ'
        'A(2x2)BCD(2x2)EFG'
        '(6x1)(1x3)A'
        'X(8x2)(3x3)ABCY')

data = sys.stdin.read()

result = 0
i, N = 0, len(data)

while i != N:
    j = data.find('(', i)
    if j != -1:
        result += j - i
        i = data.find(')', j)
        n_x_r = data[j+1:i].partition('x')
        n, r = int(n_x_r[0]), int(n_x_r[2])
        result += n * r
        i += 1 + n
    else:
        result += N - i
        i = N

print(result)
