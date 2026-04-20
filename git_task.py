import pygame
import random
import time

pygame.init()

def genereaza_matrice_culori():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(10)] for _ in range(10)]

fereastra = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Laborator 7 - Coding Style")

culori = genereaza_matrice_culori()
running = True
timp_start = time.time()

while running:
    fereastra.fill((0, 0, 0))

    for i in range(10):
        for j in range(10):
            pygame.draw.rect(fereastra, culori[i][j], (j * 50, i * 50, 50, 50))

    pygame.display.flip()

    if time.time() - timp_start >= 5:
        culori = genereaza_matrice_culori()
        timp_start = time.time()

    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            running = False

pygame.quit()