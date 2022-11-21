numbers = [1]

print(numbers)

for i in range(5):
    
    new_numbers = [1]
    
    position = 0
    while position < len(numbers) -1:
        new_numbers.append(numbers[position] + numbers[position+1])
        position+=1
    new_numbers.append(1)
    
    numbers = new_numbers.copy()
    
    print(numbers)