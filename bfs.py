from graph import Graph
from collections import deque

def bfs(g: Graph, v: int):
    if not g.has_vertex(v):
        raise ValueError(f"Vertex {v} not found in graph {g}.")
    
    queue = deque()
    queue.append(v)

    visited = set()

    while queue:
        current_vertex = queue.popleft()
        if current_vertex not in visited:
            print(f"Processing vertex {current_vertex}")
            queue.extend(g.get_adjacent_vertices(current_vertex))
        visited.add(current_vertex)

    
    print("Finished processing")

if __name__ == "__main__":
    g = Graph(list(range(4)), [])
    g.add_edge((0, 1))
    g.add_edge((0, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 3))
    bfs(g, 0)