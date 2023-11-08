import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
flag = turtle.Turtle()
flag.speed(0)  # Set the drawing speed

# Set initial position
flag.penup()
flag.goto(-150, 50)
flag.pendown()

# Draw the red background
flag.color("red")
flag.begin_fill()
for _ in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(200)
    flag.right(90)
flag.end_fill()

# Draw the green pentagram
flag.penup()
flag.goto(0, 50)
flag.pendown()
flag.color("green")
flag.begin_fill()
for _ in range(5):
    flag.forward(90)
    flag.right(144)
flag.end_fill()

# Close the window on click
screen.exitonclick()

