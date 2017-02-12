from heapq import *

def a_star(start, h, moves):
    '''A-star graph search

    start - initial state
    h(s) heuristic estimates path length from s to finish
    moves(s) are possible moves from state s
    '''
    cost = {start: 0}
    prev = {start: None}
    fringe = [(h(start), start)]
    heapify(fringe)

    def path(s):
        return [] if s is None else path(prev[s]) + [s]

    while fringe:
        f, s = heappop(fringe)
        if h(s) == 0:
            return path(s)
        c = cost[s] + 1
        for t in moves(s):
            if t not in cost or c < cost[t]:
                cost[t] = c
                heappush(fringe, (c + h(t), t))
                prev[t] = s


