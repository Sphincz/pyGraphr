import pygame
from utils.colors import Color
from pygame import gfxdraw


class Node:
    def __init__(self, name, pos=(0,0)):
        self.radius = 20
        self.name = str(name)
        self.pos = pos
        self.color = Color.BLUE.value
        self.exploration_order = None

    def set_color(self, color):
        self.color = color

    def set_order(self, order):
        self.exploration_order = order

    def draw(self, screen):
        # Anti-aliased cirle nodes
        gfxdraw.aacircle(screen, self.pos[0], self.pos[1], self.radius, self.color)
        gfxdraw.filled_circle(screen, self.pos[0], self.pos[1], self.radius, self.color)

        # Draw node name
        font = pygame.font.SysFont('Arial', 15)
        text = font.render(self.name, True, Color.WHITE.value)
        screen.blit(text, (self.pos[0] - 5, self.pos[1] - 10))

        # Draw order if it exists
        if self.exploration_order is not None:
            font = pygame.font.SysFont('Arial', 15)
            order_text = font.render(str(self.exploration_order), True, Color.WHITE.value)
            screen.blit(order_text, (self.pos[0] + self.radius, self.pos[1] - 10))

    def __str__(self):
        return self.name
