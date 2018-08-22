class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(Node):
    def __init__(self, root):
        self.root = root

    @classmethod
    def find_depth(cls, root):
        # resursive function to find depth
        # find depth of whichever side gets to bottom first
        if root.left:
            left_depth = cls.find_depth(root.left)
        else:
            left_depth = 0
        if root.right:
            right_depth = cls.find_depth(root.right)
        else:
            right_depth = 0
        return max(left_depth, right_depth)+1

    @classmethod
    def print_tree(cls, root):
        # first define function to fill a blank tree
        def fill_tree(root, d, w):
            # recursion to get depth and position of each number to fill
            # d to track depth of node
            # w to track left and right branches
            if root.left:
                fill_tree(root.left, d+1, w+[-1])
            if root.right:
                fill_tree(root.right, d+1, w+[1])
            # find position according to depth and branches record
            index = int((width+1)/2)-1
            space = int((width+1)/2)
            for i in range(len(w)):
                index += w[i]*int(space/2)
                space = int(space/2)
            # fill the blank
            df[d][index] = str(root.value)
        # create blank tree
        depth = cls.find_depth(root)
        width = sum([2**i for i in range(depth)])
        df = [['|' for i in range(width)] for j in range(depth)]
        fill_tree(root, 0, [])
        for i in range(depth):
            print("".join(df[i])+"\n")
        return df


if __name__ == '__main__':
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(1)
    node5 = Node(3)
    node6 = Node(5)
    node7 = Node(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    tree = Tree(node1)
    tree.print_tree(node1)
