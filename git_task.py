import pygame
import random

# Initialize Pygame modules
pygame.init()

# Constants for window and grid configuration
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE
REGENERATE_INTERVAL_MS = 5000  # 5 seconds in milliseconds

def generate_random_color_grid():
    """
    Creates a 10x10 matrix containing randomly generated RGB colors.
    """
    return [[(random.randint(0, 255), 
              random.randint(0, 255), 
              random.randint(0, 255)) 
             for _ in range(GRID_SIZE)] 
            for _ in range(GRID_SIZE)]

# Set up the display surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Procedural Color Grid - 5s Auto-Update")

# Initialize data and timer
color_grid = generate_random_color_grid()
is_running = True

# Define a custom event for color regeneration
REGENERATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL_MS)

# Main application loop
while is_running:
    # 1. Drawing section
    screen.fill((0, 0, 0))
    
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_color = color_grid[row][col]
            cell_rect = (col * CELL_SIZE, 
                         row * CELL_SIZE, 
                         CELL_SIZE, 
                         CELL_SIZE)
            
            pygame.draw.rect(screen, cell_color, cell_rect)

    # Update the full display Surface to the screen
    pygame.display.flip()

    # 2. Event handling section
    for event in pygame.event.get():
        # Exit the program
        if event.type == pygame.QUIT:
            is_running = False
            
        # Manual regeneration when SPACE is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_grid = generate_random_color_grid()
        
        # Automatic regeneration every 5 seconds
        elif event.type == REGENERATE_EVENT:
            color_grid = generate_random_color_grid()

# Clean up and close the window
pygame.quit()