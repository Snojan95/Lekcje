imperatorzy = {'PL' : 'Duda','US' : 'Trump'}

# w ten sposób tworzymy dictionary, uzywajac nawiasow klamrowych

# print(imperatorzy["US"])
# print(imperatorzy)

# print z obiektem US daje nam wartosc zwrotna trump, a print bez wybierania
# obiektu daje nam cale dictionary

imperatorzy['DE'] = 'Merkel'
# print(imperatorzy['DE'])

# tak dodaje się nowe wartosci do istniejacego slownika, z nazwiasem kwadratowym

# print(imperatorzy.keys())

# ta komenda wyswietla nam zawarte w slowniku klucze do wartosci (PL, US, DE)

# print(imperatorzy.values())

# ta komenda wyswietla wartosci wywolywane kluczami ze slownika (Duda, Trump, Merkel)

# print(imperatorzy.items())

# ta komenda wyswietla przedmioty - wartosci razem z kluczami z którymi są związane

# print(imperatorzy.popitem())

# ta komenda jest podobna do tej uzywanej przy listach, wywołuje wartosc ze slownika
# a nastepnie ja z niego usuwa

imperatorzy.setdefault('FR', 'Macron')

# metoda setdefault podobnie do komendy imperatorzy['DE'] = 'Merkel' dodaje
# wartosc do slownika

# print(imperatorzy.get('FR'))

# metoda get() pobiera klucz ze słownika i wyswietla przypisana do niego wartosc

nowi_imperatorzy = {'RU':'Putin', 'DE':'Schulz'}
print(nowi_imperatorzy)

imperatorzy.update(nowi_imperatorzy)
print(imperatorzy)

# z pomoca metody update() aktualizujemy jeden slownik o zawartosc innego
# w tym wypadku zaktualizowalem slownik imperatorzy za pomoca slownika 
# nowi imperatorzy, dodało to rosje i putina, bo nie bylo ich tam wczesniej,
# a wartosc klucza DE zostala zaktualizowana z Merkel do nowej wartosci Schulz



