# muscle_pain = False
# fever = False
# weakness = True
# is_man = False

# # print('podejrzenie grypy' if muscle_pain and fever and weakness else 'raczej nie grypa')

# if muscle_pain and fever and weakness or is_man and (muscle_pain or fever or weakness):
#     print('podejrzenie grypy')
# elif weakness and not fever and not muscle_pain:
#     print('po prostu odpocznij')
# else:
#     print('mozesz byc przeziebiony')

draco_molested = True
przecena_udemy = True
dorian_kupil = True

print('Dzisiaj juz cie molestowalem' if draco_molested else \
      'dobra, kurwa, dzisiaj za drogo' if not przecena_udemy else \
      'czemu jeszcze nie kupiłes kurwa' if przecena_udemy and not dorian_kupil else\
      'dobra robota')
      
    
    
