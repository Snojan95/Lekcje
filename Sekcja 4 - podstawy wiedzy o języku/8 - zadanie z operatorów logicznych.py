# print((46*5+50)*20+1022-1995)
# print((19*2+10)/2-19)
# print(2+2*2)
# print(7+7/7+7*7-7)

attendance = 0.4
score = 2.5
test = True
grad = test or ( attendance >=0.8 and score >=3.5)
print(grad)

attendance = 0.4
score = 2.5
test = True
grad = test and ( attendance >=0.8 and score >=3.0)
print(grad)