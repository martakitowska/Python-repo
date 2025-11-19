#Napisz program do sprawdzania czy podany rok jest rokiem przestępnym..


#from box_drawing import ask_user
def rok_przestepny():
    ask_user = True
    while ask_user is True:
        rok = input('Podaj rok do sprawdzenia: ')
        if rok.isdigit():
            rok = int(rok)
            if rok % 4 == 0 and rok % 100 == 0 and rok % 400 == 0 and rok > 0:
                print(f'Rok {rok} jest rokiem przestepnym')
                break
            else:
                print(f'Rok {rok} NIE jest rokiem przestepnym')
                break
        else:
            print('Podaj poprawnie rok do sprawdzenia')


