import pygame
import sys
from game import Board
import sudoku_generator as sg


def draw_game_start(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    title = title_font.render("Sudoku", True, (255, 140, 0))
    easy_button = button_font.render("Easy", True, (255, 255, 255))
    medium_button = button_font.render("Medium", True, (255, 255, 255))
    hard_button = button_font.render("Hard", True, (255, 255, 255))

    easy_button_rect = pygame.Rect(67, 500, 100, 50)
    medium_button_rect = pygame.Rect(229, 500, 150, 50)
    hard_button_rect = pygame.Rect(441, 500, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_button_rect.collidepoint(event.pos):
                    print("Easy")
                    return 30
                elif medium_button_rect.collidepoint(event.pos):
                    print("Medium")
                    return 40
                elif hard_button_rect.collidepoint(event.pos):
                    print("Hard")
                    return 50

        screen.fill((255, 255, 255))
        screen.blit(title, (175, 200))
        pygame.draw.rect(screen, (255, 140, 0), easy_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), medium_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), hard_button_rect)

        mouse = pygame.mouse.get_pos()
        if easy_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), easy_button_rect)
            # Also makes cursor a pointer
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif medium_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), medium_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif hard_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), hard_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        screen.blit(easy_button, (75, 508))
        screen.blit(medium_button, (240, 508))
        screen.blit(hard_button, (450, 508))

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((597, 700))

    difficulty = draw_game_start(screen)



    sudoku_board = Board(600, 700, screen, difficulty)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if y > 600:
                    if sudoku_board.reset_button_rect.collidepoint(event.pos):
                        print("Reset")
                    elif sudoku_board.restart_button_rect.collidepoint(event.pos):
                        print("Restart")
                    elif sudoku_board.exit_button_rect.collidepoint(event.pos):
                        print("Exit")
                else:
                    sudoku_board.cell_clicked(event.pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                sudoku_board.set_cell_sketched_value(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                sudoku_board.set_cell_sketched_value(2)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                sudoku_board.set_cell_sketched_value(3)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                sudoku_board.set_cell_sketched_value(4)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                sudoku_board.set_cell_sketched_value(5)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                sudoku_board.set_cell_sketched_value(6)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                sudoku_board.set_cell_sketched_value(7)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                sudoku_board.set_cell_sketched_value(8)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                sudoku_board.set_cell_sketched_value(9)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                sudoku_board.set_cell_sketched_value(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                sudoku_board.set_cell_value(sudoku_board.selected_cell.sketched_value)
                sudoku_board.set_cell_sketched_value(0)

        screen.fill((255, 255, 255))
        x, y = pygame.mouse.get_pos()
        if sudoku_board.reset_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            sudoku_board.draw(True, False, False)
        elif sudoku_board.restart_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            sudoku_board.draw(False, True, False)
        elif sudoku_board.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            sudoku_board.draw(False, False, True)
        elif y < 600 and 0 <= x <= screen.get_width():
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            sudoku_board.draw(False, False, False)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            sudoku_board.draw(False, False, False)

        if sudoku_board.is_full():
            print("You win!")
            # OK BRENDAN DO THIS PART BIG BOY!
        pygame.display.update()

