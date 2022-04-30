t = int(input())

def convert(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(letter)

class Tower:
    def __init__(self, blocks):
        self.blocks = blocks
        self.start = convert(blocks[0])
        self.end = convert(blocks[-1])
        self.valid = True
        self.letters = [0 for i in range(26)]
        for i in range(len(blocks)):
            if i == 0:
                self.letters[convert(blocks[i])] = 1
                continue
            if blocks[i] == blocks[i-1]:
                continue
            else:
                ind = convert(blocks[i])
                if self.letters[ind] == 1:
                    self.valid = False
                else:
                    self.letters[ind] = 1
                    continue

    def is_valid(self, tower):
        common = self.end
        if common != tower.start:
            common = False
        for i in range(26):
            if self.letters[i] == 1 and tower.letters[i] == 1:
                if self.end != tower.start or i != self.end:
                    return False
                else:
                    continue
            else:
                continue
        return True

    def append(self, tower):
        valid = self.is_valid(tower)
        if not valid:
            return False
        self.blocks = self.blocks + tower.blocks
        self.end = tower.end
        for i in range(26):
            if self.letters[i] == 1 or tower.letters[i] == 1:
                self.letters[i] = 1
            else:
                continue
        return self


def solve():
    n = int(input())
    inn = input().split()
    towers = []
    for innn in inn:
        tower = Tower(innn)
        towers.append(tower)
    starts = [[] for i in range(26)]
    ends = [[] for i in range(26)]
    for tower in towers:
        if not tower.valid:
            return "IMPOSSIBLE"
        starts[tower.start].append(tower)
        ends[tower.end].append(tower)

    def append_towers(front, back):
        ends[front.end].pop(ends[front.end].index(front))
        starts[back.start].pop(starts[back.start].index(back))
        ends[back.end].pop(ends[back.end].index(back))
        ends[back.end].append(front)
        front = front.append(back)
        if not front:
            return False
        towers.remove(back)
        return True

    while len(towers) > 1:
        # print("-----")
        # for tower in towers:
        #     print(tower.blocks)
        # take the first
        curr = towers[0]
        # add to the front
        viable = ends[curr.start].copy()
        if len(viable) == 1 and viable[0] != curr:
            pre = viable[0]
            if not append_towers(pre, curr):
                return "IMPOSSIBLE"
            continue
        elif len(viable) > 1:
            non_con = -1
            for via_i in range(len(viable)):
                if viable[via_i] == curr:
                    continue
                blocks = [convert(block) for block in viable[via_i].blocks]
                for block in blocks:
                    if block != curr.start:
                        if non_con == -1:
                            non_con = viable[via_i]
                            break
                        else:
                            return "IMPOSSIBLE"
            if curr in viable:
                viable.remove(curr)
            for j in range(len(viable)):
                if viable[j] != non_con:
                    pre = viable[j]
                    if not append_towers(pre, curr):
                        return "IMPOSSIBLE"
                    curr = pre
            if non_con != -1:
                if not append_towers(non_con, curr):
                    return "IMPOSSIBLE"
            continue

        # nothing to add to the front, add to the back
        viable = starts[curr.end].copy()
        if len(viable) == 1 and viable[0] != curr:
            post = viable[0]
            if not append_towers(curr, post):
                return "IMPOSSIBLE"
            continue
        elif len(viable) > 1:
            non_con = -1
            for via_i in range(len(viable)):
                if viable[via_i] == curr:
                    continue
                blocks = [convert(block) for block in viable[via_i].blocks]
                for block in blocks:
                    if block != curr.end:
                        if non_con == -1:
                            non_con = viable[via_i]
                            break
                        else:
                            return "IMPOSSIBLE"
            if curr in viable:
                viable.remove(curr)
            for j in range(len(viable)):
                if viable[j] != non_con:
                    post = viable[j]
                    if not append_towers(curr, post):
                        return "IMPOSSIBLE"
            if non_con != -1:
                if not append_towers(curr, non_con):
                    return "IMPOSSIBLE"
            continue

        # nothing matches at all, just add to the front of a non-matching one
        post = -1
        for tower in towers:
            if tower == curr:
                continue
            endss = ends[tower.start]
            length = len(endss)
            if tower in endss:
                length -= 1
            if length == 0:
                post = tower
                break
        if post == -1:
            return "IMPOSSIBLE"
        if not append_towers(curr, post):
            return "IMPOSSIBLE"
        continue
    
    return towers[0].blocks

for i in range(t):
    print(f"Case #{i + 1}: {solve()}")
