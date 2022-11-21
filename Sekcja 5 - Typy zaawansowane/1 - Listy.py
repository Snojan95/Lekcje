# kraje = ['FR', 'US', 'DE', 'RU']
# kraje[1] = 'GB'
# print(kraje)
# print(kraje[1])
# kraje.append('PL')
# print(kraje)
# kraje.insert(0, 'ES')
# insert wkłada na wymieniona najpierw pozycje wymieniona pozniej wartosc
# print(kraje)
# kraje.remove('RU')
# ta komenda usuwa z listy kazda instancje wartosci wymienionej w nawiasie
# print(kraje)
# kraje.sort()
# sort domyslnie sortuje liste alfabetycznie
# print(kraje)
# kraje.reverse()
# reverse służy do zamieniania calkowicie kolejnosci listy
# print(kraje)
# print(kraje.pop(0))
# pop służy do wyciagania elementu na wymienionym miejscu z listy, element jest pokazywany oddzielnie, a potem przestaje figurowac na liscie
# print(kraje)
# print(kraje.index('GB'))
# print(kraje.count('ES'))
# nowe_kraje = ['FI', 'SE']
# kraje.extend(nowe_kraje)
# print(kraje)
# kopia_kraje = kraje.copy()
# ta komenda tworzy kopie listy pod inna nazwa variable, jest to wazne, bo nie zamienia variabla oryginalnego, tylko tworzy kopie
# print(kopia_kraje)
# kopia_kraje.clear()
# komenda clear usuwa zawartosc listy, kto by pomyslal, ale ZAWARTOSC, nie sama liste!
# print(kraje)

# liczby = [1, 2, 3, 4, 5]
# kopia_liczby = liczby.copy()
# print(liczby)
# print(kopia_liczby)
# kopia_liczby.clear()
# print(liczby)
# print(kopia_liczby)

hits_titles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hits_titles)
hits_titles.extend(['CHILD IN TIME', 'AGAIN'])
# to co niżej jest alternatywą do tego co jest wyżej
# hits_titles.append('CHILD IN TIME')
# hits_titles.append('AGAIN')
# print(hits_titles)
hits_titles.insert(2, 'HOTEL CALIFORNIA')
# print(hits_titles)
hits_titles.insert(0, 'THE SOUND OF SILENCE')
# print(hits_titles.index('HOTEL CALIFORNIA'))
hits_titles.remove('HOTEL CALIFORNIA')
# print(hits_titles)
hits_titles.pop(0) 
hits_titles.insert(0, 'ENJOY THE SILENCE')
# print(hits_titles)
hits_to_read = hits_titles.copy()
# print(hits_to_read)
hits_to_read.reverse()
print(hits_to_read)
print(hits_to_read.sort())
# print(hits_to_read.pop(0), hits_to_read.pop(1), hits_to_read)
additional_songs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hits_to_read.extend(additional_songs)
print(hits_to_read.count('WISH YOU WERE HERE'), hits_to_read.count('RIDERS ON THE STORM'))
hits_to_read.clear()
print(hits_to_read)





































