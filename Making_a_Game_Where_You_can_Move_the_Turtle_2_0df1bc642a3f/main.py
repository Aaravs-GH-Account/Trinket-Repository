import turtle,random
bob=turtle.Turtle()
bobspaper=turtle.Screen()
bob2=turtle.Turtle()
bob3=turtle.Turtle()
print("Left Arrow Key (Click Left Arrow Key) - Turn Turtle Left Specified Amount\nRight Arrow Key (Click Right Arrow Key) - Turn Turtle Right Specified Amount\nUp Arrow Key (Click Up Arrow Key) - Moves Turtle Forward\nDown Arrow Key (Click Down Arrow Key) - Moves Turtle Backward\nW Key (Click 'W' Key) - Lifts Turtle Off Paper\nS Key (Click 'S' Key) - Puts Turtle Onto Paper\nMouse Click (Left-Click With Your Mouse) - Turtle Goes To Clicked Coordinates\nMouse Drag (Hold Mouse On Turtle Using Left-Click And Move Your Mouse Around While Still Holding Down) - Turtle Moves With Your Mouse\nSpace Key (Click Space Key) - Draws A Dot Wherever The Turtle Is")
a=input('What do you want your paper color to be?')
b=int(input('How many steps do you want the turtle to move per button press?'))
c=int(input('How many degrees do you want your turtle to turn at the touch of arrow keys?'))
d=input('What speed would you like your turtle to go at?')
e=int(input('How thick do you want your lines to be?'))
f=int(input('How big do you want your dots to be?'))
bob.speed(d)
bob.width(e)
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
def cd(b,d,e):
  e.up()
  e.goto(b,d)
  e.down()
cd(-70,175,bob)
bob.write('Hello!',font=('Courier',30,'bold'))
def turtleforward():
  bob3.forward(b)
def turtleleft():
  bob3.left(c)
def turtleright():
  bob3.right(c)
def turtleup():
  bob3.up()
def turtledown():
  bob3.down()
def turtleback():
  bob3.backward(b)
def mouseclick(a,b):
  bobspaper.tracer(0)
  bob3.setheading(bob3.towards(a,b))
  bob3.goto(a,b)
  bobspaper.tracer(1)
def mousedrag(a,b):
  bobspaper.tracer(0)
  bob3.goto(a,b)
  bobspaper.tracer(1)
  print(int(bob3.xcor()),int(bob3.ycor()))
  if int(bob3.xcor())==1 and int(bob3.ycor())==1:
    c(-200,-25,bob)
    bob.write('You WIN😎',font=('Courier',57,'bold','italic'))
def dotting():
  bob3.dot(f)
'''def colorchange():
  g=input('What color do you want your turtle to be?')
  bob3.color(g)
def turtlewidthchange():
  h=input('How thick do you want your turtle to draw?')
  bob3.width(h)
def dotsizechange():
  i=input('What dot size do you want your turtle to use?')
  bob3.dot(i)'''
bobspaper.listen()
bobspaper.onkey(turtleforward,'up')
bobspaper.onkey(turtleleft,'left')
bobspaper.onkey(turtleright,'right')
bobspaper.onkey(turtleup,'w')
bobspaper.onkey(turtledown,'s')
bobspaper.onkey(turtleback,'down')
bobspaper.onkey(dotting,'space')
'''bobspaper.onkey(colorchange,'1')
bobspaper.onkey(turtlewidthchange,'2')
bobspaper.onkey(dotsizechange,'3')'''
bobspaper.onclick(mouseclick)
bob3.ondrag(mousedrag)