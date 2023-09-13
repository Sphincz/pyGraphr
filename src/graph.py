import networkx as nx
import json

from node import Node


class Graph:
    def __init__(self, filename):
        self.nx_graph = nx.DiGraph()
        self.start_node = None
        self.end_node = None
        self.nodes = {}  # Store Node objects keyed by their names
        self._load_from_file(filename)

    def _load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

            # Load nodes and edges
            for node, neighbors in data.items():
                if node not in ["start", "end"]:
                    if node not in self.nodes:
                        # Create a new Node object and store it in the nodes dictionary
                        self.nodes[node] = Node(node)
                    self.nx_graph.add_node(self.nodes[node])

                    for neighbor in neighbors:
                        if neighbor not in self.nodes:
                            self.nodes[neighbor] = Node(neighbor)
                        self.nx_graph.add_edge(self.nodes[node], self.nodes[neighbor])

            # Load start and end nodes
            self.start_node = self.nodes[data["start"]]
            self.end_node = self.nodes[data["end"]]
