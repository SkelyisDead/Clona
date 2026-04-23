import pygame
import random

# 1. Initializam modulele pygame
pygame.init()

def genereaza_matrice_culori():
    # Genereaza o matrice de 10x10 cu tupluri de culori RGB aleatoare
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

# 2. Setam dimensiunile ecranului si titlul ferestrei (spatiere corecta la egal)
dimensiune_fereastra = (500, 500)
ecran = pygame.display.set_mode(dimensiune_fereastra)
pygame.display.set_caption("Procedural Color Grid (Regenerare automata la 5 secunde)")

# 3. Initializam datele si starea aplicatiei cu nume sugestive
matrice_culori = genereaza_matrice_culori()
ruleaza = True

# 4. Cream un eveniment personalizat care se declanseaza la fiecare 5 secunde (5000 milisecunde)
EVENIMENT_REGENERARE = pygame.USEREVENT + 1
pygame.time.set_timer(EVENIMENT_REGENERARE, 5000)

# Bucla principala a jocului
while ruleaza:
    # Completam fundalul cu negru
    ecran.fill((0, 0, 0))
    
    # Desenam grila de culori (Indentare corecta cu 4 spatii pentru fiecare nivel)
    for rand in range(10):
        for coloana in range(10):
            culoare = matrice_culori[rand][coloana]
            coordonata_x = coloana * 50
            coordonata_y = rand * 50
            pygame.draw.rect(ecran, culoare, (coordonata_x, coordonata_y, 50, 50))
            
    # Actualizam afisajul pe ecran
    pygame.display.flip()
    
    # Verificam evenimentele utilizatorului si ale sistemului
    for eveniment in pygame.event.get():
        
        # Daca utilizatorul inchide fereastra din 'X', oprim bucla
        if eveniment.type == pygame.QUIT:
            ruleaza = False
            
        # Daca au trecut 5 secunde (timer-ul a declansat evenimentul), regeneram culorile
        if eveniment.type == EVENIMENT_REGENERARE:
            matrice_culori = genereaza_matrice_culori()

        # Regenerarea manuala la apasarea tastei SPACE
        if eveniment.type == pygame.KEYDOWN and eveniment.key == pygame.K_SPACE:
            matrice_culori = genereaza_matrice_culori()

# Inchidem pygame in siguranta
pygame.quit()