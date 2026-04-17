import random as r
#creating a list
var1=['hello','hello again',0,1,2,3,4,0.0,True,False]
print(var1)
# defining the total number of items in a list
totalitems=len(var1)
print(totalitems)
#indexing in a list
print(var1[0])
print(var1[1])
print(var1[2])
print(var1[3])
print(var1[4])
print(var1[5])
print(var1[6])
print(var1[7])
print(var1[8])
print(var1[9])
print(var1[9])
print(var1[8])
print(var1[7])
print(var1[6])
print(var1[5])
print(var1[4])
print(var1[3])
print(var1[2])
print(var1[1])
print(var1[0])
#backward indexing
print(var1[0])
print(var1[-9])
print(var1[-8])
print(var1[-7])
print(var1[-6])
print(var1[-5])
print(var1[-4])
print(var1[-3])
print(var1[-2])
print(var1[-1])
print(var1[-1])
print(var1[-2])
print(var1[-3])
print(var1[-4])
print(var1[-5])
print(var1[-6])
print(var1[-7])
print(var1[-8])
print(var1[-9])
print(var1[0])
#indexing with random indexes
import random
a=int(input('How many times do you want different things from the list on the top to pop up?'))
for i in range(a):
  print(var1[random.randint(-9,9)])
var1=[0,'banana',2.0,True,False]
#modifiying a list value
var1[0]=5
print(var1)
#adding items to the list
#append functions
var1.append('banana2')
var1.append('nano banana')
print(var1)
#inserting added functions into places we want
var1.insert(3,'banana1')
var1.insert(1,'hello')
print(var1)
#extend
var1.extend(['banana3',False,True])
print(var1)
#removing items from the list
#remove
var1.remove(False)
var1.remove(True)
print(var1)
#throw indexing
#pop
var1.pop(-3)
print(var1)
#reversing a list
var1.reverse()
print(var1)
r.shuffle(var1)
print(var1)
#looping through your list
for i in var1:
  print(i)
#Randomly choosing an item from the list
#Choice
var2=r.choice(var1)
print var2
print()