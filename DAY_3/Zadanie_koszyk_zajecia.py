class Ksiazka(object):
    def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
        self.tytul = tytul
        self.autor = autor
        self.ilosc_stron = ilosc_stron
        self.cena = cena
        self.vat = 7
    def __str__(self):
        return f"{self.tytul}, autor: {self.autor}"
    def __len__(self):
        return self.ilosc_stron
    def __add__(self, other):
        if isinstance(other, Ksiazka):
            return self.ilosc_stron + other.ilosc_stron
        else:
            print('Tak naprawdę nic nie dodałem')
            return self.ilosc_stron
    def cena_brutto(self):
        return round(self.cena * (100 + self.vat), 2)

class Ebook(Ksiazka):
    def __init__(self, tytul, autor):
        super().__init__(tytul, autor)
        self.format = 'pdf'
        self.vat = 23

class Koszyk():
    def __init__(self):
        self.elementy = []
        self.ilosc_elementow = 0
        self.netto = 0
        self.brutto = 0

    def dodaj(self, element):
        self.elementy.append(element)
        self.ilosc_elementow += 1
        self.netto = self.netto + element.cena
        self.brutto = self.brutto + element.cena_brutto()

    def __len__(self):
        return len(self.elementy)

    def wartosc_netto(self):
        return self.netto

    def wartosc_brutto(self):
        return self.brutto

ksiazka_1 = Ksiazka('Potop','Sienkiewicz', 300)
ebook_1 = Ebook('Potop', 'Sienkiewicz')

print(ksiazka_1)
print(ksiazka_1.vat)
print(ebook_1)
print(ebook_1.autor)

moj_koszyk = Koszyk()
moj_koszyk.dodaj(ksiazka_1)
print(moj_koszyk.netto)
print(moj_koszyk.elementy)
print(moj_koszyk.ilosc_elementow)
