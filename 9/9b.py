import sys
data = ('(3x3)XYZ'
        'X(8x2)(3x3)ABCY'
        '(27x12)(20x12)(13x14)(7x10)(1x12)A'
        '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')

data = sys.stdin.read()

def decompress_length(b, e):
    j = data.find('(', b, e)
    if j == -1:
        result = e - b
    else:
        result = j - b
        b = data.find(')', j, e)
        assert b != -1
        n_x_r = data[j+1:b].partition('x')
        n, r = int(n_x_r[0]), int(n_x_r[2])
        assert b+1+n <= e
        result += r * decompress_length(b+1, b+1+n)
        result += decompress_length(b+1+n, e)
    return result

print(decompress_length(0, len(data)))
