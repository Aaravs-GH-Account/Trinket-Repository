import random
num=random.randint(1,20)
for i in range(5):
  a=int(input('Guess my number from 1 and 20!'))
  if a<num:
    print('Too low!')
  elif a>num:
    print('Too high!')
  else:
    print('You got it!')
    break