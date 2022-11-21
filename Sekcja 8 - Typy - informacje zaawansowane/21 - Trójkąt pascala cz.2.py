width = 60
height = 7
numbers = [1]

line = ''
for n in numbers:
    line+='%3d' % (n)
print(line.center(width))

for i in range(height-1):
    
    new_numbers = [1]
    
    position = 0
    while position < len(numbers) -1:
        new_numbers.append(numbers[position] + numbers[position+1])
        position+=1
    new_numbers.append(1)
    
    numbers = new_numbers.copy()
    
    line = ''
    for n in numbers:
        line+='%3d' % (n)

    print(line.center(width))
