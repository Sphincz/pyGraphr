import pygame

from utils.colors import Color


class HeuristicsTable:
    def __init__(self, position, graph):
        self.position = position
        self.graph = graph
        self.show = False

    def draw(self, screen):
        if not self.show:
            return

        x, y = self.position
        rect_width, rect_height = 100, 25

        # Header
        pygame.draw.rect(screen, Color.WHITE.value, (x, y, rect_width, rect_height))
        screen.blit(pygame.font.SysFont("Tahoma", 13, bold=True).render("Heuristics", True, Color.BLACK.value), (x + 3, y + 10))

        # Display each node and its heuristic
        for idx, node in enumerate(self.graph.nodes.values()):
            pygame.draw.rect(screen, Color.WHITE.value, (x, y + (idx + 1) * rect_height, rect_width, rect_height))
            text = f"{node.name}: {node.heuristic}"
            screen.blit(pygame.font.SysFont("Tahoma", 13).render(text, True, Color.BLACK.value),
                        (x + 5, y + 10 + (idx + 1) * rect_height))
