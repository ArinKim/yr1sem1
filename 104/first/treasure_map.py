#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9908544
#    Student name: Arin Kim
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). 81023PT
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.
# You may not use any other modules for your solution.  

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    write('    Put your legend here', align = 'left',
          font=('Arial', 24, 'normal'))    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here

# Make the token's list

token = [0, 1, 2, 3, 4]

# Define constant values used in the coordination

TL_x, TL_y = 50, 600
TR_x, TR_y = 650, 600
CT_x, CT_y = 350, 300
BL_x, BL_y = 50, 0
BR_x, BR_y = 650, 0

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in ITD104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.


# Define function to draw cute face
def face(x_coord, y_coord, colour):
    penup()
    goto(x_coord, y_coord + 2)
    pendown()
    begin_fill()
    color(colour)
    circle(47)
    end_fill()
    penup()

# Define function to draw smile emoji
def smile_emoji(x_coord, y_coord):
    # Draw a cute gold face
    face(x_coord, y_coord, "gold")
    # Draw a winking eye
    goto(x_coord - 10, y_coord + 60)
    setheading(150)
    width(5)
    color("brown")
    pendown()
    circle(25, extent = 60)
    penup()
    # Draw another eye with black pupil
    goto(x_coord + 25, y_coord + 60)
    color("white")
    dot(25)
    goto(x_coord + 25, y_coord + 60)
    color("black")
    dot(18)
    # Draw a smile mouth with cute little teeth
    goto(x_coord - 25, y_coord + 32)
    begin_fill()
    setheading(300)
    width(3)
    color("brown")
    pendown()
    circle(30, extent = 125)
    goto(x_coord - 25, y_coord + 30)
    end_fill()
    goto(x_coord - 5, y_coord + 30)
    width(5)
    color("white")
    goto(x_coord + 8, y_coord + 30)
    # Change the direction of head and pen width for next drawing
    setheading(0)
    width(1)

# Define function to draw 'aww' emoji
def aww_emoji(x_coord, y_coord):
    # Draw a cute gold face
    face(x_coord, y_coord, "gold")
    # Draw the white part of eyes
    goto(x_coord - 15, y_coord + 70)
    pendown()
    width(25)
    color("white")
    goto(x_coord - 15, y_coord + 60)
    penup()
    goto(x_coord + 15, y_coord + 70)
    pendown()
    goto(x_coord + 15, y_coord + 60)
    penup()
    # Draw pupil of eyes
    goto(x_coord - 15, y_coord + 65)
    color("black")
    dot(10)
    goto(x_coord + 15, y_coord + 65)
    dot(10)
    # Draw a mouth
    penup()
    color("brown")
    goto(x_coord + 25, y_coord + 30)
    setheading(160)
    pendown()
    width(20)
    circle(70, extent = 40)
    # Change the direction of head and pen width for next drawing
    setheading(0)
    width(1)

# Define function to draw angry emoji
def angry_emoji(x_coord, y_coord):
    # Draw a angry red face
    face(x_coord, y_coord, "orange red")
    # Draw black eyes
    goto(x_coord - 17, y_coord + 55)
    pendown()
    color("black")
    dot(20)
    penup()
    goto(x_coord + 17, y_coord + 55)
    pendown()
    dot(20)
    # Draw angry eyebrows
    penup()
    goto(x_coord - 10, y_coord + 60)
    setheading(120)
    pendown()
    width(5)
    circle(30, extent = 40)
    penup()
    goto(x_coord + 10, y_coord + 60)
    setheading(60)
    pendown()
    width(5)
    circle(-30, extent = 40)
    # Draw angry mouth
    penup()
    goto(x_coord - 22, y_coord + 30)
    setheading(50)
    color("brown")
    pendown()
    width(7)
    circle(-30, extent = 100)
    # Change the direction of head and pen width for next drawing
    setheading(0)
    width(1)

# Define function to draw lovely emoji
def love_emoji(x_coord, y_coord):
    # Draw a cute gold face
    face(x_coord, y_coord, "gold")
    # Draw left part of heart eye
    goto(x_coord - 18, y_coord + 60)
    begin_fill()
    left(110)
    color("red")
    pendown()
    circle(8, extent = 220)
    setheading(325)
    forward(15)
    penup()
    goto(x_coord - 18, y_coord + 60)
    setheading(70)
    pendown()
    circle(-8, extent = 220)
    setheading(220)
    forward(14)
    end_fill()
    # Draw right part of heart eye
    penup()
    goto(x_coord + 18, y_coord + 60)
    setheading(0)
    pendown()
    begin_fill()
    left(110)
    color("red")
    pendown()
    circle(8, extent = 220)
    setheading(325)
    forward(15)
    penup()
    goto(x_coord + 18, y_coord + 60)
    setheading(70)
    pendown()
    circle(-8, extent = 220)
    setheading(220)
    forward(14)
    end_fill()
    # Draw a cute kissing mouth
    penup()
    goto(x_coord , y_coord + 30)
    setheading(0)
    color("brown")
    width(3)
    pendown()
    circle(5, extent = 220)
    penup()
    goto(x_coord, y_coord + 30)
    setheading(0)
    pendown()
    circle(-5, extent = 220)
    # Put some make up !
    penup()
    goto(x_coord - 25, y_coord + 30)
    color("light pink")
    pendown()
    dot(20)
    penup()
    goto(x_coord + 25, y_coord + 30)
    pendown()
    dot(20)
    # Change the direction of head and pen width for next drawing
    setheading(0)
    width(1)


# Define function to draw crying emoji
def crying_emoji(x_coord, y_coord):
    # Draw a cute gold face
    face(x_coord, y_coord, "gold")
    # Draw white part of big eyes
    penup()
    goto(x_coord - 15, y_coord + 70)
    pendown()
    width(25)
    color("white")
    goto(x_coord - 15, y_coord + 60)
    penup()
    goto(x_coord + 15, y_coord + 70)
    pendown()
    goto(x_coord + 15, y_coord + 60)
    penup()
    # Draw the pupil of eyes
    goto(x_coord - 15, y_coord + 65)
    color("black")
    dot(20)
    goto(x_coord + 15, y_coord + 65)
    dot(20)
    penup()
    # Draw teary eyes
    goto(x_coord - 10, y_coord + 70)
    color("white")
    dot(5)
    goto(x_coord + 10, y_coord + 70)
    color("white")
    dot(5)
    # Draw unhappy eyebrows
    penup()
    goto(x_coord - 10, y_coord + 90)
    setheading(220)
    width(3)
    color("brown")
    pendown()
    circle(-30, extent = 50)
    penup()
    goto(x_coord + 10, y_coord + 90)
    setheading(320)
    width(3)
    color("brown")
    pendown()
    circle(30, extent = 50)
    # Draw sad mouth
    penup()
    goto(x_coord - 22, y_coord + 30)
    setheading(50)
    color("brown")
    pendown()
    width(7)
    circle(-30, extent = 100)
    # Draw a tear
    penup()
    goto(x_coord - 25, y_coord + 55)
    begin_fill()
    color("light blue")
    width(2)
    setheading(300)
    pendown()
    forward(10)
    setheading(270)
    circle(-5, extent = 180)
    setheading(60)
    forward(10)
    end_fill()
    # Change the direction of head and pen width for next drawing
    setheading(0)
    width(1)


# Define the function to call emojis with token number

def call_emoji(x_coord, y_coord, tokens):
    # If the token number is 0, call the smile emoji
    if tokens == token[0]:
        smile_emoji(x_coord, y_coord)
    # If the token number is 1, call the aww emoji
    elif tokens == token[1]:
        aww_emoji(x_coord, y_coord)
    # If the token number is 2, call the angry emoji
    elif tokens == token[2]:
        angry_emoji(x_coord, y_coord)
    # If the token number is 3, call the lovely emoji
    elif tokens == token[3]:
        love_emoji(x_coord, y_coord)
    # If the token number is 4, call the crying emoji
    elif tokens == token[4]:
        crying_emoji(x_coord, y_coord)
    
# Follow the path as per the provided dataset
# Define the follow path for call emoji function

def follow_path(path_list):
    # Get each value of positions from random path
    for pos in path_list:
        # If the first item of list is 'start'
        if 'Start' in pos[0]:
            # if the second item of list is 'Top left'
            if 'Top left' in pos[1]:
                x_cor, y_cor = TL_x, TL_y
                
            # if the second item of list is 'Top right'
            elif 'Top right' in pos[1]:
                x_cor, y_cor = TR_x, TR_y
                
            # if the second item of list is 'Centre'
            elif 'Centre' in pos[1]:
                x_cor, y_cor = CT_x, CT_y
                
            # if the second item of list is 'Bottom left'
            elif 'Bottom left' in pos[1]:
                x_cor, y_cor = BL_x, BL_y
                
            # if the second item of list is 'Bottom right'
            else:
                x_cor, y_cor = BR_x, BR_y
                
        # if the first item of list is 'East'
        elif 'East' in pos[0]:
            x_cor += grid_size * pos[1] # How many times it should go
            
        # if the first item of list is 'West'
        elif 'West' in pos[0]:
            x_cor -= grid_size * pos[1]
            
        # if the first item of list is 'North'
        elif 'North' in pos[0]:
            y_cor += grid_size * pos[1]
            
        # if the first item of list is 'South'
        else:
            y_cor -= grid_size * pos[1]

        # Call the emoji function
        call_emoji(x_cor, y_cor, pos[2])

##def follow_path(path_list):
##    # Get each value of positions from random path
##    for pos in path_list:
##        # If the first item of list is 'start'
##        if 'Start' in pos[0]:
##            # if the second item of list is 'Top left'
##            if 'Top left' in pos[1]:
##                x_cor, y_cor = TL_x, TL_y
##                call_emoji(x_cor, y_cor, pos[2])
##
##            # if the second item of list is 'Top right'
##            elif 'Top right' in pos[1]:
##                x_cor, y_cor = TR_x, TR_y
##                call_emoji(x_cor, y_cor, pos[2])
##
##            # if the second item of list is 'Centre'
##            elif 'Centre' in pos[1]:
##                x_cor, y_cor = CT_x, CT_y
##                call_emoji(x_cor, y_cor, pos[2])
##
##            # if the second item of list is 'Bottom left'
##            elif 'Bottom left' in pos[1]:
##                x_cor, y_cor = BL_x, BL_y
##                call_emoji(x_cor, y_cor, pos[2])
##
##            # if the second item of list is 'Bottom right'
##            else:
##                x_cor, y_cor = BR_x, BR_y
##                call_emoji(x_cor, y_cor, pos[2])
##
##        # if the first item of list is 'East'
##        elif 'East' in pos[0]:
##            x_cor += grid_size * pos[1] # How many times it should go
##            call_emoji(x_cor, y_cor, pos[2])
##
##        # if the first item of list is 'West'
##        elif 'West' in pos[0]:
##            x_cor -= grid_size * pos[1]
##            call_emoji(x_cor, y_cor, pos[2])
##
##        # if the first item of list is 'North'
##        elif 'North' in pos[0]:
##            y_cor += grid_size * pos[1]
##            call_emoji(x_cor, y_cor, pos[2])
##
##        # if the first item of list is 'South'
##        else:
##            y_cor -= grid_size * pos[1]
##            call_emoji(x_cor, y_cor, pos[2])


# Define the function to draw legend

def legend():
    # Not to show drawing each times
    tracer(False)
    # Draw the legend box
    penup()
    goto(750, 650)
    width(2)
    begin_fill()
    color('Dodger blue', 'Turquoise')
    setheading(0)
    pendown()
    forward(340)
    setheading(270)
    forward(600)
    setheading(180)
    forward(340)
    setheading(90)
    forward(600)
    end_fill()
    penup()
    # Write the title
    color('black')
    goto(820, 620)
    write('Adorable Emojis', font =('Times',20,'bold'))
    # Write the name of each emoji
    goto(920, 550)
    write('Smile Emoji', font=('Arial', 18))
    setheading(270)
    forward(110)
    write('Aww Emoji', font=('Arial', 18))
    setheading(270)
    forward(110)
    write('Angry Emoji', font=('Arial', 18))
    setheading(270)
    forward(110)
    write('Love Emoji', font=('Arial', 18))
    setheading(270)
    forward(110)
    write('Crying Emoji', font=('Arial', 18))
    # Draw emojis
    setheading(0)
    smile_emoji(850, 520)
    aww_emoji(850, 410)
    angry_emoji(850, 300)
    love_emoji(850, 190)
    crying_emoji(850, 80)
    # Go back to home
    penup()
    home()
    # Show the cursor again
    tracer(True)



#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Put a description of your theme and tokens here")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.

# Call the legend function
legend()

# follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

