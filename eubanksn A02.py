######################################################################
# # Author: Noah Eubanks
# Username: eubanksn
#
# Assignment: A02: Loopy Turtles
# Purpose: To demonstrate the turtle library and loops
######################################################################
#
#
import turtle

wn = turtle.Screen()
wn.bgcolor("white")


def main():
    box = turtle.Turtle
    f = turtle.Turtle


def square(box):
    """This function draws the Mickey boxy. """

    for i in range(2):
        box.pencolor("red")
        box.forward(40)
        box.right(90)
        box.forward(40)
        box.right(90)


def fries(f):
    """draws a single fry."""
    # posistion fry

    f.penup()
    f.forward(5)
    f.right(90)
    f.forward(25)
    f.left(90)
    f.pendown()
    f.pencolor("yellow")
    f.forward(20)
    wn.exitonclick()


main()
