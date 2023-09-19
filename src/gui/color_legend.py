import pygame

from utils.colors import Color


class ColorLegend:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colors = [
            {"color": Color.BLACK.value, "label": "Initial node"},
            {"color": Color.RED.value, "label": "Goal node"},
            {"color": Color.BLUE.value, "label": "Unvisited node"},
            {"color": Color.GREEN.value, "label": "Visited node"},
            {"color": Color.YELLOW.value, "label": "Path node"}
        ]
        self.font = pygame.font.SysFont('Tahoma', 12)

    def draw(self, screen):
        initial_x = self.x
        for color_info in self.colors:
            pygame.draw.rect(screen, color_info["color"], (initial_x, self.y - 2, 20, 20))
            text = self.font.render(color_info["label"], True, Color.BLACK.value)
            screen.blit(text, (initial_x + 25, self.y))
            initial_x += 250  # Change this to adjust space between legend items
