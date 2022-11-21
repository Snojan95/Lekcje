it_rains = False

if it_rains:
    print('zostajemy w domu')
else:
    print('wychodzimy na piwko')
    
print('zostajemy w domu' if it_rains else 'wychodzimy na piwko')

# nazwa jednolinijkowego wyrazenia if/else to "ternary operator"
#  ternary operatora używa się raczej tylko w prostych wypadkach
# to mniej jasny i bardziej zagmatwany sposob, ale dobry do tego 
# zeby nieco skrocic kod
