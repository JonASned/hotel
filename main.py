
# Import the Turtle 2D Graphics Module
import turtle 

# Create Game Window
screen = turtle.Screen()
screen.setup(1200, 500)
screen.bgpic("lobby2.png")
screen.addshape("touristman.png")
# Create Sprite
screen.addshape("touristman.png")
mySprite = turtle.Turtle()
mySprite.hideturtle() # hide turtle until the the duck image replaces the placeholder shape
mySprite.penup() # prevent sprite from drawing on screen as it moves
mySprite.left(90) # rotate sprite for proper placement on screen
mySprite.shape("touristman.png") # Set Image for Sprite
mySprite.setposition(0, -90)
mySprite.showturtle()

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
  
def right():
  global mySprite
  mySprite.setposition(mySprite.xcor() + 10, mySprite.ycor())
  
def fire():
  print("FIRE! (space bar pressed)")
  
# Set Event Listeners for Player Controls
# screen.onkey(up, "up")
# screen.onkey(down, "down")
screen.onkey(left, "left")
screen.onkey(right, "right")
screen.onkey(fire, "space")
screen.listen()
