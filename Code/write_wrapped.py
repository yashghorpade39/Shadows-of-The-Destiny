'''Purpose :- To move to the next line so we don't go out of the screen'''

import turtle

def write_wrapped(text, line_length): # For printing the line so that it doesn't go out of the screen
    words = text.split()
    line = ''
    for word in words:
        if len(line) + len(word) + 1 > line_length:
            turtle.write(line, font=("Arial", 10, "normal"))
            line = word + ' '
            turtle.penup()
            turtle.sety(turtle.ycor() - 18)  # move the turtle down for the new line
            turtle.pendown()
        else:
            line += word + ' '
    turtle.write(line, font=("Arial", 10, "normal"))  # write the last line
    turtle.penup()
    turtle.goto(-250,100)
    turtle.pendown()