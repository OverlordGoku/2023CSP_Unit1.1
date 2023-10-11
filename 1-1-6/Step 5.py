#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
Spider.pensize(40)
Spider.circle(20)
Legs = 8
LengthOfLegs = 70
Spacing = 360 / Legs
Spider.pensize(5)
Number = 0
while (Number < Legs):
  Spider.goto(0, 20)
  Spider.setheading(Spacing * Number)
  Spider.forward(LengthOfLegs)
  Number = Number + 1
Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()