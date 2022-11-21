colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

all_cards = []

for znak in colors:
    for karta in figures:
        a_card = karta.copy()
        a_card['Color'] = znak
        all_cards.append(a_card)

        
import random

random.shuffle(all_cards)

player_1 = []
player_2 = []
max = len(all_cards)

for i in range(max):
    if i % 2 == 0:
        player_1.append(all_cards[i])
    else:
        player_2.append(all_cards[i])

while len(player_1) != 0 and len(player_2) != 0:
    card_1 = player_1.pop(0)
    card_2 = player_2.pop(0)
    stock = []
    print('Karta gracza pierwszego:', card_1['Figure'], '\tKarta gracza drugiego:', card_2['Figure'])
    if card_1['Power'] == card_2['Power']:
        while card_1['Power'] == card_2['Power']:
            print('Wojna!')
            stock.append(card_1)
            stock.append(card_2)
            if len(player_1) < 2:
                player_2.extend(stock)
                player_2.extend(player_1)
                player_1.clear()
                break
            elif len(player_2) < 2:
                player_1.extend(stock)
                player_1.extend(player_2)
                player_2.clear()
                break
            else:
                card_1 = player_1.pop(0)
                card_2 = player_2.pop(0)
                stock.append(card_1)
                stock.append(card_2)
                card_1 = player_1.pop(0)
                card_2 = player_2.pop(0)
            print('Karta gracza pierwszego:', card_1['Figure'], '\tKarta gracza drugiego:', card_2['Figure'])
        else: 
            if card_1['Power'] > card_2['Power']:
                print('Wojne wygrał gracz 1! Wszystkie karty są wkładane do jego decku')
                stock.append(card_1)
                stock.append(card_2)
                player_1.extend(stock)
            else:
                print('Wojne wygrał gracz 2! Wszystkie karty są wkładane do jego decku')
                stock.append(card_1)
                stock.append(card_2)
                player_2.extend(stock)
    elif card_1['Power'] > card_2['Power']:
        print('Wygrał Gracz pierwszy, obie karty sa dodawane do jego decku')
        player_1.append(card_1)
        player_1.append(card_2)
        random.shuffle(player_1) #this line prevents infinite loops
    elif card_1['Power'] < card_2['Power']:
        print('Wygrał Gracz drugi, obie karty sa dodawane do jego decku')
        player_2.append(card_1)
        player_2.append(card_2)
        random.shuffle(player_2) #this line prevents infinite loops
    print('Gracz 1 posiada', len(player_1), 'kart', '\nGracz 2 posiada', len(player_2), 'kart')
    
if len(player_1) > 0:
    print('Wygrał gracz 1!')
else:
    print('Wygrał gracz 2!')
    
    
# BEWARE! Depending on the random card shuffle there is a possibility
# of infinite loop appearing! Still learning how to deal with that occurence

# update - dealt with infinite loops, playerdeck now shuffles after winning
# a battle that didnt result in war