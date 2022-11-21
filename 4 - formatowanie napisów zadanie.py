name = 'Jan'
age = 27
days_in_year = 365
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, days_in_year*age))
# message = '%s is %d years old, so is about %d days old'
# print(message % (name, age, days_in_year*age))
value_1 = 1234567890
value_2 = 12345
msg = '{0:d} divided by {1:d} is {2:d} and the rest is {3:d}'
print(msg.format (value_1, value_2, value_1//value_2, value_1%value_2))
