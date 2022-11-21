f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math

print(math.ceil(f_smaller), math.ceil(f_bigger))

# funkcja ceil - wyciaga najmniejsza liczbe calkowita wieksza od wartosci
# tu i tu bedzie to 4

print(math.floor(f_smaller), math.floor(f_bigger))

# floor to odwrotnosc ceil, zwraca nam najwieksza liczbe calkowita mniejsza
# od wartosci, tu i tu bedzie to 3

print(math.pow(2, 8))

# power to potęgowanie, pierwsza wartosc to liczba, a druga to liczba do potęgi
# której potęgujemy

print(math.sqrt(16))

# to jest pierwiastkowanie, ale tylko pierwiastkowanie do 2, nie wiecej

print(math.pi, math.e)

# w module math jest sporo zmiennych, takich jak 'pi' i 'e'

print(math.sin(math.pi/2), math.cos(math.pi/4))

# sa tez sinusy i cosinusy, mam nadzieje ze nie bedzie to bardzo potrzebne