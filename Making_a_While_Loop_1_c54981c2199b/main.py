#!/bin/python3
import os,time as t
var1=0
while var1 <10:
  print("Hello! It's working!")
  var1=var1+1
while True:
  b=int(input('How many exit times do you want?'))
  c=float(input('How long do you want each exit time to be?'))
  a=input('Continue or exit?')
  if a=='exit' or a=='Exit':
    for i in range(b):
      print("EXITING",end="")
      for i in range(3):
        t.sleep(c)
        print(".",end="")
      t.sleep(1)
      os.system('clear')
    print('Successfully Exited!')
    t.sleep(1)
    os.system('clear')
    break
  print('Continuing')