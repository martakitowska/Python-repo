'''Program rysujący piramidę o określonej wysokości, np dla 3
        #
      ###
    #####'''

wysokosc_piramidy = input('Podaj wysokosc piramidy: ')
user_input = True

wysokosc_piramidy = int(wysokosc_piramidy)
for i in range (1, wysokosc_piramidy + 1):
    znaki = 2 * i - 1
    puste_pola = wysokosc_piramidy - i
    print (' ' * puste_pola + '#' * znaki)

"""while user_input is True:
    wysokosc_piramidy = int(wysokosc_piramidy)
    x = 1
    while x < wysokosc_piramidy:
        puste_pola = int(((wysokosc_piramidy - x) / 2))
        print(' '* (puste_pola),'#' * x,' '* (puste_pola))
        puste_pola -= -1
        x+=1
    break"""

