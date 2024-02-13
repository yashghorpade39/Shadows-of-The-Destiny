'''Purpose :- To Draw the button shape'''


from turtle import *

def draw_rectangle(): # Drawing rectangle for the button
    for _ in range(4):
        if _% 2 == 0:
            forward(150)
            left(90)
        else:
            forward(40)
            left(90) 