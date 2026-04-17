import time as t,os,random as r
CapLet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LowLet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
SpeChar=['`','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
a=int(input('How many characters do you want in your password? Pick within 4-12.'))
var1=str(r.randint(0,9))
var5=str(r.randint(0,9))
var9=str(r.randint(0,9))
var2=r.choice(CapLet)
var6=r.choice(CapLet)
var10=r.choice(CapLet)
var3=r.choice(LowLet)
var7=r.choice(LowLet)
var11=r.choice(LowLet)
var4=r.choice(SpeChar)
var8=r.choice(SpeChar)
var12=r.choice(SpeChar)
AllChar=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12]
if a==12:
  print(var1+var2+var3+var4+var5+var6+var7+var8+var9+var10+var11+var12+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==11:
  print(var1+var2+var3+var4+var5+var6+var7+var8+var9+var10+var11+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==10:
  print(var1+var2+var3+var4+var5+var6+var7+var8+var9+var10+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==9:
  print(var1+var2+var3+var4+var5+var6+var7+var8+var9+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==8:
  print(var1+var2+var3+var4+var5+var6+var7+var8+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==7:
  print(var1+var2+var3+var4+var5+var6+var7+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==6:
  print(var1+var2+var3+var4+var5+var6+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==5:
  print(var1+var2+var3+var4+var5+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
elif a==4:
  print(var1+var2+var3+var4+' is a very strong password! Please remember to find a way to memorize or write it down because it is very forgettable!')
else:
  print('You did not type in a valid answer! Restart this program and type in a number(JUST the number) and hit enter.')