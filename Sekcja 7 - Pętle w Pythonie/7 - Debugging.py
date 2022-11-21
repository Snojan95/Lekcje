cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
#  to jest waga paczek w kilogramach, sort i reverse segreguje je po wadze
# od najwiekszej do najmniejszej, pozwalajac zapakowac rzeczy nieco wydajniej
print('The cargo list is:', cargo)
box_capacity = 90
box = []

# to jest maksymalna pojemnosc pudla i reprezentacja samego pudla

i = 0

# while sum(box) + cargo[i] < box_capacity and i<len(cargo):
#  i<len(cargo) zabezpiecza nas przed nieskonczonym loopem, gdyby pudlo bylo
# w stanie pomiescic wszystkie elementy listy cargo
# ta linia jest zakomentowana, bo nie jest to najlepsze rozwiazanie

while i<len(cargo) and (box_capacity - sum(box)) >= min(cargo):
    if (box_capacity - sum(box)) >= cargo[i]:
# z taka linia kodu python sprawdza kolejne wartosci i doklada je do pudelka
# tylko jesli faktycznie jest miejsce na taki obiekt w pudle
        box.append(cargo[i])
    i+=1


print('laczna waga przedmiotow w paczce to:', sum(box))
print('elementy znajdujace sie w paczce to:', box)


# ta lekcja byla na temat debuggera, troche ciezko mi to pokazac tutaj
# to bedzie pewnie najbardziej zagmatwane w nauce, trzymam za nas kciuki