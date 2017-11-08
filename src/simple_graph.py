"""An unweighted, directed graph."""


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
        return all_edges

    def del_node(self, val):
        """If node in graph, delete it."""
        try:
            val in self.graph
            del self.graph[val]
        except KeyError:
            raise KeyError("Node doesn't exist")

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
            print("Node doesn't exist")
