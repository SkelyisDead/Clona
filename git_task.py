import time

def calculeaza_suma(limita):
    rezultat = sum(range(1, limita + 1))
    return rezultat

numar_limita = 10

while True:
    rezultat_final = calculeaza_suma(numar_limita)
    
    print(f"Rezultatul este: {rezultat_final}")
    print("Se regenereaza in 5 secunde...")
    
    time.sleep(5)
