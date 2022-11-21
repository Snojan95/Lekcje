# s = 'To jest tekst'
# print(s[9])
# print(s[2:6])
# print(s[:8])
# print(s[8:])
# print(s[:8],s[8:])

# tutaj ta metoda s sluzy do wydrukowania tylko okreslonych znakow ze zmiennej
# znak :8 powoduje ze python zaczyna drukowanie od poczatku i konczy na osmym znaku
# a z kolei 8: spowoduje ze bedzie drukowal od osmego do konca
# logicznie idac, 2:6 wydrukuje nam od 2 do 6 znaku
# pamietaj ze python liczy od zera!

# msg = 'Dokument "CV.doc" został wydrukowany na drukarce: HP'
# print(msg.find(':'))
# print(msg[msg.find(':'):])
# print(msg[msg.find(':')+2:])
# print(msg[msg.find('"')+1:])
# tmp = msg[msg.find('"')+1:]
# print(tmp[:tmp.find('"')])

# z pomoca metody find znajdziemy konkretny znak w danym stringu i go wydrukujemy
# zasada z : jest ta sama, leci do konca, albo zaczyna od poczatku
# dodanie +1 albo +2 spowoduje ze znajdzie znak i bedzie printowal od nastepnego
# albo drugiego z kolei znaku po tym ktory znalezlismy
# liczba która odpowiada pozycji w stringu musi byc w nawiasach kwadratowych

# q = 'THE EYES'
# print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])

# w = 'a gentleman'
# print(w)
# print(w[3],w[6],w[7],w[2],w[0],w[4],w[5],w[1],w[8:])
# print(w[3]+w[6]+w[7]+w[2]+w[0]+w[4]+w[5]+w[1]+w[8:])

# a = 'the morse code'
# print(a)
# print(a[1:3]+a[a.find('r')]+a[a.find('e')], a[10:12]+a[4]+a[2], a[12]+a[11]+a[0]+a[7])

# 'Program "Kropka nad i" nadamy o: 22:00'
# line = 'Program "Kropka nad i" nadamy o: 22:00'
# time = line[line.find(':')+2:]
# print(time)
# tmp = line[line.find('"')+1:]
# title = tmp[:tmp.find('"')]
# print(title, time)
# print(tmp)

# 'Program "Pytanie na śniadanie" nadamy o: 6:00'
prog = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
czas = prog[prog.find(':')+2:]
print(czas)
tyt = prog[prog.find('"')+1: prog.find('"', prog.find('"')+1)]
print(tyt, czas)