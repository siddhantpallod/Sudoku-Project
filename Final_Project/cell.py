import pygame.font
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False
        self.editable = True

    def set_cell_value(self):
        self.value = self.sketched_value
        self.sketched_value = None

    def set_sketched_value(self, value):
        self.sketched_value = value
        sketch_surface = pygame.font.Font(None, 40).render(str(value), True, (86, 92, 102))
        sketch_rectangle = sketch_surface.get_rect(center=((SQUARE_SIZE * self.row) + SQUARE_SIZE // 2,(SQUARE_SIZE * self.col) + SQUARE_SIZE // 2))
        self.screen.blit(sketch_surface, sketch_rectangle)

    def draw(self):
        if self.value != 0:
            num_surface = pygame.font.Font(None, 80).render(str(self.value), True, WHITE)
            num_rectangle = num_surface.get_rect(center=((SQUARE_SIZE * self.row) + SQUARE_SIZE // 2, (SQUARE_SIZE * self.col) + SQUARE_SIZE // 2))
            self.screen.blit(num_surface, num_rectangle)

        if self.selected:
            red_square = pygame.Rect(SQUARE_SIZE * self.row, SQUARE_SIZE * self.col, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(self.screen, (255, 0, 0), red_square, 2)
            self.selected = False

        if self.sketched_value:
            sketch_surface = pygame.font.Font(None, 40).render(str(self.sketched_value), True, (86, 92, 102))
            sketch_rectangle = sketch_surface.get_rect(center=((SQUARE_SIZE * self.row) + SQUARE_SIZE // 2,(SQUARE_SIZE * self.col) + SQUARE_SIZE // 2))
            self.screen.blit(sketch_surface, sketch_rectangle)