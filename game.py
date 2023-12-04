import pygame.draw
from cell import Cell

from sudoku_generator import SudokuGenerator
import copy


class Board:
    cells = []

    def __init__(self, width, height, screen, difficulty):
        sudoku = SudokuGenerator(9, difficulty)
        sudoku.fill_values()
        self.completed = sudoku.get_board()
        self.board = sudoku.remove_cells()
        self.screen = screen
        self.selected_cell = None
        self.cell_size = 66

        for row in range(9):
            self.cells.append([])
            for col in range(9):
                self.cells[row].append(Cell(self.board[row][col], row, col, screen))

    def draw(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col] == self.selected_cell:
                    self.cells[row][col].draw(True)
                else:
                    self.cells[row][col].draw(False)

        # Draw thicker lines
        for i in range(0, (9 * self.cell_size) + 1, self.cell_size):
            thickness = 5 if i % (3 * self.cell_size) == 0 else 1

            pygame.draw.line(self.screen, (0, 0, 0), (i, 0), (i, 9 * self.cell_size), thickness)

            pygame.draw.line(self.screen, (0, 0, 0), (0, i), (9 * self.cell_size, i), thickness)

    def cell_clicked(self, pos):
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        self.selected_cell = self.cells[row][col]
        self.selected_cell.draw(True)
        print(self.selected_cell.row, self.selected_cell.col)

    def set_cell_sketched_value(self, value):
        self.selected_cell.set_cell_sketched_value(value)

    def set_cell_value(self, value):
        self.selected_cell.set_cell_value(value)













        # next_length = 0
        # start = (0, 0)
        # end = (0, 602)
        # for col in range(10):
        #     if col % 3 == 0:
        #         pygame.draw.line(self.screen, (0, 0, 0), start, end, 5)
        #         start = (start[0] + 70, 0)
        #         end = (end[0] + 70, 602)
        #     else:
        #         pygame.draw.line(self.screen, (0, 0, 0), start, end, 1)
        #         start = (start[0] + 65, 0)
        #         end = (end[0] + 65, 602)
        #
        # start = (0, 0)
        # end = (602, 0)
        #
        # for col in range(10):
        #     if col % 3 == 0:
        #         pygame.draw.line(self.screen, (0, 0, 0), start, end, 5)
        #         start = (0, start[1] + 70)
        #         end = (602, end[1] + 70)
        #     else:
        #         pygame.draw.line(self.screen, (0, 0, 0), start, end, 1)
        #         start = (0, start[1] + 65)
        #         end = (602, end[1] + 65)




