#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
Legs = 6
LengthOfLegs = 70
Spacing = 380 / Legs
Spider.pensize(5)
n = 0
while (Number < Legs):
  Spider.goto(0, 0)
  Spider.setheading(Spacing * Number)
  Spider.forward(LengthOfLegs)
  Number = Number + 1
Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()