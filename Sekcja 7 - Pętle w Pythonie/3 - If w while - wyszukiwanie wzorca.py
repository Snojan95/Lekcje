values = [10,43,12,48,12,11,18,90,57,28,19,27,49,19,74]

i = 0
max = len(values)-2

# len, czyli length, po prostu zwraca nam maksymalna ilosc wartosci zawartch
# w liscie values, odejmujemy tutaj od maxa 2, bo chcemy analizowac wartosci po
# 3 na raz, wiec musze wyznaczyc -2, aby lapalo mi same trojki. Bez tego
# program probowalby znalezc kolejne wartosci po 15, a mamy tylko 15 wartosci
# patrz na komende print nizej

while i<max:
    print(i, values[i], values[i+1], values[i+2])
    
    if values[i] < values[i+1] and values[i+1] < values[i+2]:
        print('\tBingo', values[i], values[i+1], values[i+2])
    else:
            print('pudło')
    
    i+=1