age = 19

if age >= 18:
    print('Jestes dorosly i mozesz kupic alkohol')
    # jesli chcesz zeby if zostalo wyczytane, a instrukcja wykonana komenda
    # print musi byc wcieta pod metoda if, wtedy python traktuje to jako cos
    # co ma sprawdzic i wykonac jesli if sie zgadza
else:
    print('Jestes za mlody zeby kupic alkohol')
    # if - else jest tutaj w parze, jesli to co sprawdzamy komenda IF jest prawdziwe
    # wykona on instrukcje podpieta pod soba, w przeciwnym wypadku wykona instrukcje
    # podpieta pod else
is_drunk = True
# już to robiles, dokladamy po prostu kolejne warunki
if age >= 18 and not is_drunk:
    print('Jestes dorosly i mozesz kupic alkohol')
else:
    print('nie mozesz kupic alkoholu')

is_restricted_area = False
# and anotha one
if age >= 18 and not is_drunk and not is_restricted_area:
    print('Alkohol jest twój King')
else:
    print('nie dla ciebie alko krindżlordzie')
