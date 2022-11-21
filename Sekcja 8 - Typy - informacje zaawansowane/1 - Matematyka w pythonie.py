f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print('\n')

print(int(f_smaller), int(f_bigger))
print('\n')

# metoda int to rzutowanie, ucina po prostu koncowke liczby po kropce, zostawiajac
# wartosc decimal zamiast wartosci float

print(abs(f_smaller), abs(-f_smaller))
print('\n')

# metoda abs to wartosc absolutna, zwraca wartosc absolutna, wiec pomimo wziecia
# wartosci negatywnej do f_smaller, dalo wynik na plusie, bo to absolutna wartosc

print(round(f_smaller, 2), round(f_bigger, 2), round(f_bigger,3))
print('\n')

# round to metoda zaokraglajaca, jej drugi argument dedykuje do jakiego
# miejsca po przecinku metoda ma zaokraglic

print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))
print('\n')

# min i max wyciagaja minimalna lub maksymalna wartosc z podanych argumentow

list = [1,2,3,4,5,4,4,5,4]

print(sum(list), len(list))
print('\n')

print(sum(list)/len(list))

# sum dodaje wartosci argumentu, tutaj listy liczb, len wyznacza dlugosc tej listy (length)
# tutaj obliczylismy srednia z listy

print(round(2.675, 2))

# zaokraglenie do dwoch miejsc po przecinku takiej wartosci daje 2.67
# python traktuje 2.675 == 2.6749999999, wiec zaokragla w dol