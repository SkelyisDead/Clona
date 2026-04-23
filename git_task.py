import pygame
import random
import time

pygame.init()

def genereaza_matrice_culori():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

fereastra = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid")

date_culori = genereaza_matrice_culori()
ruleaza = True
timp_start = time.time()

while ruleaza:
    fereastra.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(fereastra, date_culori[y][x], (x * 50, y * 50, 50, 50))
    
    pygame.display.flip()

    timp_curent = time.time()
    if timp_curent - timp_start >= 5:
        date_culori = genereaza_matrice_culori()
        timp_start = timp_curent

    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza = False
        if eveniment.type == pygame.KEYDOWN and eveniment.key == pygame.K_SPACE:
            date_culori = genereaza_matrice_culori()

pygame.quit()
