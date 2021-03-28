from turtle import Turtle, Screen
import logging

logging.basicConfig(level = logging.DEBUG)

def init_turtle(coordinates):
    turtle, x_pos, y_pos = coordinates
    turtle.speed(500)

    turtle.penup()
    turtle.goto(x_pos, y_pos)

    turtle.shape('classic')
    turtle.shapesize(2)
    turtle.color('green4')
    turtle.pencolor('lawn green')
    turtle.pensize(2)
    turtle.pendown()

def draw_square(info):
    turtle, size, x_pos, y_pos = info

    init_turtle((turtle, x_pos, y_pos))
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()

def main():
    bubbles = Turtle()

    for y in range(350, -260, -120):
        for x in range(-350, 260, 120):
            draw_square((bubbles, 100, x, y))

    bubbles.hideturtle()

    screen = Screen()
    screen.title('Bubbles')
    screen.exitonclick()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
