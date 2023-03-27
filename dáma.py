import pygame
import sys

# Nastavení herních údajů
WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = WIDTH // 8
FPS = 60

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicializace Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dáma')
clock = pygame.time.Clock()


# Vytvoření hrací desky
board = [
    ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
    ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
    ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'w', '.', 'w', '.', 'w', '.', 'w'],
    ['w', '.', 'w', '.', 'w', '.', 'w', '.'],
    ['.', 'w', '.', 'w', '.', 'w', '.', 'w']
]

