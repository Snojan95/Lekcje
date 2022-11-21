# for number in range(1, 21, 2):
#     print(number)
    
# metoda range przywoluje zestaw liczb, zaczynajacych sie od pierwszej wartosci
# konczaca sie na drugiej wartosci, a trzecia wartosc okresla jakie maja
# byc przeskoki pomiedzy wartoscia pierwsza i druga
# PAMIETAJ : python nie liczy wartosci stop, dlatego przybranie wartosci 21
# daje nam zakres liczb od 1 do 20, a nie 21. Wartosc 21 to dla pythona wartosc STOP

for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))
        
#  Gwoli przypomnienia lekcji z formatowania: %2 - procent jest znakiem dzielenia
# %2d sciaga nam liczbe z generowanego range'a przez metode range wyzej i rezerwuje
# dla niej dwa miejsca w metodzie print. %s sciaga stringa ustawionego dalej w
# metodzie print % (number, 'odd') - to jest użytym tutaj stringiem