import pygame
import random

# constante globale
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGENERATE_EVENT = pygame.USEREVENT + 1
TIMER_INTERVAL_MS = 5000

def generate_random_colors():
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

def main():
    pygame.init()

    # window
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")

    # Inițializare variabile de stare
    color_grid = generate_random_colors()
    is_running = True

    # timer
    pygame.time.set_timer(REGENERATE_EVENT, TIMER_INTERVAL_MS)

    while is_running:
        screen.fill((0, 0, 0))

        # grid culori
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = color_grid[row][col]
                rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)

        pygame.display.flip()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                color_grid = generate_random_colors()
                # Resetare cronometru manual
                pygame.time.set_timer(REGENERATE_EVENT, TIMER_INTERVAL_MS)
            elif event.type == REGENERATE_EVENT:
                color_grid = generate_random_colors()

    pygame.quit()

if __name__ == "__main__":
    main()
