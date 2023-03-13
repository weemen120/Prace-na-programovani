import pygame

# Nastavení velikosti okna a hrací plochy
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS
WINDOW_SIZE = (WIDTH, HEIGHT)

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializace pygame a okna
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Piškvorky')

# Font pro text
font = pygame.font.SysFont('comicsansms', 72)

def draw_grid():
    # Nakreslí hrací plochu
    for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 2)

def draw_markers(board):
    # Nakreslí křížky a kolečka na hrací plochu podle aktuálního stavu
    for x in range(COLS):
        for y in range(ROWS):
            if board[y][x] == 'X':
                center = (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2)
                radius = SQUARE_SIZE // 2 - 10
                pygame.draw.circle(screen, RED, center, radius, 2)
            elif board[y][x] == 'O':
                center = (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2)
                radius = SQUARE_SIZE // 2 - 10
                pygame.draw.circle(screen, BLUE, center, radius, 2)

def draw_winner(player):
    # Zobrazí vítěze
    text = f'Vítěz: {player}'
    label = font.render(text, True, BLACK, WHITE)
    screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT // 2 - label.get_height() // 2))

def get_winner(board):
    # Zjistí, zda je na hrací ploše nějaký vítěz
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def main():
    # Inicializace proměnných
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    turn = 'X'
    winner = None

    # Hlavní smyčka
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                # Získání pozice kliknutí myší
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE
                # Pokud pole není již obsazeno a hra neskončila, uložíme značku hráče na hrací plochu
                if board[row][col] == '':
                    board[row][col] = turn
                    # Změna tahu na dalšího hráče
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'
                    # Kontrola, zda hra skončila výhrou některého hráče nebo remízou
                    winner = get_winner(board)
                    if winner is not None:
                        print(winner)
                    elif all([all(row) for row in board]):
                        print('Remíza')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Vyplnění pozadí a kreslení hrací plochy a značek
        screen.fill(BLACK)
        draw_grid()
        draw_markers(board)
        # Pokud existuje vítěz, zobrazíme ho
        if winner is not None:
            draw_winner(winner)

        pygame.display.update()

    # Ukončení programu
    pygame.quit()

if __name__ == '__main__':
    main()

