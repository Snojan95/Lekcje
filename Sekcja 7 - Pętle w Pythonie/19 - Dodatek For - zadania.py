# fibonacci_iterations = 20
# a1 = 0
# a2 = 1
# a3 = 0

# for x in range(20):
#     print('a1 + a2 =', a3)
#     a1 = a2
#     a2 = a3
#     a3 = a1+a2
    
# to było zadanie 1

tekst = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
    '''
    
# text_2 = tekst.replace('\n', ' ').split(' ') 

# for x in text_2:
#     if x.find('p') >= 0:
#         print(x)
        
# to było zadanie 2, pamietaj ze metoda find po znalezieniu w slowie p dodaje
# do wartosci 1 - czyli ilosc znalezionych liter 'P', dlatego uzywamy do tego
#  znaku większa równa sie >=

# dictionary = {'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'} 

# for word in dictionary.keys():
#     print(word, '-', dictionary[word])
    
# to było zadanie 3 

word_dictionary = {}
list_of_words = tekst.replace('\n', ' ').split(' ')
for word in list_of_words:
    if word in word_dictionary.keys():
        word_dictionary[word] = word_dictionary[word]+1
    else:   
        word_dictionary.setdefault(word, 1)
    
print(word_dictionary)

#  to było zadanie 4
    
