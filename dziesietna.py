def dziesietna():

    print("Program do konwersji systemów liczbowych")
    print("1. Z dziesiętnego na binarny")
    print("2. Z binarnego na dziesiętny")

    wybor = input("Wybierz kierunek konwersji (1 lub 2): ")

    if wybor == "1":
        decimal = int(input("Podaj liczbę do konwersji: "))
        binary = bin(decimal)[2:]
        print(f"{decimal} w systemie dwójkowym to {binary}")
    elif wybor == "2":
        binary = input("Podaj liczbę do konwersji: ")
        decimal = int(binary, 2)
        print(f"{binary} w systemie dziesiątkowym to {decimal}")
    else:
        print("Niepoprawny wybór!")

