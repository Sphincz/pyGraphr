class SearchVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.visited_nodes = []

    def add_visited_node(self, node):
        self.visited_nodes.append(node)

    def clear_visited_nodes(self):
        self.visited_nodes.clear()
