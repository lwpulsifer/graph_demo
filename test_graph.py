import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.test_graph = self.generate_test_graph()
    
    def generate_test_graph(self):
        graph = Graph(list(range(10)), [])
        return graph
    
    def test_init(self):
        self.assertTrue(True)
    
    def test_delete(self):
        with self.assertRaises(ValueError):
            self.test_graph.delete_edge((20, 30))
    
    def test_add(self):
        self.test_graph.add_edge((0, 1))
        self.assertTrue((0, 1) in self.test_graph)

if __name__ == "__main__":
    unittest.main()