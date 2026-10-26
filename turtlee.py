#circle with turtle

import turtle
turtle.shape("turtle")
turtle.speed(2)

turtle.circle(100)
turtle.circle(75)
turtle.circle(50)
turtle.circle(25)

turtle.exitonclick()


#triangle with turtle

import turtle
turtle.shape("square")
turtle.speed(2)

turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)

turtle.exitonclick( )


#square with turtle

import turtle
turtle.shape("turtle")
turtle.speed(2)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick( )


#square with turtle using loop

import turtle

turtle.shape("turtle")

for i in range(4):
    turtle.forward(100)
    turtle.left(90)        

turtle.exitonclick()