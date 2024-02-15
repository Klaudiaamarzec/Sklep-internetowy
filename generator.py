import time

# Generator liczb pseudolosowych
# Generator LCG

class LCG:
    # Jezeli ziarno nie jest podane, generator zostanie
    # zinicjalizowany aktualnym czasem systemowym
    def __init__(self, seed=None):
        self.seed = seed
        if seed is not None:
            self.state = seed
        else:
            self.state = int(time.time())

    # Jest to przedzial <) !! Trzeba o tym pamietac
    # Mozna zmienic

    def rand(self, min=0, max=1000000):  # usunac przypisywanie wartosci? Bo i tak beda uzupelniane podczas wywolywania funkcji
        a = 1664525
        c = 1013904223
        m = 2 ** 32
        self.state = (a * self.state + c) % m
        r = self.state / m
        return int(r * ((max - min + 1) // 2 + 1) * 2) + min
        #return min + (self.state % (max - min))