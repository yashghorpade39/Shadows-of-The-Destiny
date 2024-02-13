'''Purpose :- To Draw the button with content'''


from turtle import *
from write_wrapped import *
from draw_rectangle import *

def draw_button(text, x, y): # Making the option button and filling the text in it
    penup()
    goto(x,y) # Going to the index from where to start drawing the button
    pendown()
    color("white")
    begin_fill()
    draw_rectangle() # Using the fucntion created earlier in draw_rectangle.py to draw button
    end_fill()
    penup()
    color("black")
    goto(x+5, y+20)
    write_wrapped(text,25)
    pendown()