import time

def afiseaza_mesaj_periodic():

    mesaj_de_afisat = "Hello World"
    timp_asteptare_secunde = 5
    
    while True:
        print(mesaj_de_afisat)
        
        time.sleep(timp_asteptare_secunde)

if __name__ == "__main__":
    afiseaza_mesaj_periodic()