'''Purpose :- To initiate the game'''

from turtle import *
from story_reader import *
import os
speed(0)   # Using it so that user doesn.t have to wait for the completion of the button, etc.

turtle.title("Shadows of the Destiny") # Displaying the title
penup()
pencolor("white")
goto(-250,100)

story_reader('Introduction.txt') # Start reading the input from the file provided  
done()
