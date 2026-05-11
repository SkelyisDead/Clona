import pygame
import random

# Definim constante pentru culori, dimensiuni și timp
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
UPDATE_INTERVAL = 5000  # 5 secunde exprimate în milisecunde

# Inițializăm librăria Pygame
pygame.init()

def generate_random_color_grid():
    """
    Generează o grilă bidimensională (10x10) cu culori RGB complet aleatoare.
    """
    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            row.append(random_color)
        grid.append(row)
    return grid

# Setăm fereastra principală a aplicației
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid (Regenerates every 5 seconds)")

# Generăm prima grilă de culori
color_grid = generate_random_color_grid()
is_running = True

# Variabilă pentru a urmări timpul de la ultima regenerare a grilei
last_update_time = pygame.time.get_ticks()

# Bucla principală a programului
while is_running:
    # Curățăm ecranul setând fundalul la negru
    screen.fill((0, 0, 0))
    
    # Desenăm fiecare pătrat din grilă pe ecran
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = color_grid[y][x]
            rect_dimensions = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect_dimensions)
            
    pygame.display.flip()
    
    # Obținem timpul curent
    current_time = pygame.time.get_ticks()
    
    # Dacă au trecut 5000ms (5 secunde), regenerăm grila de culori
    if current_time - last_update_time >= UPDATE_INTERVAL:
        color_grid = generate_random_color_grid()
        last_update_time = current_time

    # Gestionăm evenimentele (cum ar fi apăsarea butonului X pentru închidere)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

# Închidem aplicația în mod curat
pygame.quit()