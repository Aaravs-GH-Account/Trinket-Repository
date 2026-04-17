import turtle
import random
bob=turtle.Turtle()
bobsdrawingspace=turtle.Screen()
a=input('What color would you like the screen to be?')
bobsdrawingspace.bgcolor(a)
def bobssquare(b,c,d):
  a=input('What color do you want one of the three shapes to be?(Try not to choose a color that is the same as your background or it will not show the shape; the shape will only blend in.)')
  bob.color(a)
  bob.up()
  bob.goto(c,d)
  bob.down()
  bob.fillcolor(a)
  bob.begin_fill()
  for i in range(4):
    bob.forward(b)
    bob.left(90)
  bob.end_fill()
bobssquare(random.randint(20,100),random.randint(-150,150),random.randint(-200,200))
bobssquare(random.randint(20,100),random.randint(-150,150),random.randint(-200,200))
bobssquare(random.randint(20,100),random.randint(-150,150),random.randint(-200,200))