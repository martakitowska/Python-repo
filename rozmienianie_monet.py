#Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na
# monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.


kwota = input('Podaj kwotę do rozmienienia na drobne: ')

monety = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
wynik = {}
if kwota.isdigit():
    kwota = int(kwota)
    for x in monety:
        liczba_monet = kwota / x
        wynik[x] = liczba_monet
        kwota = round(kwota - liczba_monet * x, 2)
        print(f'{x} zl - {liczba_monet}')

print(wynik)



