# zaprezentowane w tym kodzie sa dwie metody uzywania instrukcji if/elif
# pierwszy jest tym gorszym, ale warto o nim wiedziec tak czy srak

age = 27
is_drunk = True
is_restricted_area = False

if age < 18:
    print('jestes za mlody zeby kupic alkohol')
else:
    if is_drunk:
        print('jestes zbyt pijany zeby sprzedac ci alkohol')
    else:
        if is_restricted_area:
            print('nie moge sprzedac tutaj alkoholu')
        else:
            print('walnij se grzdyla mlody')
# takie troglodyckie schody nazywa sie "nested if" generalnie nie polecamy
# ~Magda Gesler
            
print('-----')

if age < 18:
    print('jestes za mlody zeby kupic alkohol')
elif is_drunk:
    print('jestes zbyt pijany zeby sprzedac ci alkohol')
elif is_restricted_area:
    print('nie moge sprzedac tutaj alkoholu')
else:
    print('walnij se grzdyla mlody')

# To co widzisz tutaj to to samo co to na samej górze, ale o wiele czytelniejsze