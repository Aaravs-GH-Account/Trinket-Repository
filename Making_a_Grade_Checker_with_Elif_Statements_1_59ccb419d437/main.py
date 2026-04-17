var=int(input('What marks did you get on your most recent test?'))
if var>89 and var<101:
  print('You got an A!😁')
elif var>79 and var<90:
  print('You got a B!😄')
elif var>69 and var<80:
  print('You got a C!😀')
elif var>59 and var<70:
  print('You got a D.😐')
elif var>49 and var<60:
  print('You got a E.😢')
elif var<50 and var>0:
  print('You failed your test!⚠️')
elif var<0:
  print('CENSORED GRADE')
else:
  print('You are a genius!🧐🤯😎')