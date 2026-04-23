import pygame
import random


def generate_color_grid():
 # Genereaza o matrice 10x10 de culori RGB aleatorii
 return [
  [
   (random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(10)
   ] for _ in range(10)
   ]

def main():
 pygame.init()
screen=pygame.display.set_mode((500,500));
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)");
#in cazul in care se doreste o matrice de culori statica, se poate apela o singura data functia generate_color_grid() inainte de loop-ul principal
data=generate_color_grid();running=True

while running:
 screen.fill((0,0,0))
 for y in range(10):
  for x in range(10):
   pygame.draw.rect(screen,data[y][x],(x*50,y*50,50,50))
   # fiecare patrat are dimensiunea de 50x50 pixeli, iar pozitia sa este calculata in functie de indexul sau in matricea de culori
 pygame.display.flip()
 for event in pygame.event.get():
  running=False if event.type==pygame.QUIT else running;
  #daca se doreste regenerarea matricei de culori la fiecare apasare a tastei SPACE, se poate actualiza variabila data in acest moment
  data=generate_color_grid() if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE else data
pygame.quit()