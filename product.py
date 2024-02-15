class Product:  # Klasa Product zawierająca wartosci value

    def __init__(self, index, price, amount, value1=0, value2=0, value3=0):
        self.index = index
        self.price = price
        self.amount = amount
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __str__(self):
        return f"{self.index} {self.price} {self.amount} {self.value1} {self.value2} {self.value3}"

    def condition1(self):
        if (self.value3 >= 100):
            print("Produkt o indeksie " + str(self.index) + " zostal wyswietlony wiecej niz 5 razy")

    def clear(self):
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0
