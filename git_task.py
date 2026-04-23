import pygame
import random
import time

# Inițializarea modulelor Pygame
pygame.init()

# Constante pentru configurare
SCREEN_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
REGENERATE_INTERVAL = 5  # secunde

def generate_color_grid(rows, cols):
    """Generează o matrice de culori aleatorii (RGB)."""
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(cols)] 
        for _ in range(rows)
    ]

# Configurarea ferestrei
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Grilă Procedurală - Regenerare la 5 secunde")

# Starea inițială
color_data = generate_color_grid(GRID_SIZE, GRID_SIZE)
last_update_time = time.time()
is_running = True

# Bucla principală a programului
while is_running:
    current_time = time.time()

    # Verificăm dacă au trecut 5 secunde pentru regenerare
    if current_time - last_update_time >= REGENERATE_INTERVAL:
        color_data = generate_color_grid(GRID_SIZE, GRID_SIZE)
        last_update_time = current_time

    # Gestionarea evenimentelor
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        # Permitem în continuare regenerarea manuală la apăsarea tastei SPACE
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color_data = generate_color_grid(GRID_SIZE, GRID_SIZE)
            last_update_time = current_time

    # Desenarea grilei pe ecran
    screen.fill((0, 0, 0))
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            color = color_data[row_index][col_index]
            rect_position = (col_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect_position)

    # Actualizarea afișajului
    pygame.display.flip()

# Închiderea corectă a resurselor
pygame.quit()
