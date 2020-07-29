from graph import Graph

def dfs(g: Graph, v: int):
    '''
    Simple recursive dfs implementation with a helper function.
    '''
    if not g.has_vertex(v):
        raise ValueError(f"Vertex {v} not found in graph {g}")
    visited = set()

    def visit(cur_vertex: int):
        visited.add(cur_vertex)
        print(f"Visiting {cur_vertex}")
        for next_vertex in g.get_adjacent_vertices(cur_vertex):
            if next_vertex not in visited:
                visit(next_vertex)
    
    visit(v)

if __name__ == "__main__":
    g = Graph(list(range(4)), [])
    g.add_edge((0, 1))
    g.add_edge((0, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 3))
    dfs(g, 0)