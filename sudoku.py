import pygame
from board import Board

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
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Sudoku")
    difficulty = draw_game_start(screen)

    board = Board(screen, difficulty)
    screen = pygame.display.set_mode((900, 1000))

    while True:
        screen.fill((255, 255, 255))
        board.event_loop()
        board.screen_update()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



