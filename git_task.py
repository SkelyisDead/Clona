import pygame
import random

pygame.init()

def generate_grid_data():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

data = generate_grid_data()
running = True

while running:
    screen.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            color = data[y][x]
            pygame.draw.rect(screen, color, (x * 50, y * 50, 50, 50))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                data = generate_grid_data()

pygame.quit()