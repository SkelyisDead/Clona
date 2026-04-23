import pygame,random

pygame.init()

def make_empty_grid():
    matrix = []
    for _ in range(10):
        row = []
        for _ in range(10):
            row.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        matrix.append(row)
    return matrix

surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
data = make_empty_grid()
running = True

while running:
    surface.fill((0, 0, 0))

    for y in range(10):
         for x in range(10):
             pygame.draw.rect(surface, data[y][x], (x*50, y*50, 50, 50))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            data = make_empty_grid()

pygame.quit()
