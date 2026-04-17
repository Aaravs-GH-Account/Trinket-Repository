import turtle
p=turtle.Turtle()
paper=turtle.Screen()
p.shape('turtle')
p.width(10)
c=input('What color background do you want?')
paper.bgcolor(c)
if c=='black':
  p.color('white')
a=input('What shape do you want the turtle to draw out of these three shapes?:\n1.Circle\n2.Triangle\n3.Square')
if a=='Circle' or a=='circle':
  p.up()
  p.goto(0,-100)
  p.down()
  p.circle(100)
elif a=='Triangle' or a=='triangle':
  p.up()
  p.goto(-100,-100)
  p.down()
  for stuff in range(3):
    p.forward(200)
    p.left(120)
elif a=='Square' or a=='square':
  p.up()
  p.goto(-100,-100)
  p.down()
  for stuff in range(4):
    p.forward(200)
    p.left(90)
else:
  print('Do not choose any other shape than the provided ones!')