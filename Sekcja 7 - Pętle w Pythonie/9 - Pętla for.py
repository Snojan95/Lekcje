persons = ['Elizabeth', 'Steven', 'Sebastian', 'Margaret', 'Svetlana', 'Raphael']

domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('--to wszystkie adresy mailowe--')
    
# metoda for automatycznie przetwarza kazdy element z collectible ktora jest
# jej dostarczona. To potezne i autystyczne narzedzie, spojrz co zrobi gdy
# zamiast listy, nakarmie metode for np. stringiem 'elizabeth'

for x in 'Elizabeth':
    print(x)
    
# jak widac, przetworzyl kazda wartosc w stringu, czyli kazda litere z
# imienia elizabeth!