import time

def afiseaza_mesaj_repetitiv():
    """Afiseaza un mesaj pe ecran la un interval regulat."""
    mesaj = "Rezultatul a fost generat!"
    print(mesaj)

if __name__ == "__main__":
    interval_secunde = 5
    
    # Bucla care ruleaza la infinit
    while True:
        afiseaza_mesaj_repetitiv()
        # Asteapta 5 secunde inainte de urmatoarea executie
        time.sleep(interval_secunde)