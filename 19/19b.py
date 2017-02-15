N = 3005290
elves = list(range(1, N+1))

while N > 1:
    try:
        d = 0
        for i in range(N):
            elves[i + N//2 + d] = 0
            N -= 1
            d += 1
    except IndexError:
        elves = [e for e in elves if e]
        elves = elves[i:] + elves[:i]

print(elves.pop())
