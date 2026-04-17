import turtle
p=turtle.Turtle()
for i in range(2):
  p.forward(150)
  p.left(120)
  p.forward(150)
  p.left(60)
A=int(input('Guess the base length of this parallelogram:'))
print("The parallelogram's area is {},".format(A*A))
print("and the parallelogram's perimeter is {}.".format(A*4))