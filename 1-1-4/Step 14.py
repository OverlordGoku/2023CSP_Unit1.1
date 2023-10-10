painter =
ycor =
while painter.ycor () < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    painter.speed(0)
    space = space + 1
