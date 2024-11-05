import pygame
from gui.gui_manager import GUIManager
from graph import Graph
import os

class PyGraphr:
    def __init__(self):
        print("[ROOT] Starting pyGame...")
        pygame.init()
        pygame.display.set_caption('pyGraphr v1.4 - A Python Graph Traversal Visualizer')
        pygame_icon = pygame.image.load('utils/pygraphr-logo.jpeg')
        pygame.display.set_icon(pygame_icon)

        # Load graph data
        self.graph_path = "graphs/graph.txt"
        self.graph = Graph(self.graph_path)

        # Initialize the GUI Manager
        print("[GUI] Starting GUI...")
        self.gui_manager = GUIManager(self.graph)
        print("[GUI] GUI started successfully!")

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


def main():
    os.chdir(os.path.dirname(__file__))
    app = PyGraphr()
    app.run()

if __name__ == '__main__':
    main()
