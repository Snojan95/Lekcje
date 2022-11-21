# article = '''
# Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

# '''
# tutaj zmienna jest zmienna blokową, dzieki potrojnym apostrofom w linijce 1 i linijce 3

# print(article.upper())

# metoda .upper powoduje ze wszystkie litery w zmiennej article zostaja zamienione na duze litery

# print(article.lower().replace('monty', 'flying'))

# metoda lower jak wyżej, ale zmienia na małe litery, a z kolei metoda replace zamienia w zmiennej wartosc 
# pierwsza, na wartosc druga w kazdej instancji w zmiennej

# print(article.split(' '))

# metoda split dodaje wpisany w nawias symbol jako miejsce pomiedzy obiektami w stringu

# print('word python appears', article.lower.count('python'),'times')
# print('to print the \\ you need to put \\ twice in your text like this: \\\\')
# print('The best hits of \'80s!!!')
# print("The best hits of '80s!!!")
# amountPLN = 600
# usd_price = 4.65
# eur_price = 4.23
# print('cur','exchange','amount', sep=('\t'))
# print('USD', usd_price, amountPLN/usd_price, sep=('\t'))
# print('EUR', eur_price, amountPLN/eur_price, sep=('\t'))

# \t powoduje dodanie przerwy w postaci tabulatora, a \n zaczyna tekst od nowej linijki

value_as_text = '123.45'
factor = 1.23
print('value is', value_as_text, 'factor is', factor, 'value*factor=', float(value_as_text)*factor)