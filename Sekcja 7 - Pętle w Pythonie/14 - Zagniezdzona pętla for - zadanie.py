# i = 10
# result = 1

# for x in range(1, i+1):
#     result*=x
#     print(i, result)
    
# pamiętaj, wyliczajac tą silnie tutaj za kazda pętlą bierze wynik z poprzedniej
# i mnozy przez nowa wartosc zmiennej pobranej z range

# czyli nie robi za kazdym razem np 1*2*3*4, tylko 1*2*3 to wynik z poprzedniej
# pętli for, a potem tylko mnoży przez 4, czyli jakby (1*2*3)*4

# to bylo zadanie 1

# x = 10

# for i in range(1, x+1):
#     result = 1
#     for j in range (1, i+1):
#         result*=j
#         print(i, result)
        
# to bylo zadanie 2, robilismy tutaj silnie, ale po prostu pokazywalismy
# po kolei wartosci mnozenia liczb z silni

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for x in list_noun:
    for j in list_adj:
        print(x, j)
        
# to bylo zadanie 3