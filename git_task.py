import pygame
import random
import time

pygame.init()

def genereaza_matrice_culori(randuri=10, coloane=10):
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
         for _ in range(coloane)] 
        for _ in range(randuri)
    ]
 
def randeaza_grila(suprafata, date_grila, dimensiune_celula=50):
    for y, rand in enumerate(date_grila):
        for x, culoare in enumerate(rand):
            pygame.draw.rect(
                suprafata, 
                culoare, 
                (x * dimensiune_celula, y * dimensiune_celula, dimensiune_celula, dimensiune_celula)
            )

def main():
    latime, inaltime = 500, 500
    ecran = pygame.display.set_mode((latime, inaltime))
    pygame.display.set_caption("Grilă Culori - Regenerare Automată (5s)")
    date_culori = genereaza_matrice_culori()
    ruleaza = True
    ultima_actualizare = time.time()  # Monitorizăm timpul pentru regenerare

    while ruleaza:
        ecran.fill((0, 0, 0))
        timp_curent = time.time()
        if timp_curent - ultima_actualizare >= 5:
            date_culori = genereaza_matrice_culori()
            ultima_actualizare = timp_curent
            print(f"[{time.strftime('%H:%M:%S')}] Grila a fost regenerată automat.")
        randeaza_grila(ecran, date_culori)
        pygame.display.flip()

        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:
                ruleaza = False
            if eveniment.type == pygame.KEYDOWN:
                if eveniment.key == pygame.K_SPACE:
                    date_culori = genereaza_matrice_culori()
                    ultima_actualizare = time.time()
    pygame.quit()

if __name__ == "__main__":
    main()
