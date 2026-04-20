import time

# Funcție cu nume descriptiv care calculează suma
def calculeaza_suma(numar_unu, numar_doi):
    """Calculează și returnează suma a două numere."""
    return numar_unu + numar_doi

def main():
    # Variabile cu nume sugestive
    termen_unu = 5
    termen_doi = 10
    
    while True:
        rezultat = calculeaza_suma(termen_unu, termen_doi)
        print(f"Rezultatul este: {rezultat}")
        
        # Regenerare rezultat la fiecare 5 secunde [cite: 214]
        time.sleep(5)

if __name__ == "__main__":
    main()
