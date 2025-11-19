#import silnia, piramida, radius, box_drawing, rok_przestepny, rozmienianie_monet, dziesietna, kalkulator_temperatur
import prostokat
import dziesietna
import kalkulator_temperatur
import piramida
import promien_kola
import rok_przestepny
import rozmienianie_monet
import silnia

print("Zadania:\n"
      "1. kalkulator_temperatur\n"
      "2. silnia\n"
      "3. piramida\n"
      "4. promien_kola\n"
      "5. prostokat\n"
      "6. rok_przestepny\n"
      "7. rozmienianie_monet\n"
      "8. dziesietna\n")

user_ask = True
while user_ask is True:
    zapytanie = input("Wybierz program z powyzszych, ktory chcesz uruchomic: ")
    if zapytanie.isdigit():
        zapytanie = int(zapytanie)
        if zapytanie == 1:
            kalkulator_temperatur.kalkulator_temperatur()
        elif zapytanie == 2:
            silnia.silnia()
        elif zapytanie == 3:
            piramida.piramida()
        elif zapytanie == 4:
            promien_kola.radius()
        elif zapytanie == 5:
            prostokat.box_drawing()
        elif zapytanie == 6:
            rok_przestepny.rok_przestepny()
        elif zapytanie == 7:
            rozmienianie_monet.rozmienianie_monet()
        elif zapytanie == 8:
            dziesietna.dziesietna()
        else:
            print("Podaj poprawnie dane")
    elif zapytanie == 'k':
        user_ask = False
    else:
        print("Podaj poprawnie dane")











