# number = 1
# previous_number = 0

# while number < 50:
#     print(number + previous_number)
#     previous_number = number
#     number+=1
    
import random
my_number = random.randint(0, 20)
guess = -1
trials = 0
print('Zgadnij liczbe')
while guess != my_number:
    guess = int(input())
    if my_number == guess:
        print('Gratulacje, moja liczba bylo', my_number, 'i udalo ci sie zgadnac po', \
              trials, 'probach')
    elif my_number > guess:
        print('Za mało')
    else:
        print('Za dużo')
    trials+=1
    # if guess == my_number:
    #     print('Zgadles po', trials, 'probach')