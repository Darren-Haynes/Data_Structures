"""An unweighted, directed graph."""
import random
import string

class SimpleGraph(object):
    """Simple Graph Object."""

    def __init__(self):
        """Initiate an empty graph."""
        self.graph = {}

    def add_node(self, val):
        """Add a node to the graph."""
        self.graph.setdefault(val, [])

    def add_edge(self, val, edge):
        """Add value and it's edge."""
        if edge not in self.graph:
            self.add_node(edge)

        if val in self.graph:
            if edge not in self.graph[val]:
                self.graph[val].append(edge)
        else:
            self.graph[val] = [edge]

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
        return tuple(all_edges)

    def del_node(self, val):
        """If node in graph, delete it."""
        try:
            val in self.graph
            for loop_val in self.graph:
                if val in self.graph[loop_val]:
                    self.graph[loop_val].remove(val)
            del self.graph[val]
        except KeyError:
            raise ValueError("Node doesn't exist")

    def del_edge(self, val, edge):
        """Remove connection between node and edge if edge exists."""
        try:
            val in self.graph
            try:
                edge in self.graph[val]
                self.graph[val].remove(edge)
            except ValueError:
                raise ValueError("Edge doesn't exist")
        except KeyError:
            raise ValueError("Node doesn't exist")

    def has_node(self, val):
        """If node exists return True."""
        return val in self.graph

    def neighbors(self, val):
        """Return all edges of a node."""
        if val not in self.graph:
            raise ValueError("Node doesn't exist.")

        return self.graph[val]

    def adjacent(self, val1, val2):
        """Return if one node has edge with the other."""
        if val1 not in self.graph or val2 not in self.graph:
            raise ValueError("Node doesn't exist.")

        return val2 in self.graph[val1] or val1 in self.graph[val2]

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
