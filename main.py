
import turtle 

screen = turtle.Screen()
screen.setup(1200, 500)
screen.bgpic("hotellobby.png")
screen.addshape("touristmanRight.png")
screen.addshape("touristmanLeft.png")
screen.addshape("hotelman.png")
mySprite = turtle.Turtle()
mySprite.speed(0)
hotelman = turtle.Turtle()
hotelman.speed(0)
mySprite.hideturtle()
mySprite.penup()
hotelman.penup()
mySprite.left(90)
hotelman.left(90)
mySprite.shape("touristmanRight.png")
hotelman.shape("hotelman.png")
mySprite.setposition(0, -80)
hotelman.setposition(-20, -95)
mySprite.showturtle()
hotelman.showturtle()

# Create Player Controls
'''
def up():
  global mySprite
  mySprite.setposition(mySprite.xcor(), mySprite.ycor() + 10)
'''

'''
def down():
  global mySprite
  mySprite.setposition(mySprite.xcor(), mySprite.ycor() - 10)
'''

def left():
  global mySprite
  mySprite.setposition(mySprite.xcor() - 10, mySprite.ycor())
  mySprite.shape("touristmanLeft.png")
def right():
  global mySprite
  mySprite.setposition(mySprite.xcor() + 10, mySprite.ycor())
  mySprite.shape("touristmanRight.png")
# Set Event Listeners for Player Controls
# screen.onkey(up, "up")
# screen.onkey(down, "down")
screen.onkey(left, "left")
screen.onkey(right, "right")
screen.listen()
