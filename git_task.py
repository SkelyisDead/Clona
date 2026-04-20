import pygame
import random

# Constante pentru dimensiunea ferestrei și a grilei
WINDOW_SIZE = 500
GRID_ROWS = 10
GRID_COLS = 10
CELL_SIZE = WINDOW_SIZE // GRID_COLS
UPDATE_INTERVAL_MS = 5000  # 5 secunde în milisecunde

def generate_random_color_grid():
    """Generează o matrice 10x10 cu culori RGB aleatoare."""
    grid = []
    for _ in range(GRID_ROWS):
        row = []
        for _ in range(GRID_COLS):
            # Generăm o culoare RGB aleatoare
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            row.append(random_color)
        grid.append(row)
    return grid

def main():
    # Inițializăm modulele Pygame
    pygame.init()
    
    # Configurăm ecranul
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Regenerează la 5 secunde)")
    
    # Inițializăm datele
    color_grid = generate_random_color_grid()
    is_running = True
    last_update_time = pygame.time.get_ticks()
    
    # Bucla principală a programului
    while is_running:
        # 1. Gestionarea evenimentelor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            # Păstrăm și funcționalitatea de a regenera manual la apăsarea tastei SPACE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color_grid = generate_random_color_grid()
                    last_update_time = pygame.time.get_ticks()
        
        # 2. Logica de actualizare automată (Timer de 5 secunde)
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= UPDATE_INTERVAL_MS:
            color_grid = generate_random_color_grid()
            last_update_time = current_time
            
        # 3. Desenarea pe ecran
        screen.fill((0, 0, 0))  # Setăm fundalul negru
        
        for row_index in range(GRID_ROWS):
            for col_index in range(GRID_COLS):
                color = color_grid[row_index][col_index]
                # Calculăm poziția fiecărui pătrat pe ecran
                x_pos = col_index * CELL_SIZE
                y_pos = row_index * CELL_SIZE
                
                # Desenăm dreptunghiul curent
                pygame.draw.rect(screen, color, (x_pos, y_pos, CELL_SIZE, CELL_SIZE))
                
        # Actualizăm interfața grafică
        pygame.display.flip()
        
    # Închidem aplicația corect la ieșirea din buclă
    pygame.quit()

if __name__ == "__main__":
    main()