import turtle
p=turtle.Turtle()
p.up()
p.goto(0,0)
p.down()
for i in range(4):
  p.forward(150)
  p.left(90)
UserIn=int(input('Guess what the base length of this square is in inches:'))
print('The area of this square is {} inches squared,'.format(UserIn**2))
print('and the perimeter of this square is {} inches.'.format(UserIn*4))