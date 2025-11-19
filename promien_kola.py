# 2. Napisz program do obliczania pola powierzchni koła o zadanym promieniu
# (wyświetlając wzór i kolejne obliczenia)
def radius():

    import math

    user_ask = True
    while user_ask is True:
        radius_input = input('Podaj promien kola: ')
        if radius_input.isdigit():
            radius = int(radius_input)
            area_of_circle = math.pi * radius ** 2
            print(f'Pole okregu o podanym promieniu {radius_input} wynosi {area_of_circle:.2f} ') #zaokroaglony
            break
        else :
            print(f'Promien kola musi byc liczba. Podaj promien jeszcze raz.')
            continue