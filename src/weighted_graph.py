"""An unweighted, directed graph."""
from collections import OrderedDict
import random
import string

class WeightedGraph(object):
    """Simple Graph Object."""

    def __init__(self):
        """Initiate an empty graph."""
        self.graph = OrderedDict()

    def add_node(self, val):
        """Add a node to the graph."""
        self.graph.setdefault(val, {})

    def add_edge(self, val, edge, weight):
        """Add value and it's edge."""
        if val == edge:
            raise ValueError("Nodes cannot be self referential.")

        if not isinstance(weight, (float, int)):
            raise ValueError("Weight must be a number")

        if val not in self.graph:
            self.add_node(val)

        if edge not in self.graph:
            self.add_node(edge)

        if val in self.graph:
            if edge not in self.graph[val]:
                self.graph[val][edge] = weight
        else:
            self.graph[val][edge] = weight

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
                try:
                    self.graph[loop_val][val]
                    del self.graph[loop_val][val]
                except KeyError:
                    pass
            del self.graph[val]
        except KeyError:
            raise ValueError("Node doesn't exist")

    def del_edge(self, val, edge):
        """Remove connection between node and edge if edge exists."""
        try:
            val in self.graph
            try:
                self.graph[val] == edge
                del self.graph[edge]
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

        edges = []
        for edge in self.graph[val]:
            edges.append(tuple(edge)[0])
        return edges

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
                weight = random.randint(0, 100)
            self.add_edge(node, edge, weight)

    def traversal_keyerror(self, start_val):
        """If value not in graph return ValueError."""
        if start_val not in self.graph:
            raise ValueError("Node doesn't exist")

    def breadth_first_traversal(self, start_val):
        """Return full breadth first traversal path."""
        self.traversal_keyerror(start_val)

        if not self.graph[start_val]:
            return [start_val]

        walked = []
        keep_walking = [start_val]
        while keep_walking:
            node = keep_walking[0]
            if node not in walked:
                walked.append(node)
                del keep_walking[0]
                for edge in self.graph[node]:
                    if edge not in walked and edge not in keep_walking:
                        keep_walking.append(edge)
        return walked

    def depth_first_traversal(self, start_val):
        """Return depth first graph travesal."""
        if not self.graph[start_val]:
            return [start_val]

        self.traversal_keyerror(start_val)
        walked = []
        keep_walking = [start_val]
        while keep_walking:
            node = keep_walking[0]
            if node not in walked:
                walked.append(node)
                del keep_walking[0]
                edges = []
                for edge in self.graph[node]:
                    edges.append(edge[0])
                for edge in reversed(edges):
                    if edge not in walked and edge not in keep_walking:
                        keep_walking.insert(0, edge)
        return walked


if __name__ == '__main__':
    import time
    print("\nCOMPARE BREADTH VS DEPTH TRAVERSAL\n")
    for i in range(5):
        g = WeightedGraph()
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
