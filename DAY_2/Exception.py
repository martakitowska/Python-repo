try:
    print('Blok kodu który może powodować błąd')
    wynik = 15 / 0
    # wynik = nieznana_zmienna # NameError
    # list = []
    # list[10] #IndexError
except NameError as e:
    print(f'Brak zmiennej')
except Exception as e:
    print(f'Błąd dzielenia, komunikat systemowy "{e}"')
else:
    print('Gdy nie ma błędu')
finally:
    print('Zawsze')

try:
    liczba = float(input('Podaj liczbę: '))
except: #nie trzeba podawać nazwfy wyjątku
    print('To nie jest liczba :(')
else:
    print('Dzięki to jest liczba!')