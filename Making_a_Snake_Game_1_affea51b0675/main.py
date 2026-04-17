import turtle, random as r, time as t, sys
food=turtle.Turtle()
snake=turtle.Turtle()
writer=turtle.Turtle()
writer2=turtle.Turtle()
writer2.hideturtle()
writer.hideturtle()
snake.speed(1.8)
writer.speed(10000)
screen=turtle.Screen()
food.shape('circle')
snake.shape('square')
screen.bgcolor('royalblue')
food.color('darkred')
#a=input('What color do you want your snake to be? Here is a link. Choose only from the link: https://i.sstatic.net/nCk6u.jpg')
snake.color('green')
food.up()
food.goto(r.randint(-160,160), r.randint(-160,120))
snake.up()
#gaming variables
score=1
snake.direction='stop'
def snakeup():
  snake.direction='up'
def snakedown():
  snake.direction='down'
def snakeright():
  snake.direction='right'
def snakeleft():
  snake.direction='left'
def snakemove():
  if snake.direction=='up':
    startingycoordinate=snake.ycor()
    snake.sety(startingycoordinate+10)
  if snake.direction=='down':
    startingycoordinate=snake.ycor()
    snake.sety(startingycoordinate-10)
  if snake.direction=='left':
    startingxcoordinate=snake.xcor()
    snake.setx(startingxcoordinate-10)
  if snake.direction=='right':
    startingxcoordinate=snake.xcor()
    snake.setx(startingxcoordinate+10)
screen.listen()
screen.onkey(snakeup,'Up')
screen.onkey(snakedown,'Down')
screen.onkey(snakeright,'Right')
screen.onkey(snakeleft,'Left')
writer.up()
writer.color('red')
writer.width(10)
writer.goto(-180,-180)
writer.down()
writer.forward(360)
writer.left(90)
writer.forward(320)
writer.left(90)
writer.forward(360)
writer.left(90)
writer.forward(320)
writer.left(90)
writer.width(1)
writer.color('black')
writer.up()
writer.goto(-80,190)
writer.down()
for i in range(2):
  writer.forward(160)
  writer.right(90)
  writer.forward(40)
  writer.right(90)
writer.right(90)
writer.forward(30)
writer.write('Score:'+str(score),font=('courier',20))
tl=[]
while True:
  screen.update()
  #Game OVER!
  if snake.xcor()<-180 or snake.xcor()>180 or snake.ycor()<-180 or snake.ycor()>140:
    writer2.up()
    writer2.goto(-175,0)
    snake.hideturtle()
    food.hideturtle()
    #tl.hideturtle()
    writer2.write('Game OVER!🙁',font=('courier',35))
    break
  snakemove()
  if snake.distance(food)<20:
    t.sleep(0.1)
    food.goto(r.randint(-160,160), r.randint(-160,120))
    score=score+1
    if score==2:
      writer2.up()
      writer2.goto(-175,0)
      writer2.write('You WIN!😀',font=('courier',35))
      t.sleep(20)
      exit()
    writer.clear()
    writer.left(90)
    writer.up()
    writer.goto(-80,190)
    writer.down()
    newturtle=turtle.Turtle()
    newturtle.color('green')
    newturtle.shape('square')
    newturtle.up()
    tl.append(newturtle)
    writer.up()
    writer.color('red')
    writer.width(10)
    writer.goto(-180,-180)
    writer.down()
    writer.forward(360)
    writer.left(90)
    writer.forward(320)
    writer.left(90)
    writer.forward(360)
    writer.left(90)
    writer.forward(320)
    writer.left(90)
    writer.width(1)
    writer.color('black')
    writer.up()
    writer.goto(-80,190)
    writer.down()
    for i in range(2):
      writer.forward(160)
      writer.right(90)
      writer.forward(40)
      writer.right(90)
    writer.right(90)
    writer.forward(30)
    writer.write('Score:'+str(score),font=('courier',20))
  for i in range(len(tl)-1,0,-1):
    xcon=tl[i-1].xcor()
    ycon=tl[i-1].ycor()
    tl[i].goto(xcon,ycon)
  if len(tl)>0:
    sxc2=snake.xcor()
    syc2=snake.ycor()
    tl[0].up()
    tl[0].goto(sxc2,syc2)