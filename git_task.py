import pygame
import random

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

def generate_color_grid():
    # Create a 10x10 grid filled with random RGB colors
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(10)] for _ in range(10)]

# Initial state setup
color_grid = generate_color_grid()
running = True

# Main game loop
while running:
    screen.fill((0, 0, 0))

    # Draw the grid cells
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, color_grid[y][x], (x * 50, y * 50, 50, 50))
            
    pygame.display.flip()

    # Handle events (quit and key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color_grid = generate_color_grid()

pygame.quit()