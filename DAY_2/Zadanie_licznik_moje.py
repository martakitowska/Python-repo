with open('input.txt', 'r+') as f:
    licznik = f.read()
    #print(f'Otworzylem {licznik} razy')
    licznik = int(licznik)
    licznik +=1
    licznik = str(licznik)
    f.seek(0)
    f.write(licznik)