import random
import pygame

# Constante
SIZE, GRID, CELL, REGEN_MS = 500, 10, 50, 5000

def get_random_grid():
    # Generează grila 10x10 cu culori RGB aleatoare
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID)] for _ in range(GRID)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Color Grid (Regen: 5s / SPACE)")
    
    color_grid = get_random_grid()
    
    # Setează evenimentul pentru regenerare la fiecare 5 secunde
    REGEN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGEN_EVENT, REGEN_MS)
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        # Desenează celulele
        for y in range(GRID):
            for x in range(GRID):
                pygame.draw.rect(screen, color_grid[y][x], (x * CELL, y * CELL, CELL, CELL))
        
        pygame.display.flip()
        
        # Gestionare evenimente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == REGEN_EVENT:
                color_grid = get_random_grid()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                color_grid = get_random_grid()
                pygame.time.set_timer(REGEN_EVENT, REGEN_MS) # Resetează timer-ul la apăsarea tastei

    pygame.quit()

if __name__ == "__main__":
    main()