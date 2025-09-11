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

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print("Before removal:")
g.show()

g.remove_vertex("A")

print("\nAfter removal of A:")
g.show()

