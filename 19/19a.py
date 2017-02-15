# f(x0,...xn) => f(x0, x2, ... xn-1) (n odd)
#             => f(xn, x0, ... )    (n even)'''


N = 3005290
elves = list(range(1, N+1))

while len(elves) > 1:
    last = [elves.pop()] if len(elves) % 2 else []
    elves = last + elves[::2]

print(elves.pop())
