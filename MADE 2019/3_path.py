class Tree:
    awful_steps = 0
    deleted_files = 0


    def __init__(self, name, parent=None):
        self.depth_path = 0
        self.parent = parent
        self.children = {}
        self.name = name

    def if_file(self):
        if len(self.children) == 0:
            return True
        else:
            return False
    def add_path(self, full_path: list):
        child = self.get_children(full_path[0])

        if child is None:
            child = Tree(full_path[0], parent=self)

        if self.depth_path < len(full_path):
            self.depth_path = len(full_path)

        if len(full_path[1:]) > 0:
            child.add_path(full_path[1:])

        self.add_child(child)

    def direc_main(self):
        if self.parent is None:
            return Tree
        else:
            return False

    def add_child(self, top):
        self.children[top.name] = top

    def get_children(self, name):
        if name in self.children:
            return self.children[name]
        else:
            return None

    def leafs(self):
        def order_len(value):
            return value.depth_path

        if self.direc_main():
            time = 0
        else:
            time = 1

        if self.is_file():
            Tree.deleted_files += 1

        top_order = list(self.children.values())
        top_order.sort(key=order_len)

        for v in top_order:
            time += v.leafs()

            if Tree.deleted_files >= n and not self.direc_main():
                Tree.awful_steps += 1

            if not v.if_file():
                time += 1

        return time


def read_data(count):
    node = Tree('0')
    for i in range(count):
        path = str(input())
        path_list = path.split('/')
        node.add_path(path_list[1:])
    return node


n = int(input())

root = read_data(n)

print(root.leafs() - Tree.awful_steps)