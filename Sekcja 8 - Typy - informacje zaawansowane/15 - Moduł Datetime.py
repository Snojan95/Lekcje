import datetime

# print('Minimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)

# # Python obsluguje lata w przedziale od 1 do 9999

# d1 = datetime.timedelta(days=1, hours=2, minutes=-30)

# # to jest odniesienie do przyszlosci, jakby ktos powiedzial ze zrobi cos za
# # dzien, 2 godziny i minus 30 min, czyli za dzien i poltora godziny

# d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)

# # to jest odniesienie do przeszlosci, jakby ktos powiedzial ze zrobil cos
# # wczoraj, minus 2 godziny i 3 minuty

# # print(d1)
# # print(d2)

# # print('timedelta sum:', d1+d2)

# # tutaj dodajac do siebie te dwie wartosci dostajemy wynik jakbysmy tracili
# # jeden dzien, ale zyskiwali 23h27min, czyli jakbysmy tracili 33 min

# # print('Today is:', datetime.date.today())

# today = datetime.date.today()

# days_to_pay = datetime.timedelta(days=7)

# print('Today is:', today)

# print('Bills should be paid within:', days_to_pay.days, 'days')

# print('The bill should be paid till:', today + days_to_pay)

# # dodajac tutaj dni okreslone w days to pay do wartosci dnia dzisiejszego
# # otrzymujemy termin za 7 dni

# end_of_the_world = datetime.date.max

# print('Wg. Pythona ostatnim dniem swiata bedzie:', end_of_the_world, \
#       'i będzie to dzien:', end_of_the_world.weekday())

# born_date = datetime.date(1995, 11, 3)

# today = datetime.date.today()
# print(today - born_date, '- ilosc dni ktore przezylem')

print('now:', datetime.datetime.now())

# pokazuje czas ktory jest teraz

print('Today:', datetime.datetime.today())

# w sumie to jak wyzej

print('UTC now:', datetime.datetime.utcnow())

# pokazuje czas greenwich - 0

print('weekday:', datetime.datetime.today().weekday())

# pokazuje dzien tygodnia

print('%a', datetime.datetime.now().strftime('%a'))

# pokazuje dzien tygodnia, zapisany jako skrot (w dniu gdy to robilem 'Mon')

print('%A', datetime.datetime.now().strftime('%A'))

# pokazuje dzien tygodnia zapisany pelna nazwa

print('%w', datetime.datetime.now().strftime('%w'))

# wyswietla dzien tygodnia jako liczbe, ale tutaj jako 0 liczymy niedziele!

print('%Y-%m-%d_%H_%M_%S_%f', datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f'))

# tutaj dostajemy juz pelen zwrot, year-month-day-hour-minute-second-milisecond

print(datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f'))































