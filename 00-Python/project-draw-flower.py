import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw center of sunflower
pen.penup()
pen.goto(0, -50)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.circle(60)
pen.end_fill()

# Draw petals
pen.penup()
pen.goto(0, 0)
pen.setheading(0)
pen.color("yellow")

for i in range(36):
    pen.penup()
    pen.forward(60)
    pen.pendown()
    pen.begin_fill()
    pen.circle(40, 60)
    pen.left(120)
    pen.circle(40, 60)
    pen.end_fill()
    pen.penup()
    pen.goto(0, 0)
    pen.right(10)

# Draw stem
pen.goto(0, -110)
pen.setheading(-90)
pen.color("green")
pen.pensize(8)
pen.pendown()
pen.forward(200)

# Draw leaf
pen.penup()
pen.goto(0, -180)
pen.setheading(45)
pen.color("green")
pen.begin_fill()
pen.pendown()
pen.circle(60, 90)
pen.left(90)
pen.circle(60, 90)
pen.end_fill()

turtle.done()
