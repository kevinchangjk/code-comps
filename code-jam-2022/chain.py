t = int(input())

class Module:
    def __init__(self, fun):
        self.fun = fun
        self.children = []
        self.parent = -1

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def is_root(self):
        return self.parent == -1

    # recursively compute max fun by comparing with children's fun
    def find_fun(self):
        res = 0
        num_children = len(self.children)

        if (num_children == 0):
            return self.fun

        min_child = -1
        min_fun = float('inf')
        children_fun = []
        for i in range(num_children):
            child = self.children[i]
            child_fun = child.find_fun()
            children_fun.append(child_fun)
            if child_fun < min_fun:
                min_fun = child_fun
                min_child = i

        # main idea here:
        # fun of a tree is the max of the root's fun and the minimum fun of the children
        # summed together with the other funs of the children
        children_fun.pop(min_child)
        res += sum(children_fun)
        res += max(self.fun, min_fun)
        return res

def init_modules(mods):
    res_modules = []
    for mod in mods:
        fun = int(mod)
        res_modules.append(Module(fun))

    return res_modules

def init_tree(pointers, modules, n):
    for i in range(n):
        child = modules[i]
        parent_num = int(pointers[i]) - 1
        if parent_num != -1:
            parent = modules[parent_num]
            child.set_parent(parent)
            parent.add_child(child)

def solve():
    n = int(input())
    modules = init_modules(input().split())
    init_tree(input().split(), modules, n)

    res = 0
    for mod in modules:
        if mod.is_root():
            res += mod.find_fun()

    return res

for i in range(t):
    print(f"Case #{i + 1}: {solve()}")
