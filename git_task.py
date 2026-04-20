import pygame
import random
import time

# Constante pentru configurare ușoară
LATIME_ECRAN = 500
INALTIME_ECRAN = 500
DIMENSIUNE_CELULA = 50
NR_COLOANE = 10
NR_RANDURI = 10
INTERVAL_REGENERARE = 5 # secunde

def creeaza_grila_culori():
    """
    Generează o matrice 10x10 de culori RGB aleatorii.
    Fiecare element este un tuplu (R, G, B).
    """
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(NR_COLOANE)] 
        for _ in range(NR_RANDURI)
    ]

def main():
    pygame.init()
    
    ecran = pygame.display.set_mode((LATIME_ECRAN, INALTIME_ECRAN))
    pygame.display.set_caption("Grilă Procedurală - Refresh la 5s")

    # Inițializare variabile de control
    matrice_culori = creeaza_grila_culori()
    ruleaza = True
    timp_ultimul_refresh = time.time()

    while ruleaza:
        # 1. Gestionare Evenimente
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:
                ruleaza = False

        # 2. Logică - Verificăm dacă au trecut 5 secunde
        timp_curent = time.time()
        if timp_curent - timp_ultimul_refresh >= INTERVAL_REGENERARE:
            matrice_culori = creeaza_grila_culori()
            timp_ultimul_refresh = timp_curent
            print(f"Grila a fost regenerată la: {time.strftime('%H:%M:%S')}")

        # 3. Desenare (Rendering)
        ecran.fill((0, 0, 0)) # Fundal negru

        for r in range(NR_RANDURI):
            for c in range(NR_COLOANE):
                culoare = matrice_culori[r][c]
                # Calculăm poziția dreptunghiului pe baza indicilor din matrice
                pygame.draw.rect(
                    ecran, 
                    culoare, 
                    (c * DIMENSIUNE_CELULA, r * DIMENSIUNE_CELULA, DIMENSIUNE_CELULA, DIMENSIUNE_CELULA)
                )

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()