import random

min = 1
max = 6

dice = random.randint(min, max)


# print(dice)

# one = '''
#   1
   
#   o 
   
#   '''
# two = '''
# 2
#   o
   
# o  
#   '''
# three ='''
# 3
#   o
#   o 
# o  
#   '''
# four = '''
# 4
# o o
   
# o o
#   '''
# five ='''
# 5
# o o
#   o 
# o o
#   '''
# six ='''
# 6
# o o
# o o
# o o
# '''


# x = 0
# while x < 10:
#     if dice == 1:
#         print(one)
#     elif dice == 2:
#         print(two)
#     elif dice == 3:
#         print(three)
#     elif dice == 4:
#         print(four)
#     elif dice == 5:
#         print(five)
#     elif dice == 6:
#         print(six)
#     dice = random.randint(min, max)
#     x+=1
    
# if dice == 1:
#     print(one)
# elif dice == 2:
#     print(two)
# elif dice == 3:
#     print(three)
# elif dice == 4:
#     print(four)
# elif dice == 5:
#     print(five)
# elif dice == 6:
#     print(six)
    
dices = []
throw = 0

while throw < 5:
    dices.append(random.randint(min, max))
    throw+=1
dices.sort()
print(dices)






























    