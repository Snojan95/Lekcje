import random

# counter = 0

# # while counter < 10:
# #     print(random.randint(1, 100))
# #     counter+=1

# number_1 = random.randint(1, 100)

# number_2 = random.randint(1, 100)

# while number_1 != number_2:
#     number_2 = random.randint(1, 100)
#     counter+=1
# else:
#     print('liczba', number_1, 'jest równa', number_2)
#     print('trafienie wymagało', counter, 'prób')
    
# to było zadanie 1, 2 i 3

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)

group_number = 0

for group in range(len(countries)):
    if group % 4 == 0:
        group_number+=1
        print('========= Group %d ========' % (group_number))
    print(countries[group])















