# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle ()


# add code here for a circle
painter.circle(10)

# move the turtle to another part of the screen
painter.penup()
painter.goto(x:44, y:50)
painter.pendown()
# add code here for an arc
painter.circle(radius20,extent 50)

# move the turtle to another part of the screen
painter.penup()
painter.goto(x:-20, y:-20)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.penup()
painter.goto(x:47, y:7)
painter.pendown()


# move the turtle to another part of the screen
painter.penup()
painter.goto(x:47, y:7)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(radius:150,extent 360, steps:9)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()