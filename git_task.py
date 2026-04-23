import pygame

# Initializarea modulelor Pygame
pygame.init()

# Constante pentru configurarea ferestrei
LATIME_FEREASTRA = 500
INALTIME_FEREASTRA = 500
DIMENSIUNE_CELULA = 50
COLOANE = LATIME_FEREASTRA // DIMENSIUNE_CELULA
RANDURI = INALTIME_FEREASTRA // DIMENSIUNE_CELULA

# Intervalul de regenerare (in milisecunde)
INTERVAL_REGENERARE = 5000  # 5 secunde

def genereaza_matrice_culori(nr_randuri, nr_coloane):
    """
    Generează o matrice de culori aleatorii (RGB) de dimensiunea specificată.
    """
    return [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(nr_coloane)
        ]
        for _ in range(nr_randuri)
    ]

# Configurarea ferestrei de afisare
ecran = pygame.display.set_mode((LATIME_FEREASTRA, INALTIME_FEREASTRA))
pygame.display.set_caption("Grid de Culori Procedural - Regenerare la 5 secunde")

# Starea initiala
matrice_culori = genereaza_matrice_culori(RANDURI, COLOANE)
timp_ultima_actualizare = pygame.time.get_ticks()
este_activ = True

# Bucla principala a programului
while este_activ:
    # 1. Gestionarea Evenimentelor
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            este_activ = False
        
        # Regenerare manuala la apasarea tastei SPACE
        if eveniment.type == pygame.KEYDOWN:
            if eveniment.key == pygame.K_SPACE:
                matrice_culori = genereaza_matrice_culori(RANDURI, COLOANE)
                timp_ultima_actualizare = pygame.time.get_ticks()

    # 2. Logica de regenerare automata (la fiecare 5 secunde)
    timp_curent = pygame.time.get_ticks()
    if timp_curent - timp_ultima_actualizare >= INTERVAL_REGENERARE:
        matrice_culori = genereaza_matrice_culori(RANDURI, COLOANE)
        timp_ultima_actualizare = timp_curent

    # 3. Randarea (Desenarea pe ecran)
    ecran.fill((0, 0, 0)) 

    for y in range(RANDURI):
        for x in range(COLOANE):
            culoare = matrice_culori[y][x]
            dreptunghi = (x * DIMENSIUNE_CELULA, y * DIMENSIUNE_CELULA, DIMENSIUNE_CELULA, DIMENSIUNE_CELULA)
            pygame.draw.rect(ecran, culoare, dreptunghi)

    # Actualizarea afisajului
    pygame.display.flip()

# Inchiderea corecta a programului
pygame.quit()