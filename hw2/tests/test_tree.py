import unittest

from tree.print_tree import Node, Tree


class TestPrintTree(unittest.TestCase):
    def test1(self):
        node1 = Node(0)
        self.answer = [['0']]
        self.input = Tree.print_tree(node1)
        assert self.input == self.answer

    def test2(self):
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
        self.input = Tree.print_tree(node1)
        self.answer = [['|', '|', '|', '2', '|', '|', '|'],
                       ['|', '4', '|', '|', '|', '6', '|'],
                       ['1', '|', '3', '|', '5', '|', '7']]
        assert self.input == self.answer

    def test3(self):
        node1 = Node(2)
        node2 = Node(4)
        node3 = Node(6)
        node4 = Node(1)
        node1.left = node2
        node2.left = node3
        node3.left = node4
        self.input = Tree.print_tree(node1)
        self.answer = [['|', '|', '|', '|', '|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|'],
                       ['|', '|', '|', '4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                       ['|', '6', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                       ['1', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        assert self.input == self.answer

    def test4(self):
        root = Node(1)
        r11 = Node(2)
        r12 = Node(3)
        r21 = Node(4)
        r22 = Node(5)
        r23 = Node(6)
        r31 = Node(7)
        r32 = Node(8)
        r33 = Node(9)
        root.left = r11
        root.right = r12
        r11.left = r21
        r11.right = r22
        r12.left = r23
        r23.right = r33
        r21.right = r31
        r22.left = r32
        self.input = Tree.print_tree(root)
        self.answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                       ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                       ['|', '4', '|', '|', '|', '5', '|', '|', '|', '6', '|', '|', '|', '|', '|'],
                       ['|', '|', '7', '|', '8', '|', '|', '|', '|', '|', '9', '|', '|', '|', '|']]

        assert self.input == self.answer
