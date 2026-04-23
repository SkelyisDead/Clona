import pygame
import random

pygame.init()

def generate_color_grid():
    """Generate a 10x10 grid of random RGB colors."""
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
             for _ in range(10)] for _ in range(10)]

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

# Initial color data
data = generate_color_grid()
running = True

while running:
    screen.fill((0, 0, 0))

    # Draw the color grid
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, data[y][x], (x * 50, y * 50, 50, 50))

    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            data = generate_color_grid()

pygame.quit()