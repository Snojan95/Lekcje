# 1. Zadeklaruj zmienne opisujące figury kart i kolory:

# colors = ['Hearts','Diamonds','Clubs','Spades']

# figures = ['Ace','King','Queen','Jack','10','9']

# 2. Zadeklaruj zmienną allCards jako pustą listę

# 3. Napisz zagnieżdżoną pętlę, która przechodzi przez colors i figures i dodaje do allCards napis będący połączniem nazwy koloru i figury

# 4. Wyświetl allCards - zauważ, że porządek kart jest wg kolorów i figur

# 5. Zaimportuj moduł random

# 6. Wymieszaj karty znajdujące się w zmiennej allCards. Wyświetl potasowane karty

# 7. Pora rozdać karty graczom. Zrobimy to na 2 sposoby. Ale najpierw zadeklaruj puste listy player1 i player2

# 8. Sposób pierwszy:

# Do zmiennej max przypisz wartość określającą długość listy allCards

# Napisz pętlę sterowaną przez zmienną i zmieniającą się od zera do max-1, a w tej pętli:

# jeżeli i jest parzyste - dodaj element allCards[i] do listy player1

# jeżeli i jest nieparzyste - dodaj element allCards[i] do listy player2

# Wyświetl karty gracza 1 i 2

# 9. Sposób drugi - poprzednie rozwiązanie nawiązuje do tego w jaki sposób rozdajemy
#  karty do gry. Ale skoro karty i tak są wymieszane to w przypadku 24 kart można by
#  pierwszych 12 dać pierwszemu graczowi, a pozostałe 12 drugiemu. Dlatego: nie korzystając z pętli:

# przepisz do player1 elementy z allCards od 0 do 11

# przepisz do player2 elementy z allCards od 12 do 23

# wyświetl karty obu graczy

colors = ['Kier', 'Karo', 'Trefl', 'Pik']

figury = ['As', 'Król', 'Królowa', 'Walet', '10', '9']

all_cards = []

for znak in colors:
    for karta in figury:
        all_cards.append(znak +' '+ karta)
        
import random

random.shuffle(all_cards)

player_1 = []
player_2 = []

max = len(all_cards)

for i in range(max):
    if max % 2 == 0:
        player_1.append(all_cards[i])
    else:
        player_2.append(all_cards[i])
    max-=1
    
# albo bardziej buraczano 
    
for x in range(max):
    if max > 12:
        player_1.append(all_cards[x])
    else:
        player_2.append(all_cards[x])
    max-=1
        
# albo jeszcze bardziej buraczanie

player_3 = all_cards[:12]
player_4 = all_cards[12:]


















