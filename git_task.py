import pygame
import random

# Constante
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGENERATE_INTERVAL = 5000  # milisecunde (5 secunde)


def generate_color_grid():
    """
    Generează o matrice GRID_SIZE x GRID_SIZE de culori random (RGB).
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(screen, grid_data):
    """
    Desenează grid-ul de culori pe ecran.
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = grid_data[row][col]
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

    clock = pygame.time.Clock()

    grid_data = generate_color_grid()

    running = True

    # Timer pentru regenerare automată
    pygame.time.set_timer(pygame.USEREVENT, REGENERATE_INTERVAL)

    while running:
        screen.fill((0, 0, 0))

        draw_grid(screen, grid_data)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Regenerare la apăsarea SPACE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                grid_data = generate_color_grid()

            # Regenerare automată la 5 secunde
            elif event.type == pygame.USEREVENT:
                grid_data = generate_color_grid()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()