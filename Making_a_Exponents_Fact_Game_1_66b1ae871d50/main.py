import random
num1=random.randint(1,100)
num2=random.randint(1,100)
num3=random.randint(1,1000)
num4=random.randint(1,1000)
tries=3
#question1
for i in range(tries):
  a=int(input('If x='+str(num1)+' and y='+str(num2)+' then what is x^y'))
  if a==num1**num2:
    print('Great job! You figured it out!')
    break
  else:
    tries=tries-1
    if tries>0:
      print('Try again! You have ' + str(tries) + ' tries left.')
    else:
      print('GAME OVER!')
if tries>0:
  print("Brace yourself! It's Level 2!")
  for i in range(tries):
    a=int(input('If x='+str(num3)+' and y='+str(num4)+' then what is x^y'))
    if a==num3**num4:
      print('Great job! You figured it out!')
      break
    else:
      tries=tries-1
      if tries>0:
        print('Try again! You have ' + str(tries) + ' tries left.')
      else:
        print('GAME OVER!')