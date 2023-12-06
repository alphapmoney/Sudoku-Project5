'''
    Author: Alexander Wang, Brenden Brahier, Mohammed Ali, Drake Bell
    Date: 12/06/2023
    Group 86
    Sudoku Project 4
'''

# Imports and global variables here
import pygame
from pygame import mixer
from board import Board
import random
import os
chica = []

# Define a class for the background music
class bg_music():
    def __init__(self):
        # Initialize the mixer and the channel and the songs
        pygame.mixer.init()
        self.music_sfx = pygame.mixer.Channel(1)
        self.songs = ["music.mp3", "music_medium.mp3", "music_hard.mp3", "rizz.mp3","areyoustrongbecauseyourenahidwin.mp3",
                      "you_win.mp3"]
    # Define a function to play the music with the given song index
    def play(self, song_index):
        if 0 <= song_index < len(self.songs):
            song = self.songs[song_index]
            music = mixer.Sound(song)
            self.music_sfx.play(music, -1)
            print(f'Playing {song}')
        else:
            print("Invalid song index")
    # Define a function to stop the music
    def quit(self):
        self.music_sfx.stop()

    # def unpause(self):
    # self.music_sfx.unpause()
music_player = bg_music()

# Define a function to draw the game start screen with menu options
def draw_game_start(screen):
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    help_button_font = pygame.font.Font(None, 30)
    # Define the texts and the rectangles for the buttons
    title = title_font.render("Sudoku", True, (255, 140, 0))
    easy_button = button_font.render("Easy", True, (255, 255, 255))
    medium_button = button_font.render("Medium", True, (255, 255, 255))
    hard_button = button_font.render("Hard", True, (255, 255, 255))
    help_button = help_button_font.render("Help", True, (255, 255, 255))
    # Rectangles for the buttons
    easy_button_rect = pygame.Rect(67, 500, 100, 50)
    medium_button_rect = pygame.Rect(229, 500, 150, 50)
    hard_button_rect = pygame.Rect(441, 500, 100, 50)
    help_button_rect = pygame.Rect(270, 610, 60, 35)
    # Loop for the game start screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Checking if the mouse is clicked on the buttons and returning the difficulty
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_button_rect.collidepoint(event.pos):
                    print("Easy")
                    music_player.play(0)
                    return 30
                elif medium_button_rect.collidepoint(event.pos):
                    print("Medium")
                    music_player.play(1)
                    return 40
                # Plays a song when the buttons are clicked and returns the difficulty
                elif hard_button_rect.collidepoint(event.pos):
                    print("Hard")
                    music_player.play(2)
                    return 50
                elif help_button_rect.collidepoint(event.pos):
                    help_screen(screen)
        # This is where the buttons are drawn
        screen.fill((255, 255, 255))
        screen.blit(title, (175, 200))
        pygame.draw.rect(screen, (255, 140, 0), easy_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), medium_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), hard_button_rect)
        pygame.draw.rect(screen, (255, 140, 0), help_button_rect)
        # Checking if the mouse is on the buttons and changing the color of the buttons
        mouse = pygame.mouse.get_pos()
        if easy_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), easy_button_rect)
            # Also makes cursor a pointer
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif medium_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), medium_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        # For the hover effect so user knows which button they are o. Also changes the cursor to a pointer
        elif hard_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), hard_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif help_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), help_button_rect)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # Blitting the buttons onto the screen
        screen.blit(easy_button, (75, 508))
        screen.blit(medium_button, (240, 508))
        screen.blit(hard_button, (450, 508))
        screen.blit(help_button, (277, 618))

        pygame.display.update()

# Define a function to draw the help screen
def help_screen(screen):
    # Change the screen size to fit the help screen and define the fonts and texts
    screen = pygame.display.set_mode((597, 600))
    title_font = pygame.font.Font(None, 60)
    text_font = pygame.font.Font(None, 30)
    button_font = pygame.font.Font(None, 50)
    # Define the texts and the rectangles for the buttons and the back button to go back to the game start screen
    title = title_font.render("How to play:", True, (255, 140, 0))
    description1 = text_font.render("Click on cell to select it (will be highlighted)", True, (255, 140, 0))
    description2 = text_font.render("Type a number to sketch it in the cell", True, (255, 140, 0))
    description3 = text_font.render("Press enter to confirm the number", True, (255, 140, 0))
    description4 = text_font.render("Press backspace to clear the sketch", True, (255, 140, 0))
    back_button = button_font.render("Back", True, (255, 255, 255))

    back_button_rect = pygame.Rect(250, 442, 100, 50)
    # Loop for the help screen to draw the texts and the buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Checking if the mouse is clicked on the back button and returning to the game start screen
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button_rect.collidepoint(event.pos):
                    screen = pygame.display.set_mode((597, 700))
                    return
        # Drawing the texts and the buttons onto the screen
        screen.fill((255, 255, 255))
        screen.blit(title, (175, 100))
        screen.blit(description1, (100, 200))
        screen.blit(description2, (100, 250))
        screen.blit(description3, (100, 300))
        screen.blit(description4, (100, 350))
        pygame.draw.rect(screen, (255, 140, 0), back_button_rect)
        # Hover effect for the back button and changing the cursor to a pointer
        mouse = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (196, 98, 16), back_button_rect)
            # Also makes cursor a pointer
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # Blitting the back button onto the screen
        screen.blit(back_button, (258, 450))

        pygame.display.update()
# Counter for the chica images
counter = 0
# Define a function to draw the end game screen with the win or lose text
def end_game(screen, win):
    # Define the texts and the rectangles for the buttons
    global counter
    screen.fill((255, 255, 255))
    end_font = pygame.font.Font(None, 100)
    # Draw the win or lose text based on the win boolean
    if win:
        win_text = end_font.render("You Win", True, (255, 150, 0))
    else:
        # Animating the chica images when the user loses
        win_text = end_font.render("You Lose", True, (255, 150, 0))
        screen_size = (597, 700)
        img = chica[counter]
        scaled_image = pygame.transform.scale(img, screen_size)
        screen.blit(scaled_image, (0, 0))
        # Animating per frame and looping through the images
        if counter == 54:
            counter = 0
        else:
            counter += 1
    # Rendering the texts and the rectangles for the buttons
    win_text_rect = win_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    esc_font = pygame.font.Font(None, 36)
    esc = esc_font.render("Press Esc to Exit", True, (255, 150, 0))
    new_game = esc_font.render("Press Enter to Play Again", True, (255, 150, 0))
    esc_text_rect = esc.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    new_game_text_rect = new_game.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 85))
    screen.blit(win_text, win_text_rect)
    screen.blit(esc, esc_text_rect)
    screen.blit(new_game, new_game_text_rect)
    # Only delay if the user loses so the animation can play
    if not win:
        pygame.time.delay(75)


    # If the user presses enter, start a new game, if the user presses esc, quit the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            music_player.quit()
            game(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

# Define a function to animate the particles when the user wins
nahidwin_counter = 0
def particle_animation(screen):
    # nahidwin_counter so audio only plays once at a time
    global nahidwin_counter
    # Define the colors for the particles
    RED = [255, 0, 0]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 222, 179]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]

    # Define a boolean for the easter egg and give it a 1/5 chance of being true
    easter_egg = True if random.randint(1, 5) == 1 else False

    confetti = []
    # Loop to generate the particles
    for i in range(250):
        x = random.randrange(0, 700)
        y = random.randrange(0, 700)
        confetti.append([x, y])
        # confetti contains lists of some coordinates randomly made
    clock = pygame.time.Clock()
    # Loop to draw the particles and the image
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # If the user presses esc, quit the game, if the user presses enter, start a new game
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                music_player.quit()
                game(0)
        # Draw the particles and the image
        screen.fill((255, 255, 255))
        end_game(screen, True)
        confetti_color = random.choice([RED, ORANGE, YELLOW, GREEN, BLUE])
        # If the easter egg is true, play the easter egg song and draw the image, else play the normal song
        if easter_egg:
            if nahidwin_counter == 0:
                music_player.play(4)
                nahidwin_counter += 1
            image = pygame.image.load('nahidwin.jpg')
            img = pygame.transform.scale(image, (597, 700))
            screen.blit(img, (0, 0))
        # If the easter egg is false, play the normal song and draw the particles
        else:
            if nahidwin_counter == 0:
                music_player.play(5)
                nahidwin_counter += 1
        # Loop to draw the particles and move them down the screen
        for party in range(len(confetti)):
            pygame.draw.circle(screen, confetti_color, confetti[party], 3)
            confetti[party][1] += 1
            if confetti[party][1] > screen.get_height():  # Adjusted the limit here
                confetti[party][1] = random.randrange(-50, -10)
                confetti[party][0] = random.randrange(0, screen.get_width())
        # Update the screen and tick the clock because the particles are moving down the screen
        clock.tick(40)
        pygame.display.update()

# Testing mode to test win screen
test_mode = False

# Main game loop
def game(counter):
    # nahidwin_counter so audio only plays once at a time
    global nahidwin_counter
    nahidwin_counter = 0
    game_over = False
    # Loop for the game
    while not game_over:
        # Initialize pygame and the quit music player from the previous game
        pygame.init()
        music_player.quit()

        screen = pygame.display.set_mode((597, 700))
        difficulty = draw_game_start(screen)
        # Initialize the board with the screen and the difficulty and generate a sudoku board with the given difficulty
        sudoku_board = Board(screen, difficulty)
        # Loop for the game
        new_game = False
        while True:
            for event in pygame.event.get():
                # if user quits exit pygame
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Check what the user clicked on using the mouse
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    # If the user clicks on the buttons, reset the board, restart the game, or exit the game
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
                            # If the user click on nothing and is below the board set selected cell to none
                            sudoku_board.selected_cell = None
                    else:
                        # If the user clicks on the board, set the selected cell to the cell that was clicked on
                        sudoku_board.cell_clicked(event.pos)
                # add keyboard functionality to the game to select cells
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
                # add keyboard functionality to the game to set cell values only if the selected cell is not locked and is not none
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
                    # If the user presses enter and the selected cell is not locked, set the value of the cell to the sketched value
                    sudoku_board.set_cell_value(sudoku_board.selected_cell.sketched_value)
                    sudoku_board.set_cell_sketched_value(0)
            # If new_game is true, break from the loop and start a new game
            if new_game:
                break
            # Draw the board and the buttons and check if the user wins
            screen.fill((255, 255, 255))
            x, y = pygame.mouse.get_pos()
            # Checking if the mouse is on the buttons and changing the cursor to a pointer and hover effect over the correct button
            if sudoku_board.reset_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                sudoku_board.draw(True, False, False)
            elif sudoku_board.restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                sudoku_board.draw(False, True, False)
            elif sudoku_board.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                sudoku_board.draw(False, False, True)
            # Set the cursor to a pointer if the mouse is on the board and draw the board
            elif y < 600 and 0 <= x <= screen.get_width():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                sudoku_board.hover(x, y)
                sudoku_board.draw(False, False, False)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                sudoku_board.draw(False, False, False)

            # Test mode to test win screen by filling in the board with the complete board
            if test_mode:  # Define a variable for test mode
                for row in range(9):
                    for col in range(9):
                        sudoku_board.cells[row][col].value = sudoku_board.complete_board[row][col]
            # Check if the board is full and if the user wins
            if sudoku_board.is_full():
                # If win play the particle animation
                if sudoku_board.check_win():
                    particle_animation(screen)
                else:
                    # Play the music and draw the end game screen with the lose text
                    if counter == 0:
                        music_player.play(3)
                        counter += 1
                    end_game(screen, False)
            pygame.display.update()
    return

# Main function to run the game
if __name__ == "__main__":
    # Initialize pygame and the screen and load the chica images
    pygame.init()
    screen = pygame.display.set_mode((597, 700))
    # Chica images need to be loaded first and appended to a list to be used in the end game screen
    for x in range(55):
        file = sorted(os.listdir('chica'))[x]
        img = pygame.image.load('chica/' + file).convert()
        chica.append(img)
    # Loop to keep the game running and quitting functionality is inside the game
    while True:
        counter = 0
        game(counter)
