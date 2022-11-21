min_likes = 500
min_shares = 99

if min_likes >= 500 and min_shares >= 100:
    print('odziez jest na przecenie')
else:
    print('normalna cena')
    
is_pizza_ordered = True
is_big_drink_ordered = True
is_weekend = True

if is_pizza_ordered and is_big_drink_ordered and not is_weekend:
    print('masz borgiera szefie')
else:
    print('kup wincyj zeby miec borgiera')
    
    
disk_size = 140
disk_size_used = 120
file_size = 10

if disk_size - disk_size_used >= file_size:
    print('mozna pobrac plik')
else:
    print('brak miejsca na dysku')