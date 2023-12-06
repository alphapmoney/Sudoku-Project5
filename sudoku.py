import pygame
from pygame import mixer
from board import Board
import random


class bg_music():
    def __init__(self):
        pygame.mixer.init()
        self.music_sfx = pygame.mixer.Channel(1)
        self.songs = ["music.mp3", "music_medium.mp3", "music_hard.mp3"]

    def play(self, song_index):
        if 0 <= song_index < len(self.songs):
            song = self.songs[song_index]
            music = mixer.Sound(song)
            self.music_sfx.play(music, -1)
            print(f'Playing {song}')
        else:
            print("Invalid song index")

    def quit(self):
        self.music_sfx.stop()

    # def unpause(self):
    # self.music_sfx.unpause()


music_player = bg_music()


def draw_game_start(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    help_button_font = pygame.font.Font(None, 30)

    title = title_font.render("Sudoku", True, (255, 140, 0))
    easy_button = button_font.render("Easy", True, (255, 255, 255))
    medium_button = button_font.render("Medium", True, (255, 255, 255))
    hard_button = button_font.render("Hard", True, (255, 255, 255))
    help_button = help_button_font.render("Help", True, (255, 255, 255))

    easy_button_rect = pygame.Rect(67, 500, 100, 50)
    medium_button_rect = pygame.Rect(229, 500, 150, 50)
    hard_button_rect = pygame.Rect(441, 500, 100, 50)
    help_button_rect = pygame.Rect(270, 610, 60, 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_button_rect.collidepoint(event.pos):
                    print("Easy")
                    music_player.play(0)
                    return 5
                elif medium_button_rect.collidepoint(event.pos):
                    print("Medium")
                    music_player.play(1)
                    return 40
                elif hard_button_rect.collidepoint(event.pos):
                    print("Hard")
                    music_player.play(2)
                    return 50
                elif help_button_rect.collidepoint(event.pos):
                    help_screen(screen)

        screen.fill((255, 255, 255))
        screen.blit(title, (175, 200))
        pygame.draw.rect(screen, (255, 140, 0), easy_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), medium_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), hard_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), help_button_rect)

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
        elif help_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), help_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        screen.blit(easy_button, (75, 508))
        screen.blit(medium_button, (240, 508))
        screen.blit(hard_button, (450, 508))
        screen.blit(help_button, (277, 618))

        pygame.display.update()


def help_screen(screen):
    screen = pygame.display.set_mode((597, 600))
    title_font = pygame.font.Font(None, 60)
    text_font = pygame.font.Font(None, 30)
    button_font = pygame.font.Font(None, 50)

    title = title_font.render("How to play:", True, (255, 140, 0))
    description1 = text_font.render("Click on cell to select it (will be highlighted)", True, (255, 140, 0))
    description2 = text_font.render("Type a number to sketch it in the cell", True, (255, 140, 0))
    description3 = text_font.render("Press enter to confirm the number", True, (255, 140, 0))
    description4 = text_font.render("Press backspace to clear the sketch", True, (255, 140, 0))
    back_button = button_font.render("Back", True, (255, 255, 255))

    back_button_rect = pygame.Rect(250, 442, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button_rect.collidepoint(event.pos):
                    screen = pygame.display.set_mode((597, 700))
                    return

        screen.fill((255, 255, 255))
        screen.blit(title, (175, 100))
        screen.blit(description1, (100, 200))
        screen.blit(description2, (100, 250))
        screen.blit(description3, (100, 300))
        screen.blit(description4, (100, 350))
        pygame.draw.rect(screen, (255, 140, 0), back_button_rect)

        mouse = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), back_button_rect)
            # Also makes cursor a pointer
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        screen.blit(back_button, (258, 450))

        pygame.display.update()


def end_game(screen, win):
    screen.fill((255, 255, 255))
    end_font = pygame.font.Font(None, 100)
    if win:
        win_text = end_font.render("You Win", True, (255, 150, 0))
    else:
        win_text = end_font.render("You Lose", True, (255, 150, 0))

    win_text_rect = win_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    esc_font = pygame.font.Font(None, 36)
    esc = esc_font.render("Press Esc to Exit", True, (255, 150, 0))
    new_game = esc_font.render("Press Enter to Play Again", True, (255, 150, 0))
    esc_text_rect = esc.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    new_game_text_rect = new_game.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 85))
    screen.blit(win_text, win_text_rect)
    screen.blit(esc, esc_text_rect)
    screen.blit(new_game, new_game_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()


def particle_animation(screen):
    RED = [255, 0, 0]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 222, 179]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]

    easter_egg = True if random.randint(1, 10) == 1 else False

    confetti = []

    for i in range(250):
        x = random.randrange(0, 700)
        y = random.randrange(0, 700)
        confetti.append([x, y])
        # confetti contains lists of some coordinates randomly made
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game(0)

        screen.fill((255, 255, 255))
        end_game(screen, True)
        confetti_color = random.choice([RED, ORANGE, YELLOW, GREEN, BLUE])
        if easter_egg:
            imp = pygame.image.load('nahidwin.jpg').convert()
            screen.blit(imp, (0, 0))

        for party in range(len(confetti)):
            pygame.draw.circle(screen, confetti_color, confetti[party], 3)
            confetti[party][1] += 1
            if confetti[party][1] > screen.get_height():  # Adjusted the limit here
                confetti[party][1] = random.randrange(-50, -10)
                confetti[party][0] = random.randrange(0, screen.get_width())

        clock.tick(40)
        pygame.display.update()


test_mode = True


def game(counter):
    game_over = False
    while not game_over:
        pygame.init()

        screen = pygame.display.set_mode((597, 700))
        difficulty = draw_game_start(screen)

        sudoku_board = Board(screen, difficulty)

        new_game = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if y > 600:
                        if sudoku_board.reset_button_rect.collidepoint(event.pos):
                            sudoku_board.reset()
                        elif sudoku_board.restart_button_rect.collidepoint(event.pos):
                            new_game = True
                            music_player.quit()
                            break
                        elif sudoku_board.exit_button_rect.collidepoint(event.pos):
                            print("Bye bye thanks for playing")
                            pygame.quit()
                            quit()
                        else:
                            sudoku_board.selected_cell = None
                    else:
                        sudoku_board.cell_clicked(event.pos)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and sudoku_board.selected_cell is not None:
                    if sudoku_board.selected_cell.row < 8:
                        sudoku_board.selected_cell = sudoku_board.cells[sudoku_board.selected_cell.row + 1][
                            sudoku_board.selected_cell.col]
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and sudoku_board.selected_cell is not None:
                    if sudoku_board.selected_cell.row > 0:
                        sudoku_board.selected_cell = sudoku_board.cells[sudoku_board.selected_cell.row - 1][
                            sudoku_board.selected_cell.col]
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and sudoku_board.selected_cell is not None:
                    if sudoku_board.selected_cell.col < 8:
                        sudoku_board.selected_cell = sudoku_board.cells[sudoku_board.selected_cell.row][
                            sudoku_board.selected_cell.col + 1]
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and sudoku_board.selected_cell is not None:
                    if sudoku_board.selected_cell.col > 0:
                        sudoku_board.selected_cell = sudoku_board.cells[sudoku_board.selected_cell.row][
                            sudoku_board.selected_cell.col - 1]
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_1 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(1)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(2)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(3)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(4)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_6 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(6)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_7 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(7)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_8 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(8)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_9 and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(9)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and sudoku_board.selected_cell is not None:
                    sudoku_board.set_cell_sketched_value(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and sudoku_board.selected_cell is not None and sudoku_board.selected_cell.sketched_value != 0:
                    sudoku_board.set_cell_value(sudoku_board.selected_cell.sketched_value)
                    sudoku_board.set_cell_sketched_value(0)
            if new_game:
                break

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
                sudoku_board.hover(x, y)
                sudoku_board.draw(False, False, False)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                sudoku_board.draw(False, False, False)
            if test_mode:  # Define a variable for test mode
                for row in range(9):
                    for col in range(9):
                        sudoku_board.cells[row][col].value = sudoku_board.complete_board[row][col]

            if sudoku_board.is_full():
                if sudoku_board.check_win():
                    music_player.quit()
                    if counter == 0:
                        win_sfx = pygame.mixer.Sound("you_win.mp3")
                        win_sfx.play()
                        counter += 1
                    particle_animation(screen)
                else:
                    end_game(screen, False)
            pygame.display.update()
    return


if __name__ == "__main__":
    while True:
        counter = 0
        game(counter)
