import turtle,random
bob=turtle.Turtle()
bobspaper=turtle.Screen()
bob2=turtle.Turtle()
bob3=turtle.Turtle()
a=input('What do you want your paper color to be?')
if a=='black':
  bob.color('white')
  bob2.color('white')
  bob3.color('white')
else:
  bob.color('black')
  bob2.color('black')
  bob3.color('black')
bobspaper.bgcolor(a)
bob.shape('turtle')
bob2.shape('turtle')
bob3.shape('turtle')
def c(b,d,e):
  e.up()
  e.goto(b,d)
  e.down()
c(-70,175,bob)
bob.write('Hello!',font=('Courier',30,'bold'))
b=int(input('How many steps do you want the turtle to move per button press?'))
def turtleforward():
  bob3.forward(b)
def turtleleft():
  bob3.setheading(180)
def turtleright():
  bob3.setheading(0)
def turtleup():
  bob3.setheading(90)
def turtledown():
  bob3.setheading(270)
def mouseclick(a,b):
  bobspaper.tracer(0)
  bob3.setheading(bob3.towards(a,b))
  bob3.goto(a,b)
  bobspaper.tracer(1)
  print(int(bob3.xcor()),int(bob3.ycor()))
  if int(bob3.xcor())==1 and int(bob3.ycor())==1:
    c(-200,-25,bob)
    bob.write('You WIN😎',font=('Courier',75,'bold','italic'))
def mousedrag(a,b):
  bobspaper.tracer(0)
  bob3.goto(a,b)
  bobspaper.tracer(1)
bobspaper.listen()
bobspaper.onkey(turtleforward,'space')
bobspaper.onkey(turtleleft,'left')
bobspaper.onkey(turtleright,'right')
bobspaper.onkey(turtleup,'up')
bobspaper.onkey(turtledown,'down')
bobspaper.onclick(mouseclick)
bob3.ondrag(mousedrag)
c=input('Where do you want your turtle to go?').split
