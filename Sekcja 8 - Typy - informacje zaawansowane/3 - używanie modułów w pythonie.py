import math
# taka komenda załaduje caly modul math, trzeba by bylo potem korzystac z polecen zaladowanych
# poprzedzajac je nazwa modulu aby zadzialaly, jak tutaj nizej

print(math.pi)

print(math.floor(math.pi))

# jest jeszcze inna metoda, ta tutaj nizej

from math import *

# takie cos zaladuje modul math, i mozemy wtedy uzywac polecen bez potrzeby
# wpisywania nazwy modulu, jak tutaj nizej

print(pi)

print(floor(pi))

# niby wygodniejsze, ale jesli zaladujesz wiecej niz jeden modul
# a nazwy zimportowanych funkcji beda sie pokrywac, to masz problem
# wiec jesli pracujesz z wiecej niz jednym modulem to lepiej generalnie uzywac
# tej pierwszej metody wyzej