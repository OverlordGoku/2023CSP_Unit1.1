#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
Spider.pensize(40)
Spider.circle(20)
Legs = 8
LengthOfLegs = 70
Spacing = 360 / Legs-20
Spider.pensize(5)
Number = 0
while (Number < Legs):
  Spider.goto(0, 20)



  if(Number < 4):
    Spider.setheading(Spacing * Number-45)
    Spider.forward(LengthOfLegs)

  else:
    Spider.setheading(Spacing * Number+45)
    Spider.forward(LengthOfLegs)
  Number = Number + 1

for loop in range(2):
  Spider.penup()
  Spider.goto( 6, 27)
Spider.pendown()
Spider.color("Red")
Spider.pensize(10)
Spider.circle(5)
Spider.penup()
Spider.goto( -20, 27)
Spider.pendown()
Spider.circle(5)
Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()