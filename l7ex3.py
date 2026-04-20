import time

def afiseaza_mesaj_periodic():
    """
    Această funcție afișează mesajul 'Hello World' pe ecran
    o dată la fiecare 5 secunde, într-o buclă infinită.
    """
    # Definim variabile cu nume sugestive
    mesaj_de_afisat = "Hello World"
    timp_asteptare_secunde = 5
    
    # Buclează la nesfârșit pentru a regenera rezultatul
    while True:
        print(mesaj_de_afisat)
        
        # Oprește execuția programului pentru timpul specificat
        time.sleep(timp_asteptare_secunde)

# Punctul de intrare în program
if __name__ == "__main__":
    afiseaza_mesaj_periodic()
