import pygame, random, time

pygame.init()

def genereaza_matrice():
    # matrice 10x10 
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

ecran = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Regenerare la 5s)")

# generare matrice culori
matrice_culori = genereaza_matrice()
ruleaza = True
timp_anterior = time.time()

while ruleaza:
    ecran.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(ecran, matrice_culori[y][x], (x * 50, y * 50, 50, 50))
            
    pygame.display.flip()

    # regenerare 5s
    timp_curent = time.time()
    if timp_curent - timp_anterior >= 5.0:
        matrice_culori = genereaza_matrice()
        timp_anterior = timp_curent

    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza = False
            
pygame.quit()