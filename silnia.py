# Napisz program do wyliczania silni dla zadanej liczby

user_ask = True
while user_ask is True:
    zapytanie = input("Podaj liczbe do wyliczenia silni: ")
    if zapytanie.isdigit():
        zapytanie = int(zapytanie)
        if zapytanie==0:
            print('Silnia wynosi: 0')
        elif zapytanie > 1:
            wynik = 1
            for i in range(1, zapytanie + 1):
                wynik *= i
            print(wynik)
            break
    else:
        print("Podaj poprawne dane.")




