import pygame
import random

# Inițializare pygame
pygame.init()

# Constante
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGENERATE_TIME = 5000  # milisecunde (5 secunde)

# Creare fereastră
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid")

# Timer pentru regenerare automată
pygame.time.set_timer(pygame.USEREVENT, REGENERATE_TIME)


def generate_color_grid():
    """
    Generează o matrice GRID_SIZE x GRID_SIZE
    cu culori aleatorii (RGB).
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


def draw_grid(surface, grid_data):
    """
    Desenează grid-ul de culori pe ecran.
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = grid_data[row][col]
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, color, rect)


def main():
    running = True
    color_grid = generate_color_grid()

    while running:
        screen.fill((0, 0, 0))

        # Desenare grid
        draw_grid(screen, color_grid)
        pygame.display.flip()

        # Tratare evenimente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Regenerare automată la 5 secunde
            elif event.type == pygame.USEREVENT:
                color_grid = generate_color_grid()

            # Regenerare manuală la SPACE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color_grid = generate_color_grid()

    pygame.quit()


if __name__ == "__main__":
    main()