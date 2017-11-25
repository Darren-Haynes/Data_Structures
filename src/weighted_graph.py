"""A weighted, directed graph."""
import random
import string


class SimpleGraph(object):
    """Simple Graph Object."""

    def __init__(self):
        """Initiate an empty graph."""
        self.graph = {}

    def add_node(self, vertex):
        """Add a node to the graph."""
        self.graph.setdefault(vertex, [])

    def add_edge(self, vertex, edge):
        """Add vertex and it's edge."""
        if vertex == edge:
            raise ValueError("Nodes cannot be self referential.")

        if edge not in self.graph:
            self.add_node(edge)

        if vertex in self.graph:
            if edge not in self.graph[vertex]:
                self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

    def nodes(self):
        """Return all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Return all edges in the graph."""
        all_edges = []
        for edges in list(self.graph.values()):
            for edge in edges:
                if edge not in all_edges:
                    all_edges.append(edge)
        return all_edges

    def del_node(self, vertex):
        """If node in graph, delete it and all references to it."""
        try:
            vertex in self.graph
            for loop_vertex in self.graph:
                if vertex in self.graph[loop_vertex]:
                    self.graph[loop_vertex].remove(vertex)
            del self.graph[vertex]
        except KeyError:
            raise KeyError("Node doesn't exist")

    def del_edge(self, vertex, edge):
        """Remove connection between node and edge if edge exists."""
        try:
            vertex in self.graph
            try:
                edge in self.graph[vertex]
                self.graph[vertex].remove(edge)
            except ValueError:
                raise ValueError("Edge doesn't exist")
        except KeyError:
            raise KeyError("Node doesn't exist")

    def has_node(self, vertex):
        """If node exists return True."""
        return vertex in self.graph

    def neighbors(self, vertex):
        """Return all edges of a node."""
        if vertex not in self.graph:
            raise KeyError("Node doesn't exist.")

        return self.graph[vertex]

    def adjacent(self, vertex1, vertex2):
        """Return if one node has edge with the other."""
        if vertex1 not in self.graph or vertex2 not in self.graph:
            raise KeyError("Node doesn't exist.")

        return vertex2 in self.graph[vertex1] or vertex1 in self.graph[vertex2]

    def random_ascii_char(self):
        """Return random upper case ascii char between 'A' and  'J'."""
        return random.choice(string.ascii_uppercase[:10])

    def create_random_graph(self, nodes=20):  # pragma no cover
        """Make a random graph."""
        for i in range(nodes):
            node = self.random_ascii_char()
            edge = node

            while edge == node:
                edge = self.random_ascii_char()
            self.add_edge(node, edge)

    def traversal_keyerror(self, start_vertex):
        """If vertexue not in graph return KeyError."""
        if start_vertex not in self.graph:
            raise KeyError("Node doesn't exist")

    def breadth_first_traversal(self, start_vertex):
        """Return full breadth first traversal path."""
        self.traversal_keyerror(start_vertex)

        if not self.graph[start_vertex]:
            return [start_vertex]

        walked = []
        keep_walking = [start_vertex]
        while keep_walking:
            node = keep_walking[0]
            if node not in walked:
                walked.append(node)
                del keep_walking[0]
                for edge in self.graph[node]:
                    if edge not in walked and edge not in keep_walking:
                        keep_walking.append(edge)
        return walked

    def depth_first_traversal(self, start_vertex):
        """Return depth first graph travesal."""
        if not self.graph[start_vertex]:
            return [start_vertex]

        self.traversal_keyerror(start_vertex)
        walked = []
        keep_walking = [start_vertex]
        while keep_walking:
            node = keep_walking[0]
            if node not in walked:
                walked.append(node)
                del keep_walking[0]
                for edge in reversed(self.graph[node]):
                    if edge not in walked and edge not in keep_walking:
                        keep_walking.insert(0, edge)
        return walked


if __name__ == '__main__':
    import time
    print("\nCOMPARE BREADTH VS DEPTH TRAVERSAL\n")
    for i in range(5):
        g = SimpleGraph()
        g.create_random_graph()

        t0 = time.time()
        breadth = g.breadth_first_traversal('A')
        t1 = time.time()

        t3 = time.time()
        depth = g.depth_first_traversal('A')
        t4 = time.time()

        print("Comparison {}.".format(i + 1))
        print("Breadth traversal: {}".format(breadth))
        print("Depth traversal:   {}".format(depth))
        print("Breadth time = {}".format(t1 - t0))
        print("Depth time =   {}\n".format(t4 - t3))
