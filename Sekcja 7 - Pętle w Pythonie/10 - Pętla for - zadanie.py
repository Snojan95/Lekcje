data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
# for msg in data:
#     print(msg.upper())
    
# to bylo zadanie 1

# for s in data:
#     elements = s.split(':')
#     print(elements[0].upper())
#     print(elements[1].lower())
    
# zwroc uwage ze wyswietla wszystkie wartosci po kolei, bo metoda for
# przetwarza wszystkie wartosci listy jedna po drugiej!

for s in data:
    elements = s.split(':')
    print(elements[0])
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])