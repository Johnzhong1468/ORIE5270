import unittest

from graph.graph import find_shortest_path, find_negative_cycles


class TestGraphs(unittest.TestCase):
    def test_shortest_1(self):
        self.answer = (3.0, [1, 5, 8])
        self.input = find_shortest_path("shortest_graph.txt", 1, 8)
        assert self.input == self.answer

    def test_shortest_2(self):
        self.answer = (None, None)
        self.input = find_shortest_path("shortest_graph.txt", 1, 4)
        assert self.input == self.answer

    def test_shortest_3(self):
        self.answer = (5, [8, 5, 3, 9])
        self.input = find_shortest_path("shortest_graph.txt", 8, 9)
        assert self.input == self.answer

    def test_shortest_4(self):
        self.answer = (5, [1, 2, 3, 4, 6])
        self.input = find_shortest_path("shortest_graph1.txt", 1, 6)
        assert self.input == self.answer

    def test_negative_cycle_1(self):
        self.answer = None
        self.input = find_negative_cycles("shortest_graph.txt")
        assert self.input == self.answer

    def test_negative_cycle_2(self):
        self.answer = [3, 9, 8, 5, 3]
        self.input = find_negative_cycles("cycle_graph.txt")
        assert self.input == self.answer

    def test_negative_cycle_3(self):
        self.answer = [2, 3, 5, 4, 2]
        self.input = find_negative_cycles("cycle_graph1.txt")
        assert self.input == self.answer
