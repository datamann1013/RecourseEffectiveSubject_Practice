import unittest
from dfs import dfs_recursive, dfs_iterative

class DFSTest(unittest.TestCase):
    def setUp(self):
        # Eksempelgraf med en syklus: A—B—E og A—C, B—D
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A'],
            'D': ['B'],
            'E': ['B']
        }

    def test_recursive_full(self):
        visited = dfs_recursive(self.graph, 'A')
        self.assertCountEqual(visited, ['A','B','D','E','C'])

    def test_iterative_full(self):
        visited = dfs_iterative(self.graph, 'A')
        self.assertCountEqual(visited, ['A','B','D','E','C'])

    def test_single_node(self):
        g = {'X': []}
        self.assertEqual(dfs_recursive(g, 'X'), ['X'])
        self.assertEqual(dfs_iterative(g, 'X'), ['X'])

    def test_disconnected(self):
        g = {'A':['B'], 'B':['A'], 'C':[]}
        self.assertCountEqual(dfs_recursive(g,'A'), ['A','B'])
        self.assertCountEqual(dfs_iterative(g,'A'), ['A','B'])

    def test_cycle(self):
        g = {'A':['B'], 'B':['A']}
        self.assertEqual(dfs_recursive(g,'A'), ['A','B'])
        self.assertEqual(dfs_iterative(g,'A'), ['A','B'])

    def test_invalid_start(self):
        with self.assertRaises(KeyError):
            dfs_recursive(self.graph, 'Z')
        with self.assertRaises(KeyError):
            dfs_iterative(self.graph, 'Z')

if __name__ == '__main__':
    unittest.main()
