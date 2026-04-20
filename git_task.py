import pygame
import random
import time

# Inițializarea modulelor Pygame
pygame.init() [cite: 206]

# --- CONSTANTE ȘI CONFIGURĂRI ---
SCREEN_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
REFRESH_INTERVAL = 5  # Secunde între regenerări automate 

def generate_color_grid():
    """
    Generează o matrice 10x10 de culori aleatorii (RGB). [cite: 211]
    """
    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            # Fiecare celulă primește o culoare random (R, G, B)
            random_color = (
                random.randint(0, 255), 
                random.randint(0, 255), 
                random.randint(0, 255)
            )
            row.append(random_color)
        grid.append(row)
    return grid

# Setările ferestrei [cite: 212, 213]
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Procedural Color Grid - Auto-Regenerate")

# Starea inițială
color_data = generate_color_grid()
last_update_time = time.time()
running = True

# --- LOOP PRINCIPAL ---
while running:
    # 1. Gestionarea evenimentelor
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Regenerare manuală la apăsarea tastei SPACE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color_data = generate_color_grid()
            last_update_time = time.time()

    # 2. Logica de regenerare automată (la fiecare 5 secunde) 
    current_time = time.time()
    if current_time - last_update_time >= REFRESH_INTERVAL:
        color_data = generate_color_grid()
        last_update_time = current_time
        print("Grila a fost regenerată automat.")

    # 3. Randarea (Desenarea pe ecran) [cite: 82, 89]
    screen.fill((0, 0, 0)) # Fundal negru
    
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = color_data[y][x]
            rect_position = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect_position)

    pygame.display.flip()

# Închiderea curată a aplicației
pygame.quit()