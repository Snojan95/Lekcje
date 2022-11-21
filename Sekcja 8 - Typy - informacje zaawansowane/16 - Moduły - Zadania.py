# Masz następujące dane wejściowe:

# inputdata = [0,1,2,3,5,8,13,21,34,55,89]
# factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
# ZADANIE 1

# Załaduj moduł math

# Wyświetl informację o ilości elementów w obu listach

# Napisz instrukcję if, która:

# -jeśli liczba elementów na obu listach jest taka sama, 
# to rozpocznie przetwarzanie danych, które opiszemy dalej (na razie wystarczy np wyświetlić napis "ok")

# -jeśli liczba elementów nie jest zgodna wyświetli informację "inputdata and factortable need to have equal number of elements"

# Ciąg dalszy skryptu piszesz w pierwszej części polecenia if

# Napisz pętlę, która przechodzi przez wszystkie elementy listy input  data

# Ciąg dalszy piszesz w tej pętli

# wylicz wartość minvalue, która ma wynosić:
# <wartość n-tego elementu z inputdata> - <wartość n-tego elementu z factortable> * <wartość n-tego elementu z inputdata>
# oraz wartość maxvalue, która ma wynosić:
# <wartość n-tego elementu z inputdata> + <wartość n-tego elementu z factortable> * <wartość n-tego elementu z inputdata>

# Wyświetl wyliczone wartości

# Wyznacz liczby
# mininteger, która ma być największą liczbą całkowitą mniejszą od minvalue (funkcja floor)
# oraz
# maxinteger, która ma być najmniejszą liczbą całkowitą większą of maxVALUE (funkcja ceil)

# Wyświetl liczby: mininteger, n-ty element listy inputdata i maxinteger


# ZADANIE 2

# Załaduj moduł random

# Napisz pętlę, która tak jak poprzednio wyznaczy wartości minvalue oraz maxvalue, 
# ale tym razem nie chcemy korzystać z danych znajdujących się w factortable. Zamiast tych wartości wygeneruj liczby losowe z zakresu <0,1>

# Wskazówka - możesz rozpocząć od poprzedniego skryptu, tylko usuń instrukcję if i zamień odwołania do factortable[i] funkcją random.random()



# ZADANIE 3

# Z modułu datetime załaduj typ datetime.

# Wyświetl datę dzisiejszą

# Wyświetl datę dzisiejszą tak, aby pokazał się tylko rok-miesiac-dzień

# Zadanie 1
# import math

# inputdata = [0,1,2,3,5,8,13,21,34,55,89]
# factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

# print('inputdata is:', len(inputdata) ,'long.\n', 'factortable is:', len(factortable), 'long.')

# if len(inputdata) == len(factortable):
#     x = 0
#     while x < len(inputdata):
#         min_value = inputdata[x] - factortable[x] * inputdata[x]
#         max_value = inputdata[x] + factortable[x] * inputdata[x]
#         # print('max_value =', max_value, '\t', 'min_value =', min_value)
#         min_integer = math.floor(min_value)
#         max_integer = math.ceil(max_value)
#         # print('min_integer =', min_integer, '\t', 'max_integer =', max_integer)
#         print('min_integer =', min_integer, '\tinput =', inputdata[x], '\tmax_integer = ', max_integer)
#         x+=1
#     # print('OK')
# else:
#     print("inputdata and factortable need to have equal number of elements")

# Zadanie 2

# import random

# inputdata = [0,1,2,3,5,8,13,21,34,55,89]

# x = 0

# while x < len(inputdata):
#     min_value = inputdata[x] - random.random() * inputdata[x]
#     max_value = inputdata[x] + random.random() * inputdata[x]
#     print('min_value =', min_value, '\tmax_value =', max_value)
#     x+=1

# Zadanie 3
import datetime

print(datetime.datetime.now())

print(datetime.datetime.now().strftime('%Y, %m, %d'))





