#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  turtle.penup()
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  turtle.pendown()
#Starting position
startx = 0
starty = 0

#Commands for turtle to turn right and forward
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)
  t.forward(50)

#Adding 50 to the starting position
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()