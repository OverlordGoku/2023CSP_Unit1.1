#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate

    # set placement and color of turtle
for floor in range(num_floors):
    painter.penup()
    painter.goto(x, y)
    painter.color("blue")

    y = y + 5  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()