# time - czas klienta spedzony na stronie
# products - produkty dodane do koszyka
# device - urzadzenie, z ktorego korzysta uzytkownik -> SZYBKOŚĆ ŁADOWANIA STRONY

class Client:
    def __init__(self, time, products, device):
        self.time = time
        self.products = products
        self.device = device