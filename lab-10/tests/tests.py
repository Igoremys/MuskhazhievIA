import unittest
from graph_representation import AdjacencyMatrixGraph, AdjacencyListGraph
from graph_traversal import bfs, dfs_recursive, dfs_iterative
from shortest_path import find_connected_components, topological_sort, dijkstra

class TestGraphs(unittest.TestCase):
    def test_matrix_graph(self):
        g = AdjacencyMatrixGraph(directed=False)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        self.assertTrue(g.has_edge(0, 1))
        self.assertEqual(len(g.get_neighbors(1)), 2)

    def test_list_graph(self):
        g = AdjacencyListGraph(directed=True)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 3)
        self.assertEqual(g.get_neighbors(0), [(1, 5)])

    def test_bfs(self):
        g = AdjacencyListGraph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        dist, _ = bfs(g, 0)
        self.assertEqual(dist[2], 2)

    def test_dfs(self):
        g = AdjacencyListGraph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        order1 = dfs_recursive(g, 0)
        order2 = dfs_iterative(g, 0)
        self.assertIn(1, order1)
        self.assertIn(2, order2)

    def test_components(self):
        g = AdjacencyListGraph()
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        comps = find_connected_components(g)
        self.assertEqual(len(comps), 2)

    def test_topo(self):
        g = AdjacencyListGraph(directed=True)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        order = topological_sort(g)
        self.assertEqual(order, [0, 1, 2])

    def test_dijkstra(self):
        g = AdjacencyListGraph(directed=True)
        g.add_edge(0, 1, 4)
        g.add_edge(0, 2, 1)
        g.add_edge(2, 1, 2)
        dist, _ = dijkstra(g, 0)
        self.assertEqual(dist[1], 3)

if __name__ == '__main__':
    unittest.main()