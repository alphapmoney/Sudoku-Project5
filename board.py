import math
import pygame
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, screen: pygame.surface):
        self.screen = screen

        self.user_sketch = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.selc_mouse_bx = -10
        self.selc_mouse_by = -10
        self.mouse_pos = (0, 0)
        self.mouse_bx = 0
        self.mouse_by = 0
        self.end_game = False
        self.hover_obj = None

        self.sudoku_generator = SudokuGenerator(9, 31)
        self.sudoku_generator.fill_values()
        self.completed_puzzle = self.sudoku_generator.get_board().copy()
        self.sudoku_generator.print_board()

    # FIXME run after screen update
    # FIXME Returns code
    # FIXME 0 = end game
    # FIXME 1 = reset by creating new board and set to home screen
    def event_loop(self):
        t = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = pygame.mouse.get_pos()
                if pygame.Rect((250 - self.reset_button_text.get_width() // 2) - 10,
                               950 - self.reset_button_text.get_height() // 2,
                               self.reset_button_text.get_width() + 20,
                               self.reset_button_text.get_height() + 5).collidepoint(
                    self.mouse_pos):
                    self.hover_obj = 0
                elif pygame.Rect((450 - self.restart_button_text.get_width() // 2) - 10,
                                 950 - self.restart_button_text.get_height() // 2,
                                 self.restart_button_text.get_width() + 20,
                                 self.restart_button_text.get_height() + 5).collidepoint(
                    self.mouse_pos):
                    self.hover_obj = 1
                elif pygame.Rect((650 - self.exit_button_text.get_width() // 2) - 10,
                                 950 - self.exit_button_text.get_height() // 2,
                                 self.exit_button_text.get_width() + 20,
                                 self.exit_button_text.get_height() + 5).collidepoint(
                    self.mouse_pos):
                    self.hover_obj = 2
                else:
                    self.hover_obj = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.hover_obj == 0:
                        self.puzzle = self.puzzle_og
                        self.user_sketch = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        self.puzzle = []
                        for x in range(9):
                            self.puzzle.append([])
                            for y in range(9):
                                self.puzzle[x].append(self.puzzle_og[x][y])
                    elif self.hover_obj == 1:
                        t = 1
                        self.user_sketch = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                    elif self.hover_obj == 2:
                        t = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.selc_mouse_bx = self.mouse_bx
                    self.selc_mouse_by = self.mouse_by
            elif event.type == pygame.KEYUP:
                # Key inputs
                if self.selc_mouse_bx == -10:
                    self.selc_mouse_bx = -1
                    self.selc_mouse_by = -1
                elif event.key == pygame.K_UP and not self.selc_mouse_by + 2 == 1:
                    self.selc_mouse_by -= 1
                elif event.key == pygame.K_DOWN and not self.selc_mouse_by + 2 == 9:
                    self.selc_mouse_by += 1
                if self.selc_mouse_bx == -10:
                    self.selc_mouse_bx = -1
                    self.selc_mouse_by = -1
                elif event.key == pygame.K_LEFT and not self.selc_mouse_bx + 2 == 1:
                    self.selc_mouse_bx -= 1
                elif event.key == pygame.K_RIGHT and not self.selc_mouse_bx + 2 == 9:
                    self.selc_mouse_bx += 1
                if not self.selc_mouse_bx == -10 and not self.selc_mouse_by == -10:
                    if self.puzzle[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] == 0:
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 1
                        elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 2
                        elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 3
                        elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 4
                        elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 5
                        elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 6
                        elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 7
                        elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 8
                        elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 9
                    if not self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] == 0:
                        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                            self.puzzle[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = int(self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1])
                            self.user_sketch[self.selc_mouse_by + 1][self.selc_mouse_bx + 1] = 0

        return t

    def screen_update(self):
        # print(f"{self.selc_mouse_by + 2}, {self.selc_mouse_bx + 2}, {self.puzzle[self.selc_mouse_by + 1][self.selc_mouse_bx + 1]}")
        # Mouse
        self.mouse_bx = max(-2, min((math.floor(self.mouse_pos[0] / 100) - 1), 7))
        self.mouse_by = max(-2, min((math.floor(self.mouse_pos[1] / 100) - 1), 7))
        self.screen.fill((216, 226, 242), pygame.Rect((101 + self.mouse_bx * 100), 8, 99, 886))
        self.screen.fill((216, 226, 242), pygame.Rect(6, (101 + self.mouse_by * 100), 888, 99))

        pygame.draw.lines(self.screen, "grey", True, [(((self.mouse_bx + 2) * 100), ((self.mouse_by + 2) * 100)),
                                                      (((self.mouse_bx + 2) * 100) - 100, ((self.mouse_by + 2) * 100)),
                                                      (((self.mouse_bx + 2) * 100) - 100,
                                                       ((self.mouse_by + 2) * 100) - 100),
                                                      (((self.mouse_bx + 2) * 100), ((self.mouse_by + 2) * 100) - 100)],
                          10)

        pygame.draw.lines(self.screen, "black", True,
                          [(((self.selc_mouse_bx + 2) * 100), ((self.selc_mouse_by + 2) * 100)),
                           (((self.selc_mouse_bx + 2) * 100) - 100, ((self.selc_mouse_by + 2) * 100)),
                           (((self.selc_mouse_bx + 2) * 100) - 100, ((self.selc_mouse_by + 2) * 100) - 100),
                           (((self.selc_mouse_bx + 2) * 100), ((self.selc_mouse_by + 2) * 100) - 100)],
                          10)

        # Grid
        pygame.draw.line(self.screen, "black", (0, 2), (900, 2), 10)  # Top
        pygame.draw.line(self.screen, "black", (0, 898), (900, 898), 10)  # Bottom
        pygame.draw.line(self.screen, "black", (0, 0), (0, 900), 10)  # Left
        pygame.draw.line(self.screen, "black", (900 - 2, 0), (898, 900), 10)  # Right

        # Horizontal lines
        pygame.draw.line(self.screen, "black", (0, 100), (900, 100), 1)
        pygame.draw.line(self.screen, "black", (0, 200), (900, 200), 1)
        pygame.draw.line(self.screen, "black", (0, 300), (900, 300), 10)
        pygame.draw.line(self.screen, "black", (0, 400), (900, 400), 1)
        pygame.draw.line(self.screen, "black", (0, 500), (900, 500), 1)
        pygame.draw.line(self.screen, "black", (0, 600), (900, 600), 10)
        pygame.draw.line(self.screen, "black", (0, 700), (900, 700), 1)
        pygame.draw.line(self.screen, "black", (0, 800), (900, 800), 1)

        # Vertical lines
        pygame.draw.line(self.screen, "black", (100, 0), (100, 900), 1)
        pygame.draw.line(self.screen, "black", (200, 0), (200, 900), 1)
        pygame.draw.line(self.screen, "black", (300, 0), (300, 900), 10)
        pygame.draw.line(self.screen, "black", (400, 0), (400, 900), 1)
        pygame.draw.line(self.screen, "black", (500, 0), (500, 900), 1)
        pygame.draw.line(self.screen, "black", (600, 0), (600, 900), 10)
        pygame.draw.line(self.screen, "black", (700, 0), (700, 900), 1)
        pygame.draw.line(self.screen, "black", (800, 0), (800, 900), 1)

        font = pygame.font.SysFont("comicsansms", 72)

        text = {
            1: font.render("1", True, "Black"),
            2: font.render("2", True, "Black"),
            3: font.render("3", True, "Black"),
            4: font.render("4", True, "Black"),
            5: font.render("5", True, "Black"),
            6: font.render("6", True, "Black"),
            7: font.render("7", True, "Black"),
            8: font.render("8", True, "Black"),
            9: font.render("9", True, "Black"),
            0: None
        }

        sketch_text = {
            1: font.render("1", True, "Grey"),
            2: font.render("2", True, "Grey"),
            3: font.render("3", True, "Grey"),
            4: font.render("4", True, "Grey"),
            5: font.render("5", True, "Grey"),
            6: font.render("6", True, "Grey"),
            7: font.render("7", True, "Grey"),
            8: font.render("8", True, "Grey"),
            9: font.render("9", True, "Grey"),
            0: None
        }

        for x in range(9):
            for y in range(9):
                t = text[self.puzzle[y][x]]
                st = sketch_text[self.user_sketch[y][x]]
                if t is not None:
                    self.screen.blit(t, ((50 + x * 100) - t.get_width() // 2, (50 + y * 100) - t.get_height() // 2))
                if st is not None:
                    self.screen.blit(st, ((50 + x * 100) - st.get_width() // 2, (50 + y * 100) - st.get_height() // 2))

        # buttons
        text_font = pygame.font.SysFont("comicsansms", 32)
        reset_button_text = text_font.render("Reset", True, "Black")
        self.reset_button_text = reset_button_text
        self.screen.fill((200, 200, 200) if self.hover_obj is not 0 else (180, 180, 180),
                         pygame.Rect((250 - reset_button_text.get_width() // 2) - 10,
                                     950 - reset_button_text.get_height() // 2,
                                     reset_button_text.get_width() + 20, reset_button_text.get_height() + 5))
        self.screen.blit(reset_button_text,
                         (250 - reset_button_text.get_width() // 2, 950 - reset_button_text.get_height() // 2))
        restart_button_text = text_font.render("Restart", True, "Black")
        self.restart_button_text = restart_button_text
        self.screen.fill((200, 200, 200) if self.hover_obj is not 1 else (180, 180, 180),
                         pygame.Rect((450 - restart_button_text.get_width() // 2) - 10,
                                     950 - restart_button_text.get_height() // 2,
                                     restart_button_text.get_width() + 20, restart_button_text.get_height() + 5))
        self.screen.blit(restart_button_text,
                         (450 - restart_button_text.get_width() // 2, 950 - restart_button_text.get_height() // 2))
        exit_button_text = text_font.render("Exit", True, "Black")
        self.exit_button_text = exit_button_text
        self.screen.fill((200, 200, 200) if self.hover_obj is not 2 else (180, 180, 180),
                         pygame.Rect((650 - exit_button_text.get_width() // 2) - 10,
                                     950 - exit_button_text.get_height() // 2,
                                     exit_button_text.get_width() + 20, exit_button_text.get_height() + 5))
        self.screen.blit(exit_button_text,
                         (650 - exit_button_text.get_width() // 2, 950 - exit_button_text.get_height() // 2))

    def is_board_filled(self):
        for x in range(9):
            for y in range(9):
                if self.puzzle[x][y] == 0:
                    return False
        return True

    def is_board_correct(self):
        if self.is_board_filled():
            i = 81
            for x in range(9):
                for y in range(9):
                    if not (int(self.puzzle[x][y]) == int(self.completed_puzzle[x][y])):
                        i -= 1
                        print(i)
                        print(f"{self.puzzle[x][y]} == {self.completed_puzzle[x][y]}")
            return i == 81
        else:
            return False

    def remove_cells(self, num_removed_cells):
        self.sudoku_generator.removed_cells = num_removed_cells
        self.sudoku_generator.remove_cells()
        # self.puzzle = self.sudoku_generator.get_board()
        self.puzzle = []
        for x in range(9):
            self.puzzle.append([])
            for y in range(9):
                self.puzzle[x].append(self.sudoku_generator.get_board()[x][y])
        self.puzzle_og = []
        for x in range(9):
            self.puzzle_og.append([])
            for y in range(9):
                self.puzzle_og[x].append(self.sudoku_generator.get_board()[x][y])