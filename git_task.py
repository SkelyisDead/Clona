import pygame
import random

# Inițializare pygame
pygame.init()


def generate_grid_data():
    """
    Generează o matrice 10x10 cu culori RGB aleatoare.
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(10)
        ]
        for _ in range(10)
    ]


# Creare fereastră
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(
    "Procedural Color Grid (Press SPACE to Regenerate)"
)

# Generare date inițiale
grid_data = generate_grid_data()
running = True

while running:
    # Curățare ecran
    screen.fill((0, 0, 0))

    # Desenare grid
    for y in range(10):
        for x in range(10):
            color = grid_data[y][x]

            pygame.draw.rect(
                screen,
                color,
                (x * 50, y * 50, 50, 50)
            )

    # Actualizare display
    pygame.display.flip()

    # Tratare evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Regenerare culori
                grid_data = generate_grid_data()
