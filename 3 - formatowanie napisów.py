# message1 = 'Processing file %s'

# znak %s, %d powoduje że python oczekuje ze wstawimy cos w ta wartosc
# s jak string, albo d jak decimal dla cyfr

# print(message1 % ('file_1.txt'))
# message2 = 'File %s has size %d KB'
# print(message2 % ('file_1.txt', 100))
# message3 = 'File %20s has size %10d KB'

# dodanie cyfry po procencie, jak tutaj %20s, powoduje ze python zarezerwuje
# jakas ilosc miejsc dla danego stringa albo decimala, niezaleznie od tego
# czy dany string lub decimal jest faktycznie tak długi

# print(message3 % ('file_1.txt', 100))
# message4 = 'Processing file {0:s}'

# w przypadku nawiasów klamrowych sytuacja jest podobna co z %, z tą różnicą
# że oznaczenie {0:s} mówi że string ma byc na pierwszej pozycji, niezależnie
# od tego jak wyglada to przed printem, a % bierze wartosci jedna po drugiej

# print(message4.format ('file_1.txt'))
# message5 = 'File {0:s} has size {1:d}'
# print(message5.format('file_1.txt', 100))
# message6 = 'File {1:20s} has size {0:10d}'
# print(message6.format(100, 'file_1.txt'))
# hello_message = 'Hello %s!'
# print(hello_message % ('Chris'))
# hello_message = 'Hello %s!'
# print(hello_message % ('Chris'))
# hello_message = 'Hello {0:s}!'
# print(hello_message.format('Kate'))
# hello_message = 'Hello {0:s}!'
# print(hello_message.format('Chris'))
# hello_message = '%s has %d %s'
# print(hello_message % ('Kate', 1, 'animal'))
# hello_message = '%s has %d %s'
# print(hello_message % ('Chris', 10000, '$'))
# hello_message = "{0:s} has {1:d} {2:s}"
# print(hello_message.format('Epon', 20, '$'))
# hello_message = "{0:s} has {1:d} {2:s}"
# print(hello_message.format('Kate', 1, 'animal'))
pleasure = 'fisting'
price = 300
currency = 'bucks'
dungeon_visit = '%s is %d %s'
print(dungeon_visit % (pleasure, price, currency))
dungeon_visit_2 = '{2:s} is {1:d} {0:s}'
print(dungeon_visit_2.format(pleasure, price, currency))
line = '{0:20s} costs {1:6d} €'
print(line.format('Fisting', 300))
print(line.format('S&F action', 1500))
print(line.format('Slave revolt', 9999))