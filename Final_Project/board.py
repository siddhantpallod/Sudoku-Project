import pygame
from constants import *
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        self.current = None

    def draw(self):
        for i in range(1, 4):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE_BOLD),(self.width, i * SQUARE_SIZE_BOLD), BOLD_LINE_WIDTH )
        for i in range(1, 3):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE_BOLD, 0),(i * SQUARE_SIZE_BOLD, self.height), BOLD_LINE_WIDTH )
        for i in range(1, 3):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE),(self.width, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(4, 6):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE),(self.width, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(7, 9):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE),(self.width, i * SQUARE_SIZE), LINE_WIDTH)
        for i in range(1, 3):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0),(i * SQUARE_SIZE, self.height), LINE_WIDTH)
        for i in range(4, 6):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0),(i * SQUARE_SIZE, self.height), LINE_WIDTH)
        for i in range(7, 9):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0),(i * SQUARE_SIZE, self.height), LINE_WIDTH)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

    def select(self, row, col):
        self.cells[row][col].selected = True
        self.draw()
        self.current = self.cells[row][col]

    def click(self, x, y):
        if x <= self.width and y <= self.height:
            clicked_row = int(y / 70)
            clicked_col = int(x / 70)
            return clicked_row, clicked_col

        return None

    def sketch(self, value):
        if self.current.editable:
            self.current.set_sketched_value(value)

    def place_number(self):
        if self.current.editable:
            self.current.set_cell_value()

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].editable:
                    self.cells[i][j].value = 0
                    self.cells[i][j].sketched_value = 0

        self.draw()

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return False
        return True

    def check_board(self, board_correct):
        board = [[self.cells[i][j].value for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != board_correct[i][j]:
                    return False
        return True