tax = (4, 7, 8, 23)

# tuple robi sie nawiasami zyklymi

# print(tax[0])
# print(tax[-1])

# z listy tuple mozemy tak wyciagnac pewne wartosci, zwroc uwage ze notacja ujemna
# czyli taka zeby uzyskac wartosc z drugiego konca listy, zaczyna sie od -1, a nie 0

# print(tax.index(7))
# index jest metoda sprawdzania na jakiej pozycji w liscie albo tuplu znajduje sie element z nawiasu
# print(tax.count(8))
# tutaj liczymy ile razy wartosc z nawiasu pojawia sie w liscie lub w tuplu
# print(max(tax))
# tax_list = list(tax)
# to co wyżej jest konwersją tupla do listy
# print(tax_list)
# tax_list.append(30)
# append to komenda dodajaca elementy na koniec listy (ale nie tupla!)
# print(tax_list)
# new_tax = tuple(tax_list)
# to co wyżej jest konwersją listy do tupla
# print(new_tax)
# (tax1, tax2, tax3, tax4) = tax
# tutaj przypisujemy poszczególnym wartosciom 1,2,3,4 wartosci zawarte w tuplu tax
# print(tax1, tax3)
a = 1
b = 10
print('a =', a, '\tb =', b)
# temp = a
# a = b
# b = temp
# to co jest wyżej to bardziej zagmatwana alternatywa do tupla niżej
(a,b) = (b,a)
print('a =', a, '\tb =', b)