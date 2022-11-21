line = 'this IS a very STRANGE text'
# print(line.capitalize())

# capitalize zamienia wartosc stringu na napisana jak zdanie, zaczynajaca sie z duzej
# i reszta malych

# print(line.title())

# title powoduje ze kazde slowo zaczyna sie od wielkiej litery

# upper()
# lower()

# te dwie metody są juz ci znane, same duze, same male

# print(line.swapcase())

# swapcase zamienia male na duze, a duze na male

# line_ger = 'der Fluß'

# print(line_ger.casefold())

# casefold jest agresywniejsza wersja lower, zamienia nam nietypowe znaki na
# prostsze, tak jak tutaj w niemieckim tekst zostal zamieniony na 'der fluss'
# casefold zrozumial ze niemiecki szarfss moze zostac zapisany jako ss

# print(line.count('e'))

# to juz znasz, liczy ile razy 'e' pojawia sie w stringu

# print(line.find('e'), line.rfind('e'))

#  find tez juz znasz, znajduje pierwsze 'e' w tekscie, a z kolei
# rfind znajduje pierwsze 'e' w tekscie zaczynajac od prawej strony

# print(line.index('e'))
# print(line.rindex('e'))

# index to blizniacza funkcja find, dziala tutaj tak samo jak find

# print(line.find('p'))
# print(line.index('p'))

# jednak jest roznica, bo gdy szukamy za pomoca metody find litery której
# nie ma w tekscie, dostajemy wartosc zwrotna -1 (czyli false)
# a szukajac za pomoca indexu dostajemy w zwrocie błąd ValueError: substring not found

# print('e' in line)
# print('p' in line)

# mozemy tez wykorzystac operator logiczny 'in', w sposob podobny do find
# bedzie nam zwracal wartosc true lub false

# print(line.startswith('this'))
# print(line.startswith('THIS'))

# jak nazwa wskazuje, to jest dosyc logiczne, ale zwroc uwage ze startswith
# jest metoda case-sensitive i w pierwszym sprawdzeniu dalo nam wartosc true
# a w drugim dalo nam wartosc false, bo tekst zaczyna sie z malych liter

# text = '''ten dlugi tekst
# jest zawarty w wielu linijkach
# to tak zwany string blokowy'''

# print(text)
# print(text.count('\n'))

# zwroc tu uwage na to ze entery zaczynajace nowe linijki sa zakodowane w stringu
# blokowym, nawet jesli ich nie widac

# import string

# print(string.ascii_letters)
# print(string.digits)

# string to sam w sobie kolejny moduł!

line_2 = 'this is the end of this lesson'

list = line_2.split(' ')

# otrzymalismy teraz liste z poszczegolnymi slowami ze stringa line_2
# zeby teraz polaczyc znowu taka liste w stringa nie mozemy po prostu wpisac np
# list.join(' '), bo da nam to blad. Metoda join() nie dziala dla list, tylko stringów

print(' '.join(list))

# z taka komenda dostajemy spowrotem string 'this is the end of this lesson' !























