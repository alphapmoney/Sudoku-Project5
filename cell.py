import pygame


class Cell:
    rect = None
    # Initialize the cell with a value, row, column, screen, and cell size (in pixels)
    def __init__(self, value, row, column, screen, cell_size):
        self.value = value
        self.row = row
        self.col = column
        self.screen = screen
        self.cell_size = cell_size
        self.sketched_value = 0
        self.locked = True if value != 0 else False
    # Set the value of the cell to the given value if the cell is not locked
    def set_cell_value(self, value):
        if self.locked:
            return
        self.value = value
        self.sketched_value = 0
        self.locked = True
    # Reset the cell to the given value
    def set_cell_reset(self, value):
        self.value = value
        self.sketched_value = 0
    # Set the sketched value of the cell to the given value if the cell is not locked
    def set_cell_sketched_value(self, value):
        if self.locked:
            return
        self.sketched_value = value
    # Draw the cell on the screen with the given selected and hover booleans and also a border
    def draw(self, selected, hover):
        color = (0, 0, 0) if not selected else (196,245,255)

        x = self.col * self.cell_size
        y = self.row * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        if hover:
            pygame.draw.rect(self.screen, (220, 220, 220), rect, 0)
        if selected:
            pygame.draw.rect(self.screen, color, rect, 0)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 3)
        else:
            pygame.draw.rect(self.screen, color, rect, 1)

        # Draw the value of the cell if it is not 0
        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
        # Draw the sketched value of the cell if it is not 0
        elif self.value == 0 and self.sketched_value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.sketched_value), True, (150, 150, 150))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
