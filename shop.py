# Klasa sklepu internetowego- atrybuty:
#
# Konstruktor domyslny - zaczynamy od braku danych,
# dopiero w trakcie dzialania sklepu beda one dodawane
# clients - liczba klientow odwiedzajacych sklep w jednym dniu
# prod1 - liczb produktow wyswietlonych
# prod2 - liczba produktow dodanych do koszyka
# prod3 - liczba produktow, ktore zostaly sprzedane
# performance - wydajnosc serwera :

# Wydajnosc zalezy od wielu czynnikow, np: liczby odwiedzajacych, ilosci produktow w sklepie,
# Mozna zalozyc jakas liczbe na poczatek np 80 i zwiekszac ja np w momencie wiekszej liczby klientow na stronie
# Albo w momencie
# Zakladamy, ze strona internetowa jest postawiona na dwoch serwerach, zatem:

# runServers (running servers) - liczba oznaczajaca dzialajace serwery - na poczatku 2
# W trakcie dzialania programu ta liczba moze ulec zmianie, poniewaz ktorys z serwerow mogl ulec awarii
# Ilosc dzialacych serwerow bedzie wplywala na wydajnosc
# error - numer/rodzaj awarii/bledu na serwerze
# repairTime - w zaleznosci od tego, jaki blad wystapil - czas naprawy bedzie rowny - W TYM CZASIE STRONA JEST SPOWOLNIONA, ALE JAKOS DZIALA
# breakTime - czas przerwy po wystapieniu bledu - strona internetowa zamrożona, nic sie nie dzieje do momentu naprawienia
# speed - predkosc [%]

class Shop:
    def __init__(self, clients=0, performance=80, runServers=3, error=0, repairTime=0, breakTime=0, speed=100):
        self.clients = clients
        self.performance = performance
        self.runServers = runServers
        self.error = error
        self.repairTime = repairTime
        self.breakTime = breakTime
        self.speed = speed

    def shopErrors(self):
        #spowalnia prace serwera o 2%
        if (self.error == 304):
            self.speed = self.speed - 2
            self.error = 0                  # Po wystapieniu bledu, ustawienie go z powrotem na 0

        if (self.error == 400):
            self.breakTime = 2
            self.error = 0

        if (self.error == 401):
            self.breakTime = 1
            self.error = 0

        if (self.error == 403):
            self.breakTime = 1
            self.error = 0

        if (self.error == 404):
            self.error = 0

        if (self.error == 405):
            self.error = 0

        if (self.error == 408):
            self.breakTime = 2
            self.error = 0

        if (self.error == 410):
            self.error = 0

        if (self.error == 429):
            self.breakTime = 2
            self.error = 0

        if (self.error == 499):
            self.error = 0

        if (self.error == 500):
            self.error = 0

        # Awaria jednego z serwerow!!!
        if (self.error == 501):
            self.runServers = self.runServers - 1
            self.error = 0

        if (self.error == 502):
            self.error = 0

        if (self.error == 503):
            self.error = 0

        if (self.error == 504):
            self.error = 0

    def conditoins(self):

        if (self.clients >= 10000):         # Zwiekszyc ta liczbe, 10 000 tylko do testow
            # Jezeli ilosc klientow na stronie danego dnia przekroczy dana ilosc to nastepuje spowolnienie pracy serwera o 5%
            self.speed = self.speed - 5

    # Funkcja ustawia czas naprawy danego bledu/awarii
    def checkShop(self):
        # Sprawdzenie stanu sklepu

        # 1. Dzialace serwery
        if(self.runServers == 1):
            #self.speed = self.speed - 50
            self.breakTime = 7                                        # Jezeli duration bedzie 1000 to ustawic np na 100 (7 bylo git dla duration 10, dla 100 zwiekszyc)
            self.runServers = 3
            # Ustawic na wiecej niz duration breakTime zeby naprawa zajela pare dni

        # 2. Predkosc serwera
        if(self.speed == 50):
            print("Predkosc serwera spadla do 50% lub mniej")

        # 3. Jezeli czas naprawy serwera = 0, to przywrocic sprawnosc dwoch serwerow
        #if(self.breakTime == 0):
            #self.runServers = 2