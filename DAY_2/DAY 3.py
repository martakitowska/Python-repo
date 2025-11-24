produkt_1 = Ksiazka('Pan Tadeusz', liczba_stron = 200, cena_netto= 25.99)
produkt_1 = Ksiazka('Potop', liczba_stron = 200, cena_netto= 27.99)
produkt_1 = Ksiazka('Superman', liczba_stron = 20, cena_netto= 9.99, universum = 'Marvell')

koszyk.dodaj(produkt_1)
koszyk.dodaj(produkt_2)
koszyk.dodaj(produkt_3)

koszyk.zamow(klient)
koszyk.wyslij(adres)

lub

zamowienie.dodaj(koszyk)
zamowienie.realizuj(koszyk)