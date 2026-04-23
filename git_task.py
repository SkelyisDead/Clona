import pygame
import random

pygame.init()

def f():
    return [
        [
            (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
            for _ in range(10)
        ]
        for _ in range(10)
    ]

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Regenerates every 5 seconds or by pressing SPACE")
data = f()
reset = True

last_tick = pygame.time.get_ticks()

while reset:
    screen.fill((0, 0, 0))

    now_tick = pygame.time.get_ticks()
    
    if now_tick - last_tick >= 5000:
        data = f()                     
        last_tick = now_tick

    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, data[y][x], (x * 50, y * 50, 50, 50))

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            reset = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            data = f()

            last_tick = pygame.time.get_ticks()

pygame.quit()