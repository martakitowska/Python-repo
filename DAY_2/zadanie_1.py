"""10. Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak, np:
   ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
   Niech będzie możliwość wyboru tryb case sensitivity.
   Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
   "
   Ilość uruchomień programu:
   10
   Przeanalizowanych znaków:
   1223435991
   Znalezionych wyrazów:
   2399
   Znalezionych liczb:
   122
   Znalezionych małych liter:
   68923455
   etc
   "

   Oczywiście dopuszalna jest ułomność takiego programu.
   Dokładne policzenie ilość zdań nie jest trywialne ale może jakiś fajny algorytm uda się Wam wymyślić.
   Rodzaje statystyk zostawiam waszej fantazji :)
   Przydatny generator tekstu: http://lipsum.pl/"""

# Importujemy moduły, które są potrzebne.
# 'os' jest potrzebne do sprawdzania, czy plik istnieje.
# 'string' ma fajne gotowe listy liter i cyfr.
import os
import string

# --- Ustawienia programu ---
NAZWA_PLIKU_WEJSCIOWEGO = "tekst_do_analizy"
NAZWA_PLIKU_STATYSTYK_PROGRAMU = "moje_statystyki_pracy.txt"

# Zmienna przechowująca, czy liczymy małe i duże litery osobno.
# Prawda (True) - liczymy osobno. Fałsz (False) - najpierw zmieniamy na małe.
CZY_CASE_SENSITIVE = True


# UWAGA: Zmień na False, jeśli chcesz ignorować wielkość liter!

# --- KROK 1: Funkcja do wczytania statystyk programu ---
# Tę funkcję zrobimy, żeby program pamiętał, ile razy był już uruchomiony.
def wczytaj_statystyki_programu():
    # Ustawiamy domyślne statystyki na start
    statystyki_ogolne = {
        "ilosc_uruchomien": 0,
        "sum_znakow": 0,
        "sum_wyrazow": 0,
        "sum_liczb": 0
    }

    # Sprawdzamy, czy plik ze statystykami programu już istnieje.
    if os.path.exists(NAZWA_PLIKU_STATYSTYK_PROGRAMU):
        print("INFO: Znaleziono poprzednie statystyki programu, wczytuję...")
        # Staramy się otworzyć plik
        try:
            with open(NAZWA_PLIKU_STATYSTYK_PROGRAMU, 'r', encoding='utf-8') as plik:
                linie = plik.readlines()
                for linia in linie:
                    # Szukamy klucza i wartości oddzielonych dwukropkiem
                    if ":" in linia:
                        klucz, wartosc = linia.split(":", 1)
                        klucz = klucz.strip()  # usuwamy spacje
                        # Staramy się zamienić wartość na liczbę, bo to są liczniki
                        try:
                            liczba = int(wartosc.strip())
                            # Sprawdzamy, który klucz znaleźliśmy i aktualizujemy słownik
                            if klucz == "Ilość uruchomień programu":
                                statystyki_ogolne["ilosc_uruchomien"] = liczba
                            elif klucz == "Przeanalizowanych znaków":
                                statystyki_ogolne["sum_znakow"] = liczba
                            elif klucz == "Znalezionych wyrazów":
                                statystyki_ogolne["sum_wyrazow"] = liczba
                            elif klucz == "Znalezionych liczb":
                                statystyki_ogolne["sum_liczb"] = liczba
                        except ValueError:
                            # Jeśli coś się zepsuje i nie jest to liczba, po prostu to ignorujemy
                            pass
        except Exception as e:
            print(f"Ojej! Wystąpił błąd przy wczytywaniu statystyk programu: {e}")

    return statystyki_ogolne


# --- KROK 2: Główna funkcja analizująca tekst ---
def analizuj_tekst():
    print("---------------------------------------")
    print(f"START: Zaczynam analizę pliku: {NAZWA_PLIKU_WEJSCIOWEGO}")

    # Sprawdzamy, czy plik wejściowy istnieje
    if not os.path.exists(NAZWA_PLIKU_WEJSCIOWEGO):
        print(f"BŁĄD: Nie ma pliku '{NAZWA_PLIKU_WEJSCIOWEGO}'! Utwórz go i wklej tekst.")
        return None  # Przerywamy działanie

    # Wczytujemy cały tekst z pliku
    try:
        with open(NAZWA_PLIKU_WEJSCIOWEGO, 'r', encoding='utf-8') as plik:
            tekst = plik.read()
    except Exception as e:
        print(f"BŁĄD: Nie udało się wczytać pliku: {e}")
        return None

    # Słownik, w którym będziemy zapisywać wyniki tej konkretnej analizy
    wyniki_analizy = {}

    # 1. Zliczamy podstawowe rzeczy
    wyniki_analizy["Liczba wszystkich znaków (włączając spacje, itd)"] = len(tekst)

    # 2. Liczymy wyrazy
    # Najprostszy sposób dla początkującego: dzielimy tekst po spacjach.
    # W ten sposób wciąż będziemy mieli znaki interpunkcyjne, ale jest to proste.
    wyrazy = tekst.split()  # Dzieli po białych znakach (spacje, tabulatory)
    wyniki_analizy["Liczba wyrazów (proste liczenie, ignoruje interpunkcję)"] = len(wyrazy)

    # 3. Liczenie zdań (bardzo proste i ułomne)
    # Po prostu liczymy, ile jest kropek, wykrzykników i znaków zapytania.
    # To jest bardzo niedokładne, ale to prosta implementacja!
    ilosc_zdan = tekst.count('.') + tekst.count('!') + tekst.count('?')
    wyniki_analizy["Liczba zdań (OSZACOWANIE - bardzo niedokładne)"] = ilosc_zdan

    # 4. Liczenie wystąpień liter i cyfr
    liczniki_znakow = {}
    liczba_malych_liter = 0
    liczba_wielkich_liter = 0
    liczba_samych_cyfr = 0

    # Decydujemy, którą wersję tekstu będziemy analizować (case sensitive/insensitive)
    tekst_do_liczenia = tekst
    if not CZY_CASE_SENSITIVE:
        # Jeśli nie chcemy rozróżniać wielkości liter, zamieniamy wszystko na małe
        tekst_do_liczenia = tekst.lower()
        print("INFO: Analiza w trybie Case INSENSITIVE (wszystko zamienione na małe litery).")
    else:
        print("INFO: Analiza w trybie Case SENSITIVE (rozróżnia małe i duże litery).")

    # Przechodzimy przez KAŻDY znak w tekście
    for znak in tekst_do_liczenia:

        # Sprawdzamy, czy to litera (A-Z lub a-z)
        if znak.isalpha():

            # W tym miejscu liczymy wystąpienia każdej litery (dla statystyki liter)
            if znak in liczniki_znakow:
                liczniki_znakow[znak] += 1
            else:
                liczniki_znakow[znak] = 1

        # Sprawdzamy, czy to cyfra (0-9)
        elif znak.isdigit():
            liczba_samych_cyfr += 1

            # W tym miejscu też liczymy wystąpienia każdej cyfry
            if znak in liczniki_znakow:
                liczniki_znakow[znak] += 1
            else:
                liczniki_znakow[znak] = 1

    # Liczymy małe/wielkie litery na podstawie oryginalnego tekstu (to jest bardziej dokładne)
    for oryginalny_znak in tekst:
        if oryginalny_znak.islower():
            liczba_malych_liter += 1
        elif oryginalny_znak.isupper():
            liczba_wielkich_liter += 1

    wyniki_analizy["Liczba znalezionych cyfr (0-9)"] = liczba_samych_cyfr
    wyniki_analizy["Liczba małych liter"] = liczba_malych_liter
    wyniki_analizy["Liczba wielkich liter"] = liczba_wielkich_liter

    # Dzielimy statystyki na dwie grupy
    statystyki_liter = {k: v for k, v in liczniki_znakow.items() if k.isalpha()}
    statystyki_cyfr = {k: v for k, v in liczniki_znakow.items() if k.isdigit()}

    # Dodajemy szczegółowe statystyki do wyników
    wyniki_analizy["Statystyki_liter"] = statystyki_liter
    wyniki_analizy["Statystyki_cyfr"] = statystyki_cyfr

    return wyniki_analizy


# --- KROK 3: Funkcja do zapisywania statystyk programu ---
def zapisz_statystyki_programu(statystyki_ogolne, wyniki_analizy):
    # 1. Aktualizujemy statystyki
    # Zawsze zwiększamy licznik uruchomień
    statystyki_ogolne["ilosc_uruchomien"] += 1

    # Dodajemy wyniki z tej analizy do sum
    statystyki_ogolne["sum_znakow"] += wyniki_analizy.get("Liczba wszystkich znaków (włączając spacje, itd)", 0)
    statystyki_ogolne["sum_wyrazow"] += wyniki_analizy.get("Liczba wyrazów (proste liczenie, ignoruje interpunkcję)", 0)
    statystyki_ogolne["sum_liczb"] += wyniki_analizy.get("Liczba znalezionych cyfr (0-9)", 0)

    # 2. Zapisujemy do pliku
    print(f"\nINFO: Zapisuję zaktualizowane statystyki programu do: {NAZWA_PLIKU_STATYSTYK_PROGRAMU}")
    try:
        with open(NAZWA_PLIKU_STATYSTYK_PROGRAMU, 'w', encoding='utf-8') as plik:
            # Wypisujemy główne liczniki w formacie, jaki był wymagany
            plik.write("Ilość uruchomień programu:\n")
            plik.write(f"{statystyki_ogolne['ilosc_uruchomien']}\n")

            plik.write("Przeanalizowanych znaków:\n")
            plik.write(f"{statystyki_ogolne['sum_znakow']}\n")

            plik.write("Znalezionych wyrazów:\n")
            plik.write(f"{statystyki_ogolne['sum_wyrazow']}\n")

            plik.write("Znalezionych liczb:\n")
            plik.write(f"{statystyki_ogolne['sum_liczb']}\n")

            # Wypisujemy też inne statystyki, które mogłyby być ciekawe
            # (Tutaj nie sumujemy małych/dużych liter, bo to by zależało od trybu case sensitive)

        print("INFO: Zapis zakończony pomyślnie!")
    except Exception as e:
        print(f"Ojej! Nie udało się zapisać statystyk programu do pliku: {e}")


# --- KROK 4: Główny blok programu (wywołanie wszystkiego) ---

# Wczytujemy stare statystyki programu
globalne_statystyki = wczytaj_statystyki_programu()

# Wywołujemy funkcję analizującą tekst
wynik_analizy = analizuj_tekst()

# Sprawdzamy, czy analiza się powiodła
if wynik_analizy is not None:

    # Wypisujemy wyniki na ekranie (konsoli)
    print("\n\n########################################")
    print("## WYNIKI ANALIZY TEKSTU Z PLIKU ##")
    print("########################################")

    # Wypisujemy proste statystyki
    print(f"**Tryb Case Sensitivity**: {'WŁĄCZONY' if CZY_CASE_SENSITIVE else 'WYŁĄCZONY'}")
    print("-" * 40)
    print(f"Znaków łącznie: {wynik_analizy['Liczba wszystkich znaków (włączając spacje, itd)']}")
    print(f"Wyrazów (oszacowanie): {wynik_analizy['Liczba wyrazów (proste liczenie, ignoruje interpunkcję)']}")
    print(f"Zdań (bardzo proste oszacowanie): {wynik_analizy['Liczba zdań (OSZACOWANIE - bardzo niedokładne)']}")
    print(f"Cyfr (0-9): {wynik_analizy['Liczba znalezionych cyfr (0-9)']}")
    print(f"Małych liter: {wynik_analizy['Liczba małych liter']}")
    print(f"Wielkich liter: {wynik_analizy['Liczba wielkich liter']}")

    # Wypisujemy statystyki liter
    print("\n*** Statystyki Wystąpień Liter ***")
    # Sortujemy litery, żeby było ładniej (od najczęściej do najrzadziej)
    posortowane_litery = sorted(wynik_analizy["Statystyki_liter"].items(), key=lambda item: item[1], reverse=True)
    for litera, ilosc in posortowane_litery:
        print(f"Litera '{litera}': {ilosc} razy")

    # Wypisujemy statystyki cyfr
    print("\n*** Statystyki Wystąpień Cyfr ***")
    for cyfra, ilosc in wynik_analizy["Statystyki_cyfr"].items():
        print(f"Cyfra '{cyfra}': {ilosc} razy")

    print("-" * 40)

    # Zapisujemy statystyki programu
    zapisz_statystyki_programu(globalne_statystyki, wynik_analizy)

else:
    print("Program zakończył działanie z powodu błędu w analizie tekstu.")