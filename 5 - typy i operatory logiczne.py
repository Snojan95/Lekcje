# is_weekend = True
# print("Is weekend =", is_weekend)
# temp = 22
# print('temperature =', temp)
# to_do = ''
# print('to do list =', to_do)
# is_weekend = True
# print("Is weekend =", is_weekend)
# temp = 25
# print('temperature =', temp)
# to_do = ''
# print('to do list =', to_do)
# is_happy = (is_weekend and temp >= 20 and to_do == '')\
#     or (not is_weekend and not temp >= 20 and to_do != '')
# print("is happy =", is_happy)
is_automatic_mode = False
# tryb automatyczny wlaczony
is_80_percent_light = False
# poziom swiatla powyzej 80%
is_direct_light = False
# swiatlo swieci prosto w oczy kierowcy
is_rainy = True
# pada deszcz, jest mgla lub inne niekorzystne warunki pogodowe
turn_lights_on = is_automatic_mode and (not is_80_percent_light or is_direct_light or is_rainy)
print("Automatic mode:   ", is_automatic_mode)
print("Is the light good:", is_80_percent_light)
print("Is sun low:       ", is_direct_light)
print("Is it rainy:      ", is_rainy)
print("TURN LIGHTS ON:   ", turn_lights_on)

# Operatory logiczne takie jak and, or, is, is not, pozwalaja nam sprawdzac
# czy pewne warunki sa lub nie sa spelnione i na bazie tego wykonywac
# lub nie wykonywac pewnych funkcji

# a jesli chodzi o znaczki to == jest równe, > < - wieksze mniejsze
# >= <= wieksze/mniejsze i rowne / = znaczy ze cos jest, != znaczy ze nie jest