persons = ['Elizabeth', 'Steven@sales.mycompany.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']

domain = 'mycompany.com'

emails = []

# for person in persons:
#     if '@' in person:
#         emails.append(person)
#     else:
#         email = person + '@' + domain
#         emails.append(email)

# to jest wykonanie tego zadania bez instrukcji continue, if wykrywa że jesli
# jest malpa, to wystarczy wrzucic pozycje z listy persons do listy emails
# w przeciwnym wypadku instrukcja else tworzy maila a dopiero potem go dodaje do listy

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)
    
# continue zamieniło tutaj instrukcje else, ale nie dziala w taki sam sposob
# jesli w wartosci z listy istnieje malpa i kod wchodzi do instrukcji zawartych
# w if, ta wartosc zostaje dodana do listy emails, potem kod natrafia na 
# instrukcje 'continue' ktora powoduje ze ignorowana jest dalsza czesc po if
# i kod wraca do argumentu for (mozesz zobaczyc to w debuggerze)

