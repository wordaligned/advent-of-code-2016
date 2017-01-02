# Disc #1 has 7 positions; at time=0, it is at position 0.
# Disc #2 has 13 positions; at time=0, it is at position 0.
# Disc #3 has 3 positions; at time=0, it is at position 2.
# Disc #4 has 5 positions; at time=0, it is at position 2.
# Disc #5 has 17 positions; at time=0, it is at position 0.
# Disc #6 has 19 positions; at time=0, it is at position 7.

discs = [(7, 0),
         (13, 0),
         (3, 2),
         (5, 2),
         (17, 0),
         (19, 7)]

#discs = ((5,4),(2,1))

def slots_first_align(discs):
    t = 0
    while any((pos + t + d) % posns for d, (posns, pos) in enumerate(discs, 1)):
        t += 1
    return t

print(slots_first_align(discs))
print(slots_first_align(discs + [(11, 0)]))
