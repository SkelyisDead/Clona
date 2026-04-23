import time

def calculeaza_suma_numere(primul_numar, al_doilea_numar):
    """
    Această funcție primește două numere întregi și returnează suma lor.
    Respectă regula numelor sugestive pentru funcții și variabile.
    """
    # Spațiere corectă în jurul operatorului '+'
    rezultat = primul_numar + al_doilea_numar
    return rezultat

def main():
    # Variabile cu nume descriptive în loc de a, b, c 
    valoare_stanga = 5
    valoare_dreapta = 10

    print("Programul a pornit. Rezultatul se va regenera la fiecare 5 secunde.")

    try:
        while True:
            # Apelăm funcția de calcul
            suma_finala = calculeaza_suma_numere(valoare_stanga, valoare_dreapta)
            
            # Afișăm rezultatul cu o indentare corectă
            print(f"[{time.strftime('%H:%M:%S')}] Suma numerelor este: {suma_finala}")
            
            # Cerința: Regenerarea rezultatului o dată la 5 secunde 
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nProgram oprit de utilizator.")

if __name__ == "__main__":
    main()