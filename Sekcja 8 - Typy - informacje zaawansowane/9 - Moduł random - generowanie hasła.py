# for i in range(32,127):
#     print(i, chr(i))
    
# ta komenda wyswietla nam czesc tabeli ASCII

import random

ints = range(33,127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))
print('Password is:', password)