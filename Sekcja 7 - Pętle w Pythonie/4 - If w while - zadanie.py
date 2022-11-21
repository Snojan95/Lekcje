numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

# i = 0
# max = len(numbers)-1

# while i < max:
#     print(numbers[i], numbers[i+1])
#     if numbers[i]**2 == numbers[i+1]:
#         print('Kod znaleziony')
#     i+=1

# to było zadanie 1

# max = len(numbers)-2

# while i < max:
#     print(numbers[i], numbers[i+1], numbers[i+2])
#     if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
#         print('Kod znaleziony')
#     i+=1

# to było zadanie 2

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0 
max = len(texts)-1

while i<max:
    print(len(texts[i]), len(texts[i+1]))
    if len(texts[i]) == len(texts[i+1]):
        print('tyle samo liter')
    i+=1
    
# zadanie 3