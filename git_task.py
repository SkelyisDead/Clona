import time
import random

def genereaza_numar_aleator(minim, maxim):
    """
    Aceasta functie genereaza un numar intreg aleatoriu intre doua limite.
    Respecta normele de coding style (PEP8).
    """
    rezultat = random.randint(minim, maxim)
    return rezultat

if __name__ == "__main__":
    print("Programul a pornit. Rezultatul se va regenera la fiecare 5 secunde...")
    
    try:
        while True:
            # Generam si afisam un numar nou
            numar_nou = genereaza_numar_aleator(1, 100)
            print(f"Numar generat: {numar_nou}")
            
            # Asteptam 5 secunde conform cerintei
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nProgram oprit de utilizator.")