'''Purpose :- To Draw the Emoji which will pe used upon completing and quiting the story'''

from turtle import *
from star import *

def move_next():
    penup()
    forward(10)
    pendown()

def starryeyes():
    #yellow face
    begin_fill()
    color("black","gold")
    circle(12.5)
    end_fill()
    #moving to the eye position
    penup()
    back(10)
    left(90)
    forward(17.5)
    right(90)
    pendown()
    #eyes
    begin_fill()
    color("sky blue","steel blue")
    star()
    move_next()
    star()
    end_fill()
    #move position for smile
    penup()
    right(90)
    forward(7.5)
    right(90)
    pendown()
    color("black")
    forward(7.5)
    right(180)
    #smile
    begin_fill()
    color("black","white smoke")
    right(90)
    circle(7.5,180)
    left(90)
    forward(15)
    end_fill()
    #teeth
    left(105)
    forward(7.5)
    left(75)
    forward(15)
    penup()
    color("white")
#end of starryeyes function


def dead():
    #yellow face
    fillcolor("gold")
    begin_fill()
    circle(12.5)
    end_fill()

    penup()
    left(90)
    forward(10)
    right(90)
    forward(5)
    pendown()
    color("black")
    write("X", font = ('ARIAL', 5,'')) # Draws the first eye

    penup()
    left(180)
    forward(12.5)
    pendown()
    color("black")
    write("X", font = ('ARIAL', 5,'')) # Draws the other eye

    penup()
    left(90)
    forward(5)
    left(90)
    pendown()
    forward(15)
    color("white")
    penup()