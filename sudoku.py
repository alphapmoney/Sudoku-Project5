import sudoku_generator as sg
import pygame

# Initialize pygame
pygame.init()

game_font = pygame.font.SysFont('Comic Sans MS', 70)
button_font = pygame.font.SysFont('Arial', 30)
X = 500
Y = 600
size = (X, Y)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

text = game_font.render('Sudoku Game', False, (0, 0, 0))
button_text = button_font.render('Test', False, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (X // 2, 100)

running = True
while running:
    mouse = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)

    if X / 2 <= mouse[0] <= X / 2 + 140 and Y / 2 <= mouse[1] <= Y / 2 + 40:
        pygame.draw.rect(screen, color_light, [X / 2, Y / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [X / 2, Y / 2, 140, 40])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if X / 2 <= mouse[0] <= X / 2 + 140 and Y / 2 <= mouse[1] <= Y / 2 + 40:
                    running = False

    pygame.display.update()
