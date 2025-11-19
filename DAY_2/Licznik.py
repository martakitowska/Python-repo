def licznik():
    try:
        # otwiera plik do odczytu i zapisu ale go nie tworzy
        with open('licznik.txt', 'r+') as plik:
            #odczytujemy stan licznika w pliku
            ilosc_uruchomien = plik.read()

            try:
                # z pliku zawsze mamy str więc zamieniamy na int i inkrementujemy (zwiększamy) o jeden
                ilosc_uruchomien = int(ilosc_uruchomien)
                ilosc_uruchomien += 1
            except:
                # w każdym innym przyadku ustalamy wartość początkową na 1
                ilosc_uruchomien = 1

            # po odczycie kursor w pliku ustawiony jest na koniec - można to sprawdzić metodą .tell()
            # tak więc ustawiamy go na początek pliku
            # by nadpisać wartość a nie dodać na koniec pliku
            plik.seek(0)

            # zapisujemy do pliku .write() przyjmuje str więc rzutujemy przed zapisem
            plik.write(str(ilosc_uruchomien))

            print(f"=={ilosc_uruchomien}==")
    except FileNotFoundError:
        # jeśli pliku nie ma to tworzymy go i wpisujemy wartość początkową 1
        with open('licznik.txt', 'w') as plik:
            plik.write("1")
            print("1")

# każde wywołanie funkcji zwiększa licznik w pliku o jeden
licznik()