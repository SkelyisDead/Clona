import pygame
import random

# --- Constante pentru configurarea aplicației ---
GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE  # 500x500 pixeli
REGENERATE_INTERVAL = 5000  # 5 secunde în milisecunde

def generate_color_grid():
    """
    Generează o matrice bidimensională (10x10) cu tupluri de 
    culori RGB (Red, Green, Blue) complet aleatorii.
    """
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(GRID_SIZE)] 
        for _ in range(GRID_SIZE)
    ]

def main():
    # Inițializarea modulului pygame
    pygame.init()
    
    # Configurarea ferestrei principale
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Regenerează automat sau apasă SPACE)")
    
    # Crearea unui eveniment personalizat pentru regenerarea grilei la fiecare 5 secunde
    REGENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL)
    
    # Inițializarea datelor grilei și a stării de rulare
    grid_data = generate_color_grid()
    is_running = True
    
    # Bucla principală a jocului
    while is_running:
        # Curățarea ecranului cu negru
        screen.fill((0, 0, 0))
        
        # Desenarea fiecărui pătrat din grilă
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = grid_data[row][col]
                rect_dimensions = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect_dimensions)
        
        # Actualizarea ecranului
        pygame.display.flip()
        
        # Gestionarea evenimentelor (input de la utilizator / timere)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
            # Regenerare manuală la apăsarea tastei SPACE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                grid_data = generate_color_grid()
                
            # Regenerare automată declanșată de timer
            elif event.type == REGENERATE_EVENT:
                grid_data = generate_color_grid()

    # Închiderea aplicației în mod curat
    pygame.quit()

if __name__ == "__main__":
    main()