# *** to zadanie jest nieco trudniejsze - jeśli nie podejmujesz się samodzielnego rozwiązania, spróbuj przynajmniej porównać
#  opis zadania z rozwiązaniem, ale oczywiście zachęcam do rozwiązywania - jak się uda - satysfakcja murowana***

# W tym ćwiczeniu zaimplementujemy karcianą grę w wojnę. Jeśli ktoś nie pamięta zasad: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)

# Na razie skorzystamy z opcji "pokój", tzn. jeżeli obaj gracze mają taką samą kartę, to karty te wracają do graczy na dół ich talii.

# Zacznijmy od drobnego przygotowania. Pamiętasz co to słownik? Tworzymy go z wykorzystaniem nawiasów klamrowych, np

# aCard = {"Figure":"King", "Power":12}
# print(aCard)
# print(aCard['Figure'])
# print(aCard['Power'])
# daje w wyniku:

# {'Figure': 'King', 'Power': 12}
# King
# 12
# W definicji karty mamy teraz 2 informacje. Figurę karty - tutaj "King" i jej moc -
#  tutaj 12. Kiedy chcesz się dowiedzieć tylko o figurze lub tylko o mocy karty stosujesz notację

# aCard['Figure']
# aCard['Power']
# Dodatkowo, jeśli chcesz dodać nową właściwość karty, np Color, to możesz to zrobić tak:

# aCard['Color'] = 'Heart'
# print(aCard['Color'])
# Po tej powtórce zacznijmy zadanie! Na wejściu masz następujące listy:

# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = [
#     {'Figure':'Ace',  'Power':14},
#     {'Figure':'King', 'Power':13},
#     {'Figure':'Queen','Power':12},
#     {'Figure':'Jack', 'Power':11},
#     {'Figure':'10',   'Power':10},
#     {'Figure':'9',    'Power':9}]
# Są one bardzo podobne do listy z poprzednego zadania, tylko teraz elementami listy figures są słowniki.

# 1. Korzystając z rozwiązania poprzedniego LAB-a napisz

# w zmiennej allCards zapisz pustą listę

# napisz zagnieżdżoną pętlę, która

# dla każdego koloru z listy colors

# i dla każdej figury z listy figures

# zapamięta w zmiennej aCard figurę (jest to słownik) - uwaga przepisując wartość 
# skorzystaj z metody copy, która rzeczywiście tworzy kopię obiektu (  aCard = f.copy()  )

# do słownika aCard doda właściwość 'Color' o wartości w tej chwili przetwarzanego koloru

# obiekt aCard dodaj do listy allCards

# 2. Zaimportuj moduł random i potasuj karty. Możesz je na tym etapie wyświetlić

# 3. Utwórz puste listy player1 i player2 i wybraną przez siebie metodą daj im równą ilość kart z allCards

# 4. Znowu możesz wyświetlić karty obu graczy

# 5. Ponieważ gra w wojnę trwa tak długo, aż jeden z graczy zostanie bez kart,
#  to napisz pętlę while, która będzie się wykonywać tak długo jak długo każdy z graczy ma karty

# 6. Korzystając z metody pop():

# w zmiennej card1 zapisz kartę pobraną z listy player1

# w zmiennej card2 zapisz kartę pobraną z listy player2

# 7. Porównaj właściwość 'Power' dla card1 i card2, następnie:

# jeżeli karty mają jednakową moc, zwróć je na koniec listy z kartami graczy:

# card1 wraca na koniec player1

# card2 wraca na koniec player2

# jeżeli card1 ma większą moc niż card2, to obie karty dopisz na końcu player1

# jeżeli card2 ma większą moc niż card1, to obie karty dopisz na końcy player2

# Podejmując wyżej opisaną decyzję wyświetl informację o kartach o tym kto wygrał.
#  Możesz dodatkowo wyświetlać ilość kart u gracza 1 i 2 lub np. tyle gwiazdek ile kart ma gracz numer 1 - sam zdecyduj

# 8. Za pętlą ustal kto ma karty i wyświetl informację o tym,  kto wygrał

# 9. Uruchom skrypt i zobacz jak komputer się bawi. Z opcją pokój rozgrywki mogą
#  nigdy się nie skończyć... więc w razie czego pamiętaj, że wykonanie skryptu możesz przerwać naciskając CTRL+C

# Jedno z uruchomień, które wreszcie się skończyło u mnie wyglądało tak:

# PLAY-1 	 12 	 11 	*************
# PLAY-1 	 13 	 12 	**************
# PLAY-2 	 9 	 11 	*************
# PLAY-1 	 14 	 10 	**************
# PLAY-1 	 14 	 10 	***************
# PLAY-1 	 14 	 12 	****************
# PLAY-2 	 9 	 13 	***************
# PLAY-1 	 14 	 10 	****************
# PLAY-1 	 13 	 9 	*****************
# PLAY-1 	 12 	 10 	******************
# PLAY-2 	 9 	 13 	*****************
# =EQUAL 	 11 	 11 	*****************
# PLAY-1 	 12 	 11 	******************
# PLAY-1 	 11 	 9 	*******************
# =EQUAL 	 13 	 13 	*******************
# PLAY-1 	 12 	 9 	********************
# PLAY-1 	 14 	 13 	*********************
# PLAY-1 	 10 	 9 	**********************
# PLAY-1 	 14 	 11 	***********************
# PLAY-2 	 10 	 13 	**********************
# PLAY-1 	 14 	 13 	***********************
# PLAY-1 	 12 	 10 	************************
# PLAYER 1 WON!!!!



# a_card = {"Figure":"King", "Power":12}

# print(a_card['Figure'], a_card['Power'])

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
    if max % 2 == 0:
        player_1.append(all_cards[i])
    else:
        player_2.append(all_cards[i])
    max-=1

while len(player_1) != 0 and len(player_2) != 0:
    card_1 = player_1.pop(0)
    card_2 = player_2.pop(0)
    print('Karta gracza pierwszego:', card_1['Figure'], '\tKarta gracza drugiego:', card_2['Figure'])
    if card_1['Power'] == card_2['Power']:
        print('Remis, karty wracaja do decku graczy')
        player_1.append(card_1)
        player_2.append(card_2)
    elif card_1['Power'] > card_2['Power']:
        print('Wygrał Gracz pierwszy, obie karty sa dodawane do jego decku')
        player_1.append(card_1)
        player_1.append(card_2)
    elif card_1['Power'] < card_2['Power']:
        print('Wygrał Gracz drugi, obie karty sa dodawane do jego decku')
        player_2.append(card_1)
        player_2.append(card_2)
    print('Gracz 1 posiada', len(player_1), 'kart', '\nGracz 2 posiada', len(player_2), 'kart')
    
if len(player_1) == 0:
    print('Wygrał gracz 2!')
else:
    print('Wygrał gracz 1!')
        





















