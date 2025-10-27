#zadanie 1
# 1. Napisz program do przeliczania stopni Celsjusza
# na Fahrenheita i odwrotnie (niech program zapyta o kierunek konwersji)

print('-' * 20, "Kalkulator temperatury",'-' * 20 )

ask_user = True
while ask_user is True:
    user_input_FC = input("Jesli chcesz przeliczyc stopnie F na C wcisnij F, w odwrotnym przypadku wcisnij C: ").upper()
    if user_input_FC == 'F':
        F_degree = input("Podaj stopnie Fahrenheita: ")
        if F_degree.isdigit():
            F_degree = int(F_degree)
            przeliczenie_na_Celcujusza = round(((F_degree - 32) * 5/9),2)
            print(przeliczenie_na_Celcujusza)
            break
        else:
            print('Niepoprawna liczba stopni. Podaj poprawne dane.')
    elif user_input_FC == 'C':
        C_degree = input("Podaj stopnie Celcjusza: ")
        if C_degree.isdigit():
            C_degree = int(C_degree)
            przeliczenie_na_Fahrenheita = round(((C_degree * 9/5) + 32),2)
            print(przeliczenie_na_Fahrenheita)
            break
        else:
            print('Wpisz poprawnie liczbe:  ')
    else:
        print('Niepoprawny wybor. Jesli chcesz przeliczyc stopnie F na C wcisnij F, w odwrotnym przypadku wcisnij C:  ')



