import pygame
import sys
import mysql.connector

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
                label = font.render('X', True, WHITE, BLACK)
                screen.blit(label, (center[0] - label.get_width() // 2, center[1] - label.get_height() // 2))
            elif board[y][x] == 'O':
                center = (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2)
                label = font.render('O', True, WHITE, BLACK)
                screen.blit(label, (center[0] - label.get_width() // 2, center[1] - label.get_height() // 2))

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

def add_win_to_db(name):
    try:
        connection = mysql.connector.connect(
            host="dbs.spskladno.cz",
            user="student13",
            password="spsnet",
            database="vyuka13"
        )
        cursor = connection.cursor()

        # Check if the player already exists in the database
        query_select = "SELECT * FROM HRY WHERE player_name = %s"
        data_select = (name,)
        cursor.execute(query_select, data_select)
        result = cursor.fetchone()

        if result:
            # If the player exists, update the win count
            query_update = "UPDATE HRY SET wins = wins + 1 WHERE player_name = %s"
            cursor.execute(query_update, data_select)
        else:
            # If the player doesn't exist, insert a new record
            query_insert = "INSERT INTO HRY (player_name, wins) VALUES (%s, 1)"
            cursor.execute(query_insert, data_select)

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_player_wins(name):
    try:
        connection = mysql.connector.connect(
            host="dbs.spskladno.cz",
            user="student13",
            password="spsnet",
            database="vyuka13"
        )
        cursor = connection.cursor()

        query = "SELECT wins FROM HRY WHERE player_name = %s"
        data = (name,)
        cursor.execute(query, data)
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0] if result else 0

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0

def get_player_name():
    screen.fill(BLACK)
    input_box = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, SQUARE_SIZE)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text = ''
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

def get_player_symbol():
    screen.fill(BLACK)
    font = pygame.font.SysFont('comicsansms', 48)
    text_x = font.render('X', True, WHITE)
    text_o = font.render('O', True, WHITE)
    text_x_rect = text_x.get_rect(center=(WIDTH // 4, HEIGHT // 2))
    text_o_rect = text_o.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

    player_symbol = None

    while player_symbol is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_x_rect.collidepoint(event.pos):
                    player_symbol = 'X'
                elif text_o_rect.collidepoint(event.pos):
                    player_symbol = 'O'

        screen.fill(BLACK)
        screen.blit(text_x, text_x_rect)
        screen.blit(text_o, text_o_rect)

        pygame.display.flip()

    return player_symbol

def main():
    # Zeptáme se hráče na jméno a symbol pomocí GUI
    player_name = get_player_name()
    player_symbol = get_player_symbol()
    print(f'Vaše jméno: {player_name}')
    print(f'Zvolený symbol: {player_symbol}')
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
                        print(f'Vítěz: {winner}')
                    if winner == player_symbol:
                        add_win_to_db(player_name)
                        print(f'Aktuální počet výher: {get_player_wins(player_name)}')
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
