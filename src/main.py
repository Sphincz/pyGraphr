import pygame
from gui.gui_manager import GUIManager
from graph import Graph


class PyGraphr:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pyGraphr - A Python Graph Traversal Visualizer')

        # Load graph data
        self.graph_path = "./graphs/graph_dict.txt"
        self.graph = Graph(self.graph_path)

        # Initialize the GUI Manager
        self.gui_manager = GUIManager(self.graph)

    def run(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                self.gui_manager.process_events(event)

            self.gui_manager.update(time_delta)
            self.gui_manager.draw()

            pygame.display.flip()


if __name__ == '__main__':
    app = PyGraphr()
    app.run()