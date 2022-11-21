import random

my_numbers = []

# while len(my_numbers) < 7:
    # new_number = random.randint(1, 49) # pamietaj ze randint czyta wartosci skrajne, w tym wypadku do 49 wlacznie z 49!
    # my_numbers.append(new_number)
# print('To moje liczby do totka:', my_numbers)

# ten kod powoduje ze moga sie trafic powtorki, np 2 i 2, tutaj nizej
# widac jak tego uniknac

while len(my_numbers) < 7:
    new_number = random.randint(1, 49)
    if new_number in my_numbers:
        print('Eliminated:', new_number)
        continue
    else:
        my_numbers.append(new_number)
print('To moje liczby do totka:', my_numbers)