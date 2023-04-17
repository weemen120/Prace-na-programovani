import pygame
import sys
import random

# Nastavení velikosti okna a herního pole
WINDOW_SIZE = 540
GRID_SIZE = WINDOW_SIZE // 9
LINE_WIDTH = 2

# Nastavení barev
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializace pygame
pygame.init()

# Vytvoření okna
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Sudoku')

# Inicializace hodnot
current_row = 0
current_col = 0
movement_cooldown = 0

# Generování náhodných čísel na herní pole
grid = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if random.random() < 0.5:
            grid[i][j] = random.randint(1, 9)

# Hlavní smyčka hry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Získání stisknutých kláves
    keys = pygame.key.get_pressed()

    # Omezení pohybu na každých 5 snímků
    if movement_cooldown == 0:
        # Pohyb nahoru
        if keys[pygame.K_UP]:
            current_row = max(0, current_row - 1)
            movement_cooldown = 5
        # Pohyb dolů
        if keys[pygame.K_DOWN]:
            current_row = min(8, current_row + 1)
            movement_cooldown = 5
        # Pohyb doleva
        if keys[pygame.K_LEFT]:
            current_col = max(0, current_col - 1)
            movement_cooldown = 5
        # Pohyb doprava
        if keys[pygame.K_RIGHT]:
            current_col = min(8, current_col + 1)
            movement_cooldown = 5

    # Snížení doby cooldownu
    if movement_cooldown > 0:
        movement_cooldown -= 1

    # Vymazání obrazovky
    screen.fill(WHITE)

    # Vykreslení herního pole
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, BLACK, (i * GRID_SIZE, j * GRID_SIZE, GRID_SIZE, GRID_SIZE), LINE_WIDTH)
            pygame.draw.rect(screen, RED, (current_col * GRID_SIZE, current_row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 2)
            if grid[i][j] != 0:
                font = pygame.font.SysFont(None, 36)
                text = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(text, (j * GRID_SIZE + GRID_SIZE // 3, i * GRID_SIZE + GRID_SIZE // 3))

    # Vykreslení změn na obrazovku
    pygame.display.flip()

    # Omezení počtu snímků za sekundu na 60
    pygame.time.Clock().tick(60)
