import time

# Funcție cu nume sugestiv pentru adunarea a două numere
def aduna_doua_numere(primul_numar, al_doilea_numar):
    return primul_numar + al_doilea_numar

while True:
    suma_totala = aduna_doua_numere(5, 10)
    print("Rezultatul adunării este:", suma_totala)
    
    # Punem programul pe pauză 5 secunde înainte să o ia de la capăt
    time.sleep(5)