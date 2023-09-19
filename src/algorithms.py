class Algorithms:
    def __init__(self, graph):
        self.found_path = []
        self.visit_order = []
        self.graph = graph
        self.designations = ['Profundidade Primeiro', 'Largura Primeiro', 'Greedy BFS', 'A*', 'Dijkstra']

    def dfs(self, start_node, end_node):
        return [], []

    def bfs(self, start_node, end_node):
        return [], []

    def greedy_bfs(self, start_node, end_node):
        return [], []

    def a_star(self, start_node, end_node):
        return [], []

    def dijkstra(self, start_node, end_node):
        return [], []

    def perform_search(self, search_type, start_node, end_node):
        match search_type:
            case "Profundidade Primeiro":
                self.visit_order, self.found_path = self.dfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "Largura Primeiro":
                self.visit_order, self.found_path = self.bfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "Greedy BFS":
                self.visit_order, self.found_path = self.greedy_bfs(start_node, end_node)
                return self.visit_order, self.found_path
            case "A*":
                self.visit_order, self.found_path = self.a_star(start_node, end_node)
                return self.visit_order, self.found_path
            case "Dijkstra":
                self.visit_order, self.found_path = self.dijkstra(start_node, end_node)
                return self.visit_order, self.found_path

