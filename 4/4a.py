import collections
import re
import sys

Room = collections.namedtuple('Room', 'name sector checksum')

data = '''\
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''

data = sys.stdin.read()

match = re.compile(r'([a-z-]+)-(\d+)\[([a-z]+)\]').match

def room(r):
    m = match(r)
    return Room(m.group(1).replace('-', ''), int(m.group(2)), m.group(3))

def valid_room(r):
    counts = collections.Counter(r.name)
    def key(kv):
        return -kv[1], kv[0]
    return r.checksum == ''.join(c for c,_ in sorted(counts.most_common(), key=key)[:5])

rooms = map(room, data.splitlines())

print(sum(r.sector for r in rooms if valid_room(r)))
