import turtle
p=turtle.Turtle()
p.up()
p.goto(0,0)
p.down()
for i in range(3):
  p.forward(150)
  p.left(120)
A=int(input('Guess the base length of this triangle:'))
B=int(input('Guess the height length of this triangle:'))
print("The triangle's area is {},".format((A*B)*0.5))
print("and the triangle's perimeter is {}.".format(A*3))