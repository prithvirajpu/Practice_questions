from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}   # stores nodes and their connections

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        # Undirected graph → both ways connection
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def show(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return

        # Remove this vertex from all its neighbors
        for neighbor in self.adj_list[vertex]:
            self.adj_list[neighbor] = [
                v for v in self.adj_list[neighbor] if v != vertex
            ]

        # Finally, delete the vertex itself
        del self.adj_list[vertex]

    # -----------------
    # BFS Traversal
    # -----------------
    def bfs(self,val):
        visited=set()
        result=[]
        visited.add(val)
        queue=[val]
        while queue:
            vertex=queue.pop(0)
            result.append(vertex)
            for i in self.adj_list[vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return result
        
        
    # -----------------
    # DFS Traversal (iterative)
    # -----------------
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        visited.add(start)

        while stack:
            vertex = stack.pop()
            result.append(vertex)
            for n in self.adj_list[vertex]:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        return result
    
    
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print("Before removal:")
g.show()

print("\nBFS from A:", g.bfs("A"))
print("DFS from A:", g.dfs("A"))

g.remove_vertex("A")

print("\nAfter removal of A:")
g.show()

print("\nBFS from B:", g.bfs("B"))
print("DFS from B:", g.dfs("B"))
