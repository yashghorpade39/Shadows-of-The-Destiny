'''Purpose :- To read the input from the text file and 
move to the corresponding file which user selected'''

# importing libraries
import sys
import time
from turtle import *
from write_wrapped import *
from draw_button import *
import os
from emoji import *
import random  

# Initialize Turtle graphics
hideturtle()
pendown()

# Global variables
variable = {}
var_name = ""
option = {}
button_list = []
input_title = "And here it begins!!"
Screen = Screen()

# List which stores the background images
random_image = ["Background\Standindalone.gif","Background\jonas-jaeken-JGH0H5IyyM8-unsplash.gif","Background\Skeleton.gif","Background\susan-q-yin-xNLAq4U3GT8-unsplash.gif","Background\Hand.gif"]

# Initializing a varialbe to caputre what all images are used
used_image = []

# Function to call the next text file
def next_story(path):
    color("white")
    story_reader(path)

# Check if the click is within the bounds of the option button
def button_click(x, y):
    if -250 <= x <= -100 and -110 <= y <= -70:
        clear()
        next_story(option['a'])
    elif -70 <= x <= 80 and -110 <= y <= -70:
        clear()
        next_story(option['b'])
    elif 110 <= x <= 260 and -110 <= y <= -70:
        clear()
        next_story(option['q']) 
    elif -250 <= x <= -100 and -60 <= y <= -20:
        clear()
        next_story(option['q'])
    elif -70 <= x <= 80 and -60 <= y <= -20:
        clear()
        next_story(option['r'])

# Function to draw buttons based on a list of button labels
def buton_draw(b_x, b_y, button_list):
    for b in button_list:
        draw_button(b,b_x,b_y)
        b_x += 180

# Function to read the content of the files
def story_reader(file_path):
    abcd = random.shuffle(random_image) # Shuffle the image list
    for abcd in random_image:
        Screen.bgpic(abcd)
    pendown()
    setpos(-240,100) # Start writing from this position
    final_folder_path = os.path.abspath(".")
    story_folder_path = os.path.join(final_folder_path, "Story")
    text_file_path = os.path.join(story_folder_path, file_path)

    global var_name # Declaring global variable to store the username
    end_of_the_code = 0 

    # Opening the file to read the content
    with open(text_file_path,"r") as file:
        for line in file:
            if end_of_the_code == 1: # Checking if we have reached to the end of the text file
                option1, file_path = line.split(":")
                option[option1.lower()] = file_path.strip()
            else:
                if line.startswith("<"): # Capturing the Username of the Player
                    var_name, question = line[1:-2].split(":-")
                    user_input = textinput(input_title, question) # Capturing what user has entered
                    globals()[var_name] = user_input.lower()
                    variable[var_name] = user_input
                elif line.startswith("---"):   
                    end_of_the_code = 1      # Setting flag as 1 indicating the code will now check for changing the file
                elif line.startswith("{"):
                    next_story(line[1:-1])
                elif line.startswith("***"): # Checks if we are at the end of the story
                    sys.exit()
                elif line.startswith("("): 
                    button_list = line[1:-2].split(":")
                elif line.startswith("*"): # Checking for the line where the emoji has to be drawn
                    emoji = line[1:-2]
                    penup()
                    goto(-240,50)
                    pendown()
                    if emoji == "starry_eyes": # Validating the emoji text from the  text file
                        starryeyes() # Draws the emoji
                        time.sleep(3)
                    elif emoji == "dead_emoji":
                        dead()
                        time.sleep(3)
                elif line.startswith("["):  # Placing the username of the user into the running story
                    half_line = ""
                    placeholder = ""  
                    i = 0
                    for l in line:
                        if l != "]" and l != "[":
                            placeholder += l
                            i += 1
                        elif l == "]":
                            i += 1
                            break
                    for j in range(0, len(line)):
                        if j > i:
                            half_line += line[j]
                    final_message = f"{variable[placeholder]}{half_line}"
                    print(final_message)
                    clear()  
                    write(final_message)  
                    time.sleep(2)
                else:
                    print(line, end ="")   
                    clear()
                    write_wrapped(line,80)     
                    time.sleep(3)
    if len(button_list) == 3:
        buton_draw(-250,-110,button_list)
    elif len(button_list) == 2:
        b_x = -250
        b_y = -60
        buton_draw(-250,-60,button_list)
    
    # Capturing the click on the screen
    turtle.onscreenclick(button_click)
    turtle.mainloop()

    # Passing the path of the text file to be opened next
    next_story(option[variable[var_name].lower()])