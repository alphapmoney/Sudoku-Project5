import pygame.draw

import sudoku_generator
from cell import Cell

from sudoku_generator import SudokuGenerator
import copy

pygame.font.init()


class Board:
    button_font = pygame.font.Font(None, 35)
    reset_button = button_font.render("Reset", True, (255, 255, 255))
    restart_button = button_font.render("Restart", True, (255, 255, 255))
    exit_button = button_font.render("Exit", True, (255, 255, 255))

    reset_button_rect = pygame.Rect(64, 620, 90, 50)
    restart_button_rect = pygame.Rect(240, 620, 120, 50)
    exit_button_rect = pygame.Rect(446, 620, 90, 50)

    def __init__(self, screen, difficulty):
        self.cells = []
        self.sudoku = SudokuGenerator(9, difficulty)
        self.sudoku.fill_values()
        self.complete_board = [row[:] for row in self.sudoku.get_board()]
        self.sudoku.remove_cells()
        self.board = self.sudoku.get_board()
        self.screen = screen
        self.selected_cell = None
        self.cell_size = 66

        for row in range(9):
            self.cells.append([])
            for col in range(9):
                self.cells[row].append(Cell(self.board[row][col], row, col, screen, self.cell_size))

    def draw(self, reset_s, restart_s, exit_s):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col] == self.selected_cell:
                    self.cells[row][col].draw(True, False)
                else:
                    self.cells[row][col].draw(False, False)

        # Draw thicker lines
        for i in range(0, (9 * self.cell_size) + 1, self.cell_size):
            thickness = 5 if i % (3 * self.cell_size) == 0 else 1

            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, 9 * self.cell_size), thickness)

            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (9 * self.cell_size, i), thickness)

        self.draw_options(reset_s, restart_s, exit_s)

    def draw_options(self, reset_s=False, restart_s=False, exit_s=False):
        if reset_s:
            pygame.draw.rect(self.screen, (196, 98, 16), self.reset_button_rect)
        else:
            pygame.draw.rect(self.screen, (255, 140, 0), self.reset_button_rect)

        if restart_s:
            pygame.draw.rect(self.screen, (196, 98, 16), self.restart_button_rect)
        else:
            pygame.draw.rect(self.screen, (255, 140, 0), self.restart_button_rect)

        if exit_s:
            pygame.draw.rect(self.screen, (196, 98, 16), self.exit_button_rect)
        else:
            pygame.draw.rect(self.screen, (255, 140, 0), self.exit_button_rect)

        self.screen.blit(self.reset_button, (75, 632))
        self.screen.blit(self.restart_button, (259, 632))
        self.screen.blit(self.exit_button, (465, 632))

    def cell_clicked(self, pos):
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        if 0 <= row <= 8 and 0 <= col <= 8:
            self.selected_cell = self.cells[row][col]
            self.selected_cell.draw(True, False)
            print(self.selected_cell.row, self.selected_cell.col)
        else:
            self.selected_cell = None

    def set_cell_sketched_value(self, value):
        self.selected_cell.set_cell_sketched_value(value)

    def set_cell_value(self, value):
        self.selected_cell.set_cell_value(value)

    def is_full(self):
        count = 0
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    count += 1
        if count == 0:
            return True
        else:
            return False

    def check_win(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value != self.complete_board[row][col]:
                    return False
        return True

    def reset(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].locked = False
                self.cells[row][col].set_cell_reset(self.board[row][col])

    # Check what cell is being hovered on
    def hover(self, x, y):
        row = y // self.cell_size
        col = x // self.cell_size
        if 0 <= row <= 8 and 0 <= col <= 8:
            self.cells[row][col].draw(False, True)
        else:
            self.selected_cell = None
