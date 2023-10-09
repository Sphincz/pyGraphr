import numpy as np
import pygame
import pygame_gui
from pygame_gui.core import ObjectID

from algorithms import Algorithms
from gui.color_legend import ColorLegend
from gui.heuristics_table import HeuristicsTable
from node import Node
from search_visualizer import SearchVisualizer
from utils.colors import Color
from utils.hierarchy_network import hierarchy_pos


class GUIManager:
    def __init__(self, graph):
        self.found_path = None
        self.visit_order = None
        self.graph = graph
        self.animation_completed = False

        # Ajustar se necessario
        self.window_size = (1280, 720)
        self.graph_margin = 150
        self.animation_speed = 50
        self.legend_margin_left = 100
        self.heuristics_margin_left = 10
        self.heuristics_margin_top = 75
        self.node_radius = 20
        self.background_color = Color.WHITE.value
        self.node_color = Color.BLUE.value

        # Inicializar motor
        self.algorithms = Algorithms(self.graph)
        self.visualizer = SearchVisualizer(self.graph)
        self.heuristics_table = HeuristicsTable((self.heuristics_margin_left, self.heuristics_margin_top), graph)

        self.screen = pygame.display.set_mode(self.window_size)
        self.color_legend = ColorLegend(self.legend_margin_left, self.window_size[1] - 40)
        self.manager = pygame_gui.UIManager(self.window_size, './gui/theme.json')
        self.nodes = {name: Node(name, pos) for name, pos in hierarchy_pos(self.graph.nx_graph).items()}

        # UI elements configs
        space_between_elements = 10
        center_group_width = 60 + space_between_elements + 200 + space_between_elements + 50
        right_group_width = 100 + space_between_elements + 100
        left_start_x = space_between_elements
        center_start_x = (self.window_size[0] - center_group_width) // 2
        right_start_x = self.window_size[0] - right_group_width - space_between_elements

        # Begin button
        self.begin_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((left_start_x, 10), (100, 40)),
            text='Begin',
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#button-label'),
        )
        left_start_x += 100 + space_between_elements

        # Dropdown menu for algorithm choice
        self.algorithm_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=self.algorithms.designations,
            starting_option=self.algorithms.designations[0],
            relative_rect=pygame.Rect((left_start_x, 10), (200, 40)),
            manager=self.manager
        )

        # Speed label
        self.speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((center_start_x, 10), (60, 40)),
            text='Speed:',
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#speed-label'),
        )
        center_start_x += 60 + space_between_elements

        # Speed slider
        self.speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((center_start_x, 10), (200, 40)),
            start_value=self.animation_speed,
            value_range=(0, 100),
            manager=self.manager,
        )
        center_start_x += 180 + space_between_elements

        # Speed value label
        self.slider_value_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((center_start_x, 10), (50, 40)),
            text=str(self.animation_speed),  # Start with initial speed value
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#speed-label'),
        )

        # Reset button
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((right_start_x, 10), (100, 40)),
            text='Reset',
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#button-label'),
        )
        right_start_x += 100 + space_between_elements

        # Exit button
        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((right_start_x, 10), (100, 40)),
            text='Exit',
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#button-label'),
        )

        # Info toggle heuristics table
        self.heuristics_table_info_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((5, 50), (300, 30)),
            text="Click 'H' key to toggle heuristics table",
            manager=self.manager,
            object_id=ObjectID(class_id=None, object_id='#normal-label')
        )

        self.create_nodes()

    def process_events(self, event):
        if event.type == pygame.USEREVENT:
            # For buttons
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == self.begin_button:
                    selected_algorithm = self.algorithm_dropdown.selected_option
                    print("[ALGO] Begin search for search algorithm:", selected_algorithm)
                    self.visit_order, self.found_path = self.algorithms.perform_search(selected_algorithm,
                                                                                       self.graph.start_node,
                                                                                       self.graph.end_node)

                elif event.ui_element == self.reset_button:
                    print("[ALGO] Graph search reset!")
                    self.visualizer.clear_visited_nodes()  # Clear visited nodes
                    if hasattr(self, 'visit_order'):
                        self.visit_order = []  # Reset visit_order
                        self.animation_completed = False  # Reset animation completed flag

                elif event.ui_element == self.exit_button:
                    pygame.quit()
                    print("[ROOT] pyGraphr exited.")
                    exit()

            # For the speed slider
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.speed_slider:
                    self.animation_speed = int(self.speed_slider.get_current_value())
                    self.slider_value_label.set_text(str(self.animation_speed))

        # For the heuristics table
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Press 'h' to toggle heuristics table
                self.heuristics_table.show = not self.heuristics_table.show

        self.manager.process_events(event)

    def update(self, time_delta):
        self.manager.update(time_delta)

        # Logic to move nodes to visit_order for animation
        if hasattr(self, 'visit_order') and self.visit_order:
            pygame.time.wait(1000 - (self.animation_speed * 10))
            next_node_name = self.visit_order.pop(0)
            self.visualizer.add_visited_node(next_node_name)
            self.nodes[next_node_name].set_order(len(self.visualizer.visited_nodes) + 1)

            if len(self.visit_order) == 0:
                self.animation_completed = True

    def draw(self):
        self.screen.fill(self.background_color)

        # Drawing edges with arrowheads
        for edge in self.graph.nx_graph.edges:
            p1 = np.array(self.nodes[edge[0]].pos, dtype=float)
            p2 = np.array(self.nodes[edge[1]].pos, dtype=float)

            # Normalize the direction
            direction = p2 - p1
            direction /= np.linalg.norm(direction)

            # Perpendicular vector
            perp_vector = np.array([-direction[1], direction[0]])

            # Offset the arrow tip from the destination node (node circle's edge)
            p2_arrow = p2 - self.node_radius * direction

            arrow_size = 15
            left = p2_arrow - arrow_size * (direction * 0.5 + perp_vector * 0.7)
            right = p2_arrow - arrow_size * (direction * 0.5 - perp_vector * 0.7)

            pygame.draw.line(self.screen, Color.BLACK.value, p1, p2_arrow, 2)
            pygame.draw.line(self.screen, Color.BLACK.value, p2_arrow, left, 2)
            pygame.draw.line(self.screen, Color.BLACK.value, p2_arrow, right, 2)

            # Compute midpoint for rendering edge weight
            midpoint = (p1 + p2) / 2

            # Get the edge's weight
            edge_weight = self.graph.nx_graph[edge[0]][edge[1]].get('weight', 0)

            # Render the edge weight at the midpoint
            font = pygame.font.SysFont("Tahoma", 16)
            weight_text = font.render(str(edge_weight), True, Color.BLACK.value)
            # Create a new surface with dimensions expanded by padding
            bg_padding = 3
            padded_surface = pygame.Surface((weight_text.get_width() + 2 * bg_padding,
                                             weight_text.get_height() + 2 * bg_padding))
            padded_surface.fill(Color.WHITE.value)
            padded_surface.blit(weight_text, (bg_padding, bg_padding))
            # Compute the midpoint for the padded surface
            text_rect = padded_surface.get_rect(center=(midpoint[0], midpoint[1]))
            self.screen.blit(padded_surface, text_rect.topleft)

            # Drawing nodes
            for node_name, node in self.nodes.items():
                node.color = self.node_color
                # Setting node colors and order based on its state
                if node_name == self.graph.start_node:
                    node.set_color(Color.BLACK.value)
                elif node_name == self.graph.end_node:
                    node.set_color(Color.RED.value)

                if node_name in self.visualizer.visited_nodes:
                    node.set_color(Color.GREEN.value)

                if self.found_path and node_name in self.found_path and self.animation_completed:
                    node.set_color(Color.YELLOW.value)

                node.draw(self.screen)

        # Repaint and update UI elements after graph was drawn
        self.manager.draw_ui(self.screen)
        self.color_legend.draw(self.screen)
        self.heuristics_table.draw(self.screen)
        pygame.display.flip()

    def create_nodes(self):
        """Initialize Node objects based on the graph's nodes."""
        pos = hierarchy_pos(self.graph.nx_graph)

        # Scaling positions to fit within the window
        min_x = min([coords[0] for coords in pos.values()])
        max_x = max([coords[0] for coords in pos.values()])
        min_y = min([coords[1] for coords in pos.values()])
        max_y = max([coords[1] for coords in pos.values()])

        x_scale = (self.window_size[0] - 2 * self.graph_margin) / (max_x - min_x)
        y_scale = (self.window_size[1] - 2 * self.graph_margin) / (max_y - min_y)

        scaled_pos = {node: (int((coords[0] - min_x) * x_scale + self.graph_margin),
                             self.window_size[1] - int((coords[1] - min_y) * y_scale + self.graph_margin))
                      for node, coords in pos.items()}

        self.nodes = {name: Node(name, pos) for name, pos in scaled_pos.items()}
