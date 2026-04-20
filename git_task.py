import pygame
import random
import time

# Inițializare pygame
pygame.init()

# Dimensiuni
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE


def generate_color_grid():
    """
    Generează o matrice de culori random.
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


def draw_grid(screen, grid_data):
    """
    Desenează grid-ul pe ecran.
    """
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(
                screen,
                grid_data[y][x],
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )


def main():
    """
    Rulează aplicația și regenerează culorile la fiecare 5 secunde.
    """
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")

    grid_data = generate_color_grid()
    running = True
    last_update_time = time.time()

    while running:
        screen.fill((0, 0, 0))

        draw_grid(screen, grid_data)
        pygame.display.flip()

        # Evenimente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Regenerare la fiecare 5 secunde
        current_time = time.time()
        if current_time - last_update_time >= 5:
            grid_data = generate_color_grid()
            last_update_time = current_time

    pygame.quit()


if __name__ == "__main__":
    main()