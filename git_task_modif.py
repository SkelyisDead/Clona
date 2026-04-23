import pygame
import random

# Inițializare pygame
pygame.init()

# Constante pentru dimensiunea ferestrei și grilei
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 10
CELL_SIZE = 50
REGENERATE_INTERVAL = 5000  # 5 secunde în milisecunde


def generate_color_grid():
    """
    Generează o matrice 10x10 de culori random RGB.
    Fiecare celulă primește o culoare diferită.
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


# Crearea ferestrei aplicației
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(
    "Procedural Color Grid (Auto Regenerate Every 5 Seconds)"
)

# Generarea inițială a grilei
color_grid = generate_color_grid()

# Timer pentru regenerare automată
last_update_time = pygame.time.get_ticks()

running = True

while running:
    # Umplerea fundalului cu negru
    screen.fill((0, 0, 0))

    # Desenarea grilei colorate
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            pygame.draw.rect(
                screen,
                color_grid[row][column],
                (
                    column * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

    # Actualizarea ecranului
    pygame.display.flip()

    # Verificarea timpului pentru regenerare automată
    current_time = pygame.time.get_ticks()

    if current_time - last_update_time >= REGENERATE_INTERVAL:
        color_grid = generate_color_grid()
        last_update_time = current_time

    # Gestionarea evenimentelor
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # SPACE regenerează manual grila
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_grid = generate_color_grid()
                last_update_time = current_time

# Închiderea aplicației
pygame.quit()