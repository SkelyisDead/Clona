import pygame
import random

# Definirea constantelor pentru a evita "numerele magice" în cod
LATIME_FEREASTRA = 500
INALTIME_FEREASTRA = 500
DIMENSIUNE_CELULA = 50
NUMAR_CELULE = 10
TIMP_REGENERARE_MS = 5000  # 5 secunde (exprimate în milisecunde)

def genereaza_grila_culori():
    """
    Generează o matrice 10x10 ce conține culori RGB (Red, Green, Blue) 
    alese în mod complet aleatoriu.
    """
    # Am rescris lista comprehensivă pe mai multe rânduri pentru lizibilitate
    grila = [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
            for _ in range(NUMAR_CELULE)
        ] 
        for _ in range(NUMAR_CELULE)
    ]
    return grila

def main():
    """
    Funcția principală care inițializează și rulează aplicația Pygame.
    """
    # 1. Inițializarea aplicației
    pygame.init()
    ecran = pygame.display.set_mode((LATIME_FEREASTRA, INALTIME_FEREASTRA))
    pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")
    
    # 2. Setarea stării inițiale
    grila_culori = genereaza_grila_culori()
    ruleaza = True
    
    # Creăm un eveniment personalizat care se va declanșa o dată la 5 secunde
    EVENIMENT_REGENERARE = pygame.USEREVENT + 1
    pygame.time.set_timer(EVENIMENT_REGENERARE, TIMP_REGENERARE_MS)
    
    # 3. Bucla principală a jocului
    while ruleaza:
        # Curățăm ecranul cu negru la fiecare cadru
        ecran.fill((0, 0, 0))
        
        # Desenăm grila de celule pe ecran
        for y in range(NUMAR_CELULE):
            for x in range(NUMAR_CELULE):
                culoare = grila_culori[y][x]
                dreptunghi = (x * DIMENSIUNE_CELULA, y * DIMENSIUNE_CELULA, 
                              DIMENSIUNE_CELULA, DIMENSIUNE_CELULA)
                pygame.draw.rect(ecran, culoare, dreptunghi)
        
        # Actualizăm fereastra pentru a afișa noile desene
        pygame.display.flip()
        
        # 4. Gestionarea evenimentelor
        for eveniment in pygame.event.get():
            # Utilizatorul a apăsat pe butonul [X] pentru a închide fereastra
            if eveniment.type == pygame.QUIT:
                ruleaza = False
                
            # Timer-ul de 5 secunde s-a declanșat
            elif eveniment.type == EVENIMENT_REGENERARE:
                grila_culori = genereaza_grila_culori()

    # Închidem aplicația în mod curat la ieșirea din buclă
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()