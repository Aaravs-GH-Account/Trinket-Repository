#!/bin/python3
import os, time as t
var1=[]
while True:
  #a=int(input('Enter the number of items in the list.'))
  print("1.Display the list\n2.Add an item to the list\n3.Remove an item from the list\n4.Change an item in the list\n5.Display the length of the list\n6.Exit the program")
  a=input('Which one do you want to do? Just type in the number or the command.')
  if a=='1' or a=='Display the list' or a=='display the list':
    print(var1)
  elif a=='2' or a=='Add an item to the list' or a=='add an item to the list':
    b=input('What item do you want to add to the list?')
#    c=int(input('Which index do you want the added item to go into? The indexes work like this. The first object in the list is index 0. The second is index one. The third is index 2 ect..'))
    var1.append(b)
  elif a=='3' or a=='Remove an item from the list' or a=='remove an item from the list':
    d=int(input('Which index do you want the removed item to go from? The indexes work like this. The first object in the list is index 0. The second is index one. The third is index 2 ect..'))
    var1.pop(d)
  elif a=='4' or a=='Change an item in the list' or a=='change an item in the list':
    e=int(input('Which index is the item you want to change in? The indexes work like this. The first object in the list is index 0. The second is index one. The third is index 2 ect..'))
    f=input('What is the item do you want to switch it to?')
    var1[e]=f
  elif a=='5' or a=='Display the length of the list' or a=='display the length of the list':
    print('The number of items in the list is '+str(len(var1)))
  elif a=='6' or a=='Exit the program' or a=='exit the program':
    for i in range(1):
      print('EXITING',end='')
      for i in range(3):
        t.sleep(1)
        print(".",end="")
      t.sleep(1)
      os.system('clear')
    print('Successfully Exited!')
    t.sleep(1)
    os.system('clear')
    break
  else:
    print('You have not typed in a valid response! Please redo your answer!')