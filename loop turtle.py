import turtle
turtle.shape("turtle")
turtle.speed(2)

for i in range(4):
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

turtle.exitonclick()

import turtle
turtle.shape("turtle")
turtle.speed(2)
for side_length in [50, 100, 150, 200, 250, 300, 350, 400]:
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
turtle.exitonclick()


import turtle
turtle.shape("turtle")
turtle.color("orange")
turtle.speed(5)

counter = 0
while counter < 36:
    turtle.forward(100)
    turtle.left(170)
    counter += 1

turtle.exitonclick()

import turtle

height = 5
width = 5

turtle.speed (2)
turtle.penup()

for y  in range (height):
    for x in range (width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()

        
