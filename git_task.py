import pygame
import random
import time

# --- CONFIGURARE CONSTANTE ---
LATIME_FEREASTRA = 500
INALTIME_FEREASTRA = 500
DIMENSIUNE_PATRAT = 50
NR_COLOANE = 10
NR_RANDURI = 10
SECUNDE_REGENERARE = 5

def genereaza_matrice_culori():
    """
    Creeaza o lista de liste (matrice) care contine culori RGB aleatorii.
    Fiecare element este un tuplu de forma (R, G, B).
    """
    matrice = []
    for _ in range(NR_RANDURI):
        rand_nou = []
        for _ in range(NR_COLOANE):
            # Generam o culoare random: (rosu, verde, albastru)
            culoare_rgb = (
                random.randint(0, 255), 
                random.randint(0, 255), 
                random.randint(0, 255)
            )
            rand_nou.append(culoare_rgb)
        matrice.append(rand_nou)
    return matrice

def main():
    # Initializam motorul grafic
    pygame.init()
    ecran = pygame.display.set_mode((LATIME_FEREASTRA, INALTIME_FEREASTRA))
    pygame.display.set_caption("Laborator IS1 - Procedural Grid")

    # Initializam datele de start
    date_grid = genereaza_matrice_culori()
    timp_ultima_actualizare = time.time()
    ruleaza = True

    # Bucla principala a programului
    while ruleaza:
        # 1. Verificam daca s-a inchis fereastra
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:
                ruleaza = False

        # 2. Logica de regenerare automata (Cerinta: o data la 5 secunde)
        timp_acum = time.time()
        if timp_acum - timp_ultima_actualizare >= SECUNDE_REGENERARE:
            date_grid = genereaza_matrice_culori()
            timp_ultima_actualizare = timp_acum
            print("Grid-ul a fost regenerat automat!")

        # 3. Desenarea pe ecran
        ecran.fill((0, 0, 0))  # Fundal negru
        
        for y in range(NR_RANDURI):
            for x in range(NR_COLOANE):
                culoare = date_grid[y][x]
                forma_patrat = (
                    x * DIMENSIUNE_PATRAT, 
                    y * DIMENSIUNE_PATRAT, 
                    DIMENSIUNE_PATRAT, 
                    DIMENSIUNE_PATRAT
                )
                pygame.draw.rect(ecran, culoare, forma_patrat)

        # Actualizam ce vede utilizatorul
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()