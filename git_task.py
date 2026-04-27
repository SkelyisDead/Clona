import time

"""
Acest script reprezinta rezolvarea task-urilor combinate.
Scopul sau este de a afisa un mesaj de salut pe ecran la fiecare 5 secunde,
respectand normele de coding style.
"""

def afiseaza_mesaj_salut():
    """
    Aceasta functie defineste si afiseaza mesajul 'Hello World' in consola.
    """
    # Definim o variabila cu un nume sugestiv care stocheaza textul dorit
    mesaj = "Hello World"
    
    # Afisam variabila pe ecran
    print(mesaj)

# Verificam daca scriptul este rulat direct
if __name__ == "__main__":
    
    # Bucla principala care ruleaza la nesfarsit
    while True:
        afiseaza_mesaj_salut()  # 1. Afisam rezultatul
        time.sleep(5)           # 2. Punem programul pe pauza pentru 5 secunde