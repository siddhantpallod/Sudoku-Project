import pygame
import sys

from board import Board
from constants import *
from sudoku_generator import *


def draw_game_start(screen):
    screen.fill(BLACK)
    image = pygame.image.load('image.webp')
    img_res = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_res, (0, 0))

    title_surface = pygame.font.Font(None, 80).render("Welcome to Sudoku", True, (255, 0, 255))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    game_mode_surface = pygame.font.Font(None, 70).render("Select Game Mode", True, (255, 0, 255))
    game_mode_rectangle = game_mode_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))
    screen.blit(game_mode_surface, game_mode_rectangle)

    easy_text = pygame.font.Font(None, 20).render("EASY", True, BLACK)
    medium_text = pygame.font.Font(None, 20).render("MEDIUM", True, BLACK)
    hard_text = pygame.font.Font(None, 20).render("HARD", True, BLACK)

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 50, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (27, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 50, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (27, 10))

    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 120))
    medium_rectangle = medium_surface.get_rect(center=(2 * (WIDTH // 4), HEIGHT // 2 + 120))
    hard_rectangle = hard_surface.get_rect(center=(3 * (WIDTH // 4), HEIGHT // 2 + 120))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(e.pos):
                    return "easy"
                elif medium_rectangle.collidepoint(e.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(e.pos):
                    return "hard"
        pygame.display.update()


def draw_game_win(screen):
    screen.fill(BLACK)
    image = pygame.image.load('image.webp')
    img_res = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_res, (0, 0))

    win_surface = pygame.font.Font(None, 80).render("Game Won!", True, (255, 0, 255))
    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)

    win_text = pygame.font.Font(None, 20).render("EXIT", True, BLACK)

    win_surface = pygame.Surface((win_text.get_size()[0] + 20, win_text.get_size()[1] + 20))
    win_surface.fill(LINE_COLOR)
    win_surface.blit(win_text, (10, 10))

    win_rectangle = win_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    screen.blit(win_surface, win_rectangle)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if win_rectangle.collidepoint(e.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_lose(screen):
    screen.fill(BLACK)
    image = pygame.image.load('image.webp')
    img_res = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_res, (0, 0))

    lose_surface = pygame.font.Font(None, 80).render("Game Over :(", True, (255, 0, 255))
    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(lose_surface, lose_rectangle)

    restart_text = pygame.font.Font(None, 20).render("RESTART", True, BLACK)
    lose_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    lose_surface.fill(LINE_COLOR)
    lose_surface.blit(restart_text, (10, 10))

    lose_rectangle = lose_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
    screen.blit(lose_surface, lose_rectangle)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if lose_rectangle.collidepoint(e.pos):
                    main()
        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty = draw_game_start(screen)
    screen.fill(BG_GAME_COLOR)
    removed = 0
    if difficulty == "easy":
        removed = 30
    elif difficulty == "medium":
        removed = 40
    elif difficulty == "hard":
        removed = 50
    sudoku = SudokuGenerator(9, removed)
    sudoku.fill_values()
    board_complete = sudoku.get_board()
    sudoku.remove_cells()
    board_blank = sudoku.get_board()
    display_board = Board(WIDTH - 20, HEIGHT - 20, screen, removed)

    for i in range(9):
        for j in range(9):
            display_board.cells[i][j].value = board_blank[i][j]
            if display_board.cells[i][j].value != 0:
                display_board.cells[i][j].editable = False

    display_board.draw()

    reset_text = pygame.font.Font(None, 20).render("RESET", True, BLACK)
    restart_text = pygame.font.Font(None, 20).render("RESTART", True, BLACK)
    exit_text = pygame.font.Font(None, 20).render("EXIT", True, BLACK)

    reset_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (27, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (27, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 316))
    restart_rectangle = restart_surface.get_rect(center=(2 * (WIDTH // 4), HEIGHT // 2 + 316))
    exit_rectangle = exit_surface.get_rect(center=(3 * (WIDTH // 4), HEIGHT // 2 + 316))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    clicked_row = 0
    clicked_col = 0

    while True:
        if display_board.is_full():
            print("board full")

            if display_board.check_board(board_complete):
                draw_game_win(screen)
            else:
                draw_game_lose(screen)

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.pos[1] <= 630:
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    clicked_row, clicked_col = display_board.click(e.pos[1], e.pos[0])

                    display_board.select(clicked_row, clicked_col)
                elif reset_rectangle.collidepoint(e.pos):
                    screen.fill(BG_GAME_COLOR)
                    display_board.reset_to_original()
                elif restart_rectangle.collidepoint(e.pos):
                    main()
                elif exit_rectangle.collidepoint(e.pos):
                    sys.exit()
            if e.type == pygame.KEYDOWN:
                input_value = None
                if e.key == pygame.K_RETURN:
                    input_value = 0
                elif e.key == pygame.K_1:
                    input_value = 1
                elif e.key == pygame.K_2:
                    input_value = 2
                elif e.key == pygame.K_3:
                    input_value = 3
                elif e.key == pygame.K_4:
                    input_value = 4
                elif e.key == pygame.K_5:
                    input_value = 5
                elif e.key == pygame.K_6:
                    input_value = 6
                elif e.key == pygame.K_7:
                    input_value = 7
                elif e.key == pygame.K_8:
                    input_value = 8
                elif e.key == pygame.K_9:
                    input_value = 9
                elif e.key == pygame.K_UP:
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_value = 11
                    if clicked_col - 1 >= 0:
                        clicked_col -= 1
                        display_board.select(clicked_row, clicked_col)
                elif e.key == pygame.K_DOWN:
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_value = 11
                    if clicked_col + 1 <= 8:
                        clicked_col += 1
                        display_board.select(clicked_row, clicked_col)
                elif e.key == pygame.K_LEFT:
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_value = 11
                    if clicked_row - 1 >= 0:
                        clicked_row -= 1
                        display_board.select(clicked_row, clicked_col)
                elif e.key == pygame.K_RIGHT:
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_value = 11
                    if clicked_row + 1 <= 8:
                        clicked_row += 1
                        display_board.select(clicked_row, clicked_col)

                try:
                    if 1 <= input_value <= 9:
                        display_board.sketch(input_value)
                        screen.fill(BG_GAME_COLOR)
                        display_board.sketch(input_value)
                        display_board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                        pygame.display.update()

                    elif input_value == 0:
                        if display_board.current.editable and display_board.current.value:
                            display_board.current.value = 0
                        else:
                            display_board.place_number()
                        screen.fill(BG_GAME_COLOR)
                        display_board.draw()

                except:
                    pass

        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        pygame.display.update()


if __name__ == "__main__":
    main()