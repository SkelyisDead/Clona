import pygame
import random

#Initializam pygame
pygame.init()

def generate_color_grid():
 #Genereaza o matrice 10x10 de culori RGB aleatorii
 return [[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(10)] for _ in range(10)]

#Cream fereastra de 500x500 pixeli si setam titlul
screen=pygame.display.set_mode((500,500));
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)");

#Generam prima grila de culori
data=generate_color_grid();

#Setam un timer care va declansa un eveniment la fiecare 5 secunde pentru a regenera grila automat
TIMER = pygame.USEREVENT
pygame.time.set_timer(TIMER, 5000)

#Variabila care mentine bucla de rulare a jocului
is_running=True;

while is_running:
 #Curatam ecranul cu negru
 screen.fill((0,0,0))

#Parcurgem liniile si coloanele matricei de culori
 for y in range(10):
  for x in range(10):
   #Desenma fiecare patratel de 50x50 pixeli cu culoarea corespunzatoare din matrice
   pygame.draw.rect(screen,data[y][x],(x*50,y*50,50,50))

#Afisam pe ecran ce am creat
 pygame.display.flip()

 #Verificam evenimentele
 for event in pygame.event.get():
  #Daca utilizatorul inchide fereastra, oprim bucla
  if event.type==pygame.QUIT:
   is_running=False

  #Daca utilizatorul apasa SPACE, generam o noua grila de culori
  if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
   data=generate_color_grid()

  if event.type==TIMER:
   data=generate_color_grid()

#Inchidem pygame   
pygame.quit()