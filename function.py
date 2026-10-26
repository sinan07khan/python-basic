def add(n1 , n2):
    return n1 + n2

n = 10
m = 5
result = add(n, m)
print(result)

print(add(10.5, 5.5))

import turtle 
turtle.speed(0)  # Set the drawing speed to the fastest
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

counter = 0
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1
turtle.exitonclick()


