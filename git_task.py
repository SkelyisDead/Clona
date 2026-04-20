import pygame
import random
import time

# Inițializează modulele pygame
pygame.init()

def generate_color_grid():
    """Generează o matrice 10x10 conținând culori RGB complet aleatorii."""
    # Lista de liste unde fiecare element este un tuplu (R, G, B)
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

# Setările ecranului (rezoluție și titlu)
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Procedural Color Grid (Regenereaza automat la 5s)")

# Inițializarea variabilelor de stare
color_grid = generate_color_grid()
is_running = True
last_update_time = time.time()  # Salvăm timpul de start pentru contor

# Bucla principală a aplicației
while is_running:
    # Setăm fundalul pe negru
    screen.fill((0, 0, 0))

    # Desenăm grila de 10x10
    for y in range(10):
        for x in range(10):
            # Parametrii pentru fiecare celulă: coordonata X, coordonata Y, lățime, înălțime
            rect_dimensions = (x * 50, y * 50, 50, 50)
            pygame.draw.rect(screen, color_grid[y][x], rect_dimensions)
    
    # Actualizăm interfața grafică
    pygame.display.flip()

    # Procesăm evenimentele (cum ar fi apăsarea pe "X" pentru a închide fereastra)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        # Păstrăm și funcționalitatea opțională a tastei SPACE pentru regenerare manuală
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_grid = generate_color_grid()
                last_update_time = time.time()  # Resetăm timer-ul dacă dăm regenerare manuală

    # Regenerarea automată a rezultatului o dată la 5 secunde
    current_time = time.time()
    if current_time - last_update_time >= 5.0:
        color_grid = generate_color_grid()
        last_update_time = current_time

# Oprim librăria pygame curat
pygame.quit()