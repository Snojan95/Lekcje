import time
 
# sprawdzenie wersji pythona
import sys
# print(sys.version)
 
# # zamiast
# print(time.clock(), time.localtime(time.clock()))
# # korzystaj z funkcji time.perf.counter():
# print(time.perf_counter(), time.localtime(time.perf_counter()))

# print('\n')

# print('Current time is... unix epoch', time.time())

# ta komenda wyswietla czas w wartosci unixowiej (od 1 stycznia 1970) w sekundach

# print('\n')

# print('Current time is... tuple', time.localtime(time.time()))

# ta komenda wyswietla dokladnie czas, juz tak normalniej jak znamy, ale
# niestety troche sztywno, w tuplu
# Current time is... tuple time.struct_time(tm_year=2022, tm_mon=11, tm_mday=19, tm_hour=10, tm_min=54, tm_sec=14, tm_wday=5, tm_yday=323, tm_isdst=0)

# 

# print('\n')

# print('Current time is... for human', time.asctime(time.localtime(time.time())))

# ta komenda juz wyswietla czas normalnie, a nie w jakis dziwny sposob
      
# print('Current time is... for human')
# ta linijka jest juz nieważna, chodziło tu o moduł clock() który jest juz
# nieobslugiwany, widac instrukcje jak go zastapic wyzej, na poczatku kodu

import calendar

# print(calendar.month(2022, 11, w=5, l=2))

# ta komenda wyswietla kalendarz dla danego miesiaca, 2022 i 11 to rok i miesiac
# w = 5 to atrybut ktory definiuje ze na kazy dzien ma byc dedykowane 5 linijek
# czyli jakby 5 wierszy od gory do dolu
# l=2 definiuje ze odstepy miedzy wierszami maja wynosic 2

# print('weekday is:', calendar.weekday(2022, 11, 19))

# ta komenda wyswietla nam jaki dzien tygodnia był podczas wprowadzonej daty
# dla tej daty wynik to sobota, wiec wynik wynosi 5, pamietamy ze python liczy od 0
# wiec poniedzialek = 0

calendar.setfirstweekday(0)

# print(calendar.month(2022, 11))

# komenda setfirstweekday 6 spowoduje ze wyswietlony kalendarz bedzie mial niedziele
# jako pierwszy dzien, zamiast poniedzialku
#    November 2022
# Su Mo Tu We Th Fr Sa
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30
# ALE PAMIETAJ! to wplywa tylko na wyswietlanie kalendarza, poniedzialek
# nadal traktowany jest jako wartosc 0, a nie niedziela

# print(calendar.isleap(2022))

# ta komenda wyswietla nam czy dany rok jest rokiem przystepnym, czy nie
# dla 2022 ta wartosc bedzie False

# print('leap days between 2012-2022:', calendar.leapdays(2012, 2022))

# ta komenda pokazuje ile bylo dni przestepnych w przedziale 2012-2021
# pamietaj, tutaj sprawdza tylko do 2021, bo python nie bierze pod uwage 
# ostatniego argumentu, traktuje jako stop i nie czyta go

print(calendar.calendar(2022))

# ta funkcja drukuje kalendarz za cały rok!






















