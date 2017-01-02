from itertools import islice

row = list('.^^.^.^^^^')
R = 10

row = list('^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.')
R = 400000

def trap(above):
    return '^' if above in (list('^..'),list('..^'),
                            list('^^.'),list('.^^')) else '.'

def rows(row):
    N = len(row)
    while True:
        yield row
        row = ['.'] + row + ['.']
        row = [trap(row[i-1:i+2]) for i in range(1,N+1)]

print(sum(row.count('.') for row in islice(rows(row), R)))
