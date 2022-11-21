# initial_capital = 20000
# percent = 0.03
# max_time_years = 10

# i = 0

# while i < max_time_years:
#     initial_capital = initial_capital + (initial_capital*percent)
#     i+=1
#     print('W roku:', i, 'ilosc srodkow na koncie wynosi:', initial_capital)
# else:
#     print('pod koniec okresu kwota na koncie wynosi:', initial_capital)
    
# to bylo zadanie 1

# number = 20730906
# temp = number
# suma = 0

# while temp > 0:
#     digit = number%10
#     suma+=digit
#     temp = temp//10
# else:
#     print(suma)
    
# to było zadanie 2

tekst = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
list_of_words = tekst.replace('\n', ' ').split(' ')

short_words = 0
long_words = 0
word_length = 6
i = 0

while i < len(list_of_words):
    if len(list_of_words[i]) > word_length:
        long_words+=1
    else:
        short_words+=1
        
    i+=1
print('Ilosc slow dluzszych niz 6 znakow:', long_words, '\nilosc slow krotszych niz 6 znakow:', short_words)

# to było zadanie 3
# zapomniales tutaj o tym jak dziala metoda len(), sprawdza ona dlugosc listy albo stringa
# poza tym kojarzyles o co kaman, ale jeszcze wiele cwiczenia przed toba
    