import random

print('One random number:', random.randint(1, 100))

# randint - daje nam random integer (calkowita) od pierwszej wartosci do drugiej
# tutaj 1-100

print('Random number from a range:', random.choice(range(1,100)))

# to robi to samo, ale inaczej

print('Easier random range:', random.randrange(1,100))

# to z grubsza to samo, ale jeszcze inaczej z pomoca modulu random

list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print('Reordered list:', list)

# shuffle miesza dany element, tutaj liste

print(random.random())

# funkcja random po prostu generuje wartosc float od 0 do 1

