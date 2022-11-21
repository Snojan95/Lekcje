# for candidate in range(2,31):
#     for divider in range(2, candidate):
#         if candidate % divider ==0:
#             print("%2d is not a prime number - divider is %2d" % (candidate, divider))
#             break

# metoda break powoduje ze gdy mamy juz jeden hit, kod znajdzie pasujacy efekt
# to pętla zostanie przerwana. Tutaj przerwana zostaje pętla wewnetrzna i wracamy
# do pętli zewnętrznej. Bez komendy break kod wypluwa wyniki dla każdego dzielnika
# np:
    # 12 is not a prime number - divider is  2
    # 12 is not a prime number - divider is  3
    # 12 is not a prime number - divider is  4
    # 12 is not a prime number - divider is  6
# a z komenda break wyglada to tak:
    # 10 is not a prime number - divider is  2
    # 12 is not a prime number - divider is  2
    # 14 is not a prime number - divider is  2
    
# for candidate in range(2,31):
#     is_prime = True
#     for divider in range(2, candidate):
#         if candidate % divider ==0:
#             is_prime = False
#             print("%2d is not a prime number - divider is %2d" % (candidate, divider))
#             break
#     if is_prime:
#         print('%2d is prime!' % (candidate))

# wezmy za przyklad liczbe 7, pierwsze for lapie wartosc 7, ustawia zmienna
# is_prime na true, leci dalej, probuje dzielic (pamietaj ze % uzyty jako znak
# matematyczny wypluwa wynik RESZTY, czyli np 10%3 wypluje wynik 1/3!), jesli
# znajdzie w wewnetrznej pętli for wynik dzielenia z reszta to szuka dalej,
# ale jesli znajdzie wynik dzielenia bez reszty to egzekwuje zagniezdzone if: o to:  is_prime = False
# print("%2d is not a prime number - divider is %2d" % (candidate, divider))
# break
# jesli na calej dlugosci nie znajdzie, to egzekwuje if: (if is_prime:) ktore jest przypisane
# do zagniezdzonego for: (for divider in range(2, candidate):)

for candidate in range(2,31):
    for divider in range(2, candidate):
        if candidate % divider ==0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    else:
        print('%2d is prime!' % (candidate))

# ta konstrukcja jest identyczna w skutkach do tej nad nia, ale zrobilismy
# to nieco inaczej, laczac zagniezdzona metode for z metoda else, to jest
# unikatowa dla pythona konstrukcja, w innych jezykach trzeba by bylo
# zrobic cos co bardziej przypomina konstrukcje pierwsza, a nie ta druga

# PAMIETAJ, W ZAKRESIE RANGE WARTOSC STOP JEST IGNOROWANA, CZYLI 31 NIE JEST SPRAWDZANE