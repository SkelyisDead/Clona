print("Hello World")

import random
import pygame

# Constante pentru dimensiunile ferestrei + grila
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGENERATE_INTERVAL_MS = 5000  # 5 sec exprimate in ms

def generate_random_color_grid():
    """
    Genereaza o matrice 2D (10x10) ce contine culori RGB aleatorii.
    """
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(GRID_SIZE)]
        for _ in range(GRID_SIZE)
    ]

def main():
    # Initializare modul
    pygame.init()
    
    # Configurarea ferestrei(folosind variabilele definite) si a titlului 
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (5sec or press SPACE)")
    
    # Generarea matricei initiale de culori
    color_grid = generate_random_color_grid()
    
    # Regenerarea grilei la fiecare 5 secunde folosind event
    REGENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL_MS)
    
    running = True
    
    # Loop-ul principal
    while running:
        # Stergere ecran
        screen.fill((0, 0, 0))
        
        # Desenarea celulelor in grila
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = color_grid[row][col]
                rect_x = col * CELL_SIZE
                rect_y = row * CELL_SIZE
                pygame.draw.rect(screen, color, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))
        
        # Actualizarea ecranului
        pygame.display.flip()
        
        # Gestionarea evenimentelor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Oprirea buclei la inchidere
                running = False
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Regenerare manuala la apasare SPACE
                color_grid = generate_random_color_grid()
                # Resetam timerul pentru evitarea regenerarii inainte de 5 sec
                pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL_MS)
                
            elif event.type == REGENERATE_EVENT:
                # Regenerare declansata de event(timer)
                color_grid = generate_random_color_grid()
                
    # Inchiderea modulului
    pygame.quit()

if __name__ == "__main__":
    main()