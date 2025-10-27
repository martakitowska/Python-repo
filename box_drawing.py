'''Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
    | (bok)
    - (góra/dół)
    + (wierzchołek)
    czyli np:
    +---+
    |       |
    |       |
    +---+'''

#print('-' * 20, "PROSTOKAT",'-' * 20 )

print('MOJ PIEKNY PROSTOKAT')
ask_user = True
while ask_user is True:
    wysokosc = input('Podaj wysokosc prostokata: ')
    szerokosc = input('Podaj szerokosc prostokata: ')
    if wysokosc.isdigit() and szerokosc.isdigit():
        wysokosc = int(wysokosc)
        szerokosc = int(szerokosc)
        if wysokosc > 1 and szerokosc > 1:
            print('*','-' * (szerokosc -2),'*')
            i=0
            while i < (wysokosc - 2):
                print("|", " " * (szerokosc - 2), "|")
                i +=1
            print('*','-' * (szerokosc -2),'*')
            break
        else:
            print('Szerokosc badz wysokosc sa za male, zeby narysowac prostakat')
            continue
    elif wysokosc.isdigit() or szerokosc.isdigit():
        print('Szerokosc i wysokosc musza byc liczba.')
    else:
        print("Podaj poprawne wartosci liczbowe.")


