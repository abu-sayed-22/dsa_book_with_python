import turtle

t=turtle.Turtle()
screen=t.getscreen()
file=open("data.txt", "r")

# Getting the file data
for line in file:
    values=line.strip().split(",")
    command=values[0]
#     Matching the command
    match command :
        case "goto":
            x=float(values[1])
            y=float(values[2])
            width=float(values[3])
            color=values[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        case "circle":
            radius = float(values[1])
            width = float(values[2])
            color=values[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        case "beginfill":
            color = values[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        case "endfill":
            t.end_fill()
        case "penup":
            t.penup()
        case "pendown":
            t.pendown()
t.ht()
screen.exitonclick()
file.close()