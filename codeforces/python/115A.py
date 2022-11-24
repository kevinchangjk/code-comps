n = int(input())
tree = []

def find(man):
    for branch in tree:
        if man in branch:
            return tree.index(branch)

for emp in range(1, n+1):
    manage = int(input())
    if manage == -1:
        if len(tree) == 0:
            tree.append([])
        tree[0].append(emp)
    else: 
        dest = find(manage) + 1
        if len(tree) == dest:
            tree.append([])
        tree[dest].append(emp)
    
print(len(tree))
        