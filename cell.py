class Cell:
    def __init__(self, value, row, column, screen):
        self.value = value
        self.row = row
        self.column = column
        

    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched_value = value

