'''The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.'''

import copy
import math
from itertools import chain, combinations

import a_star

Pm, Pu, Ru, Sr, Tm, El, Di = range(7)

F = frozenset

start = (1,                               # Where the elevator is
         (F({Tm, Pu, Sr}), F({Tm})),      # generators, chips on floor 1
         (F(),             F({Pu, Sr})),  # ditto                floor 2
         (F({Pm, Ru}),     F({Pm, Ru})),  # ...
         (F(),             F()))

def valid(rtgs, chips):
    exposed = chips - rtgs
    return not exposed or not rtgs

def moves(state):
    floor = state[0]
    rtgs, chips = state[floor]
    moveable = [(r, 0) for r in rtgs] + [(c, 1) for c in chips]
    for rc in chain(combinations(moveable, 2), combinations(moveable, 1)):
        rm = {r for r,t in rc if t==0}
        cm = {c for c,t in rc if t==1}
        for new_floor in {floor+1, floor-1} & {1,2,3,4}:
            rtgs_, chips_ = state[new_floor]
            if valid(rtgs - rm, chips - cm) and valid(rtgs_ | rm, chips_ | cm):
                new_state = list(copy.deepcopy(state))
                new_state[0] = new_floor
                new_state[floor] = rtgs - rm, chips - cm
                new_state[new_floor] = rtgs_ | rm, chips_ | cm
                yield tuple(new_state)

def heuristic(state):
    s = sum((len(state[i][0]) + len(state[i][1]) * (4 - i))
            for i in range(1, 4))
    return math.ceil(s / 2)

path = a_star.a_star(start, heuristic, moves)
print(len(path) - 1)

start = (1,                                          # Where the elevator is
         (F({Tm, Pu, Sr, El, Di}), F({Tm, El, Di})), # generators, chips on floor 1
         (F(),                     F({Pu, Sr})),     # ditto                floor 2
         (F({Pm, Ru}),             F({Pm, Ru})),     # ...
         (F(),                     F()))

path = a_star.a_star(start, heuristic, moves)
print(len(path) - 1)
