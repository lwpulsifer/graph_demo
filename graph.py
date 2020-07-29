'''
A custom Graph implementation for the Real Python video series 
Graphs in Python. Uses an adjacency list internally
and allows the user to print the graph in both adjacency list and
adjacency matrix form.

My plan to demo this is to do the following methods live:
- init
- build_adjacency_list
- add_[vertex,edge]
- delete_[vertex,edge]
- get_adjacent_vertices

I'll write those with minimal error-handling, then encourage
the viewer to implement some of that and the additional methods
on their own. I'll provide this code for download to check their work.
I'll also probably omit the type annotations in the demo.

@author Liam Pulsifer, 24 July 2020
'''
from typing import List, Tuple, Iterable
from matrix_print import print_matrix

class Graph():

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int]]=None):
        self._adjacency_list = self.build_adjacency_list(vertices, edges)
    
    def build_adjacency_list(self, vertices: List[int], edges: List[Tuple[int, int]]):
        '''
        Builds an adjacency list from the provide lists of vertices and edges.
        '''
        adjacency_list = {}
        for vertex in vertices:
            adjacency_list[vertex] = set()
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)
        return adjacency_list
    
    def add_vertex(self, vertex: int):
        '''
        Adds the provided vertex to the graph.
        Raises ValueError if the vertex is already present.
        '''
        if vertex in self._adjacency_list:
            raise ValueError(f"Vertex {vertex} is already in the graph.")
        else:
            self._adjacency_list[vertex] = set()
    
    def delete_vertex(self, vertex: int):
        '''
        Deletes the given vertex and all edges incident upon it from the graph.
        Raises ValueError if the vertex is not present in the graph.
        '''
        if vertex not in self._adjacency_list:
            raise ValueError(f"Vertex {vertex} is not in the graph.")
        else:
            del self._adjacency_list[vertex]
            for other_vertex in self._adjacency_list:
                self._adjacency_list[other_vertex].discard(vertex)
    
    def add_edge(self, edge: Tuple[int, int]):
        '''
        Adds the undirected edge (u, v) to the graph. 
        Raises ValueError if the edge is already present, or if the 
        edge to be added is a self-edge.
        '''
        u, v = edge
        self.check_vertices_exist(edge)
        if v in self._adjacency_list[u] and u in self._adjacency_list[v]:
            raise ValueError(f"Edge {edge} is already in the graph.")
        elif u == v:
            raise ValueError(f"Self edges not permitted.")
        else:
            self._adjacency_list[u].add(v)
            self._adjacency_list[v].add(u)
    
    def delete_edge(self, edge: Tuple[int, int]):
        '''
        Deletes the undirected edge (u, v) from the graph.
        Raises ValueError if the edge is not present in both directions.
        '''
        u, v = edge
        self.check_vertices_exist(edge)
        if not (v in self._adjacency_list[u] and u in self._adjacency_list[v]):
            raise ValueError(f"Edge {edge} is not present in the graph.")
        else:
            self._adjacency_list[u].remove(v)
            self._adjacency_list[v].remove(u)
    
    def get_adjacent_vertices(self, v: int):
        if self.has_vertex(v):
            return self._adjacency_list[v]
        else:
            raise ValueError("Vertex {v} not found.")

    
    def check_vertices_exist(self, edge: Tuple[int, int]):
        u, v = edge
        if not self.has_vertex(u):
            raise ValueError(f"Graph does not have vertex {u}")
        elif not self.has_vertex(v):
            raise ValueError(f"Graph does not have vertex {v}")
    
    def __contains__(self, edge: Tuple[int, int]):
        u, v = edge
        self.check_vertices_exist(edge)
        return v in self._adjacency_list[u] and u in self._adjacency_list[v]
    
    def has_vertex(self, vertex: int):
        return vertex in self._adjacency_list

    
    def print_adjacency_list(self):
        '''
        Prints the internal adjacency list representation of the graph.
        '''
        for vertex in self._adjacency_list:
            edges = self._adjacency_list[vertex]
            print(f"Vertex #{vertex:4} has edge(s) to vertices {[x for x in edges]}")
    
    def print_adjacency_matrix(self):
        '''
        Constructs and then prints an adjacency matrix form of the graph.
        '''
        size = len(self._adjacency_list)
        matrix = [
            [False for _ in range(size)] for _ in range(size)
        ]
        for vertex in self._adjacency_list:
            for other_vertex in self._adjacency_list[vertex]:
                matrix[vertex][other_vertex] = True
                matrix[other_vertex][vertex] = True
        
        print_matrix(matrix)



if __name__ == "__main__":    
    g = Graph(list(range(6)), [])
    g.add_edge((1, 5))
    g.add_edge((2, 3))
    g.add_edge((4, 1))
    g.add_edge((0, 3))
    g.print_adjacency_list()
    g.print_adjacency_matrix()
