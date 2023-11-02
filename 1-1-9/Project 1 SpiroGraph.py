import turtle as trtl

painter = trtl.Turtle()

painter.speed(100)

painter.penup()
x = -475
y = -372
painter.goto(x, y)


painter.pendown()

painter.color("green")

for numStars in range(25):
    for triangle in range(15):
        painter.pendown()
        painter.forward(50)
        painter.left(120)
        painter.left(45)
        painter.penup()
    x += 57
    y += 45
    painter.left(50)
    painter.goto(x, y)

    rem = numStars % 2
    if(rem==0):
        painter.color("blue")
    else:
        painter.color("green")
        rem+=1
wn = trtl.Screen()
wn.mainloop()
