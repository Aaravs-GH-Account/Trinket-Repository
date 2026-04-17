import time as t,os,random as r
def code():
  CapLet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  LowLet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  SpeChar=['`','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
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
  print('A very strong password is: \n{}{}{}{}{}{}{}{}{}{}{}{}'.format(var4,var7,var6,var8,var2,var10,var5,var11,var1,var9,var3,var12,))
  t.sleep(3)
  os.system('clear')
code()
while True:
  b=input("Do you want a new password? Answer'Yes' or answer 'No'.")
  if b=='Yes' or b=='yes':
    os.system('clear')
    code()
  elif b=='No' or b=='no':
    os.system('clear')
    print('Thank you for using the password generator!')
    t.sleep(5)
    os.system('clear')
    break
  else:
    print("You have not typed in a valid response! Just type 'Yes' or 'No'!")