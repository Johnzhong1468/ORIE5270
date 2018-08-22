class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(Node):
    def __init__(self, root):
        self.root = root
    def find_depth(self, root):
        if root.left:
            l = self.find_depth(root.left)
        else:
            l = 0
        if root.right:
            r = self.find_depth(root.right)
        else:
            r = 0
        return max(l,r)+1
        
    def print_tree(self,root):
        def fill_tree(root,d,w):
            if root.left:
                fill_tree(root.left,d+1,w+[-1])        
            if root.right:
                fill_tree(root.right,d+1,w+[1])
            #print(root.value,d,w)

            index = int((width+1)/2)-1
            l = int((width+1)/2)
            for i in range(len(w)):
                index += w[i]*int(l/2)
                l = int(l/2)
            df[d][index] = str(root.value)
        depth = self.find_depth(root)
        width = sum([2**i for i in range(depth)])
        df = [[' ' for i in range(width)] for j in range(depth)]
        fill_tree(self.root,0,[])
        for i in range(depth):
            print("".join(df[i])+"\n")



if __name__ == '__main__':
    root = Node(1)
    r11 = Node(2)
    r12 = Node(3)
    r21 = Node(4)
    r22 = Node(5)
    r23 = Node(6)
    r31 = Node(7)
    r32 = Node(8)
    r33 = Node(9)
    r41 = Node(10)
    root.left = r11
    root.right = r12
    r11.left = r21
    r11.right = r22
    r12.left = r23
    r23.right = r33
    r21.right = r31
    r22.left = r32
    r32.right = r41
    tree = Tree(root)
    tree.print_tree(root)
