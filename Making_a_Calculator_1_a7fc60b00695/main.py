import os,time
a=input('Choose an operation to start!\n1. Addition +\n2. Subtraction -\n3. Multiplication *\n4. Division /\n5. Exponents ^\n6. Floor Division //\n7. Modulus %\n(Just type the number, name, or symbol of the operation you want to use):')
os.system('clear')
b,c=input('Enter 2 Numbers\n(Add a space between both Numbers and do not type anything other than the Numbers themselves):').split()
b=float(b)
c=float(c)
if a=='1' or a=='1.' or a=='addtion' or a=='Addition' or a=='+':
  print('{}+{}={}'.format(b,c,b+c))
elif a=='2' or a=='2.' or a=='subtraction' or a=='Subtraction' or a=='-':
  print('{}-{}={}'.format(b,c,b-c))
elif a=='3' or a=='3.' or a=='multiplication' or a=='Multiplication' or a=='*':
  print('{}*{}={}'.format(b,c,b*c))
elif a=='4' or a=='4.' or a=='division' or a=='Division' or a=='/':
  print('{}÷{}={}'.format(b,c,b/c))
elif a=='5' or a=='5.' or a=='Exponents' or a=='exponents' or a=='^':
  print('{}^{}={}'.format(b,c,b**c))
elif a=='6' or a=='6.' or a=='Floor division' or a=='Floor Division' or a=='floor division' or a=='floor Division' or a=='//':
  print('{}//{}={}'.format(b,c,b//c))
elif a=='7' or a=='7.' or a=='Modulus' or a=='modulus' or a=='%':
  print('{}%{}={}'.format(b,c,b%c))
else:
  print("Read the Instructions that come with each step you have to take! You typed in something that you weren't supposed to!")