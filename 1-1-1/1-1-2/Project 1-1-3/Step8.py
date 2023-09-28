#   a113_circle_of_circles.py
#   Modify this code to draw a circle of circles
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
for line in range(12):
    painter.stamp()
    painter.forward(100)
    painter.left(45)
wn = trtl.Screen()
wn.mainloop()