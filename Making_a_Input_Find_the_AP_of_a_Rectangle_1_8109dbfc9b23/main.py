import turtle
p=turtle.Turtle()
for i in range(2):
  p.forward(150)
  p.left(90)
  p.forward(75)
  p.left(90)
A=int(input('Guess the base length of this rectangle:'))
B=int(input('Guess the height length of this rectangle:'))
print("The rectangle's area is {},".format(A*B))
print("and the rectangle's perimeter is {}.".format(A*2+(B*2)))