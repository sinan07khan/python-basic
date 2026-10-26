import math as m
import random as r
import time
import turtle as t

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

N = 500
stars = []
for _ in range(N):
	a = 2 * m.pi * r.random()
	base_x = 16 * m.sin(a) ** 3
	base_y = (
		13 * m.cos(a)
		- 5 * m.cos(2 * a)
		- 2 * m.cos(3 * a)
		- m.cos(4 * a)
	)
	tx = base_x * 18
	ty = base_y * 18
	sx = r.randint(-320, 320)
	sy = r.randint(-320, 320)
	size = r.uniform(2.5, 5.5)
	stars.append((sx, sy, tx, ty, size))

pen = t.Turtle()
pen.hideturtle()


def draw_star(x, y, size):
	pen.pencolor("#a855f7")
	pen.width(1.2)
	for angle in (0, 45, 90, 135):
		radians = m.radians(angle)
		dx = size * m.cos(radians)
		dy = size * m.sin(radians)
		pen.penup()
		pen.goto(x - dx, y - dy)
		pen.pendown()
		pen.goto(x + dx, y + dy)


steps = 50
for frame in range(steps + 1):
	pen.clear()
	progress = frame / steps
	eased = m.sin(progress * m.pi / 2)
	for sx, sy, tx, ty, size in stars:
		cx = sx + (tx - sx) * eased
		cy = sy + (ty - sy) * eased
		draw_star(cx, cy, size)
	screen.update()
	time.sleep(0.025)

t.done()