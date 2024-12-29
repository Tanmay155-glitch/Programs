import turtle

# Create turtle object
t = turtle.Turtle()

# Set background color
turtle.bgcolor("white")

# Set pen size and color
t.pensize(3)
t.color("red")

# Start drawing the heart
t.begin_fill()
t.fillcolor("red")

# Move turtle to start position
t.left(50)
t.forward(133)

# Draw the left curve of the heart
t.circle(50, 200)

# Draw the right curve of the heart
t.right(140)
t.circle(50, 200)

# Complete the heart shape
t.forward(133)

t.end_fill()

# Hide turtle
t.hideturtle()

# Keep the window open
turtle.done()
