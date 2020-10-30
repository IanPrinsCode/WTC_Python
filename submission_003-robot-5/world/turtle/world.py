import import_helper
from sys import argv
import turtle
import os
if len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py"):
    obs = import_helper.dynamic_import("maze." + argv[2])
elif len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py") == False:
    print("Maze file not found")
    obs = import_helper.dynamic_import("maze.obstacles")
else:
    obs = import_helper.dynamic_import("maze.obstacles")

# globals
character = object
screen = object
is_sprint = False
is_obstructed = False

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
move_commands = valid_commands[3:]

obstacles = []

def list_obstacles():
    """
    This funtion prints a list of object coordinates, that are saved in the obstacles, onto the console.
    """
    global obstacles

    obstacles.clear()
    obstacles = obs.get_obstacles()


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def show_position(robot_name):
    """
    Prints current position of robot.
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, is_obstructed
    is_obstructed = False
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obs.is_position_blocked(new_x, new_y) or obs.is_path_blocked(position_x, position_y, new_x, new_y):
        is_obstructed = True
        return False

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def initialize_objects():
    """
    Initializes the turtle graphics' objects.
    """
    global character
    global screen

    screen = turtle.Screen()
    character = turtle.Turtle()
    screen.setworldcoordinates(-250, -250, 250, 250)


def set_up_graphics():
    """
    Initializes the settings and colors for turtle graphics.
    """
    global character

    turtle.title("Toy Robot 4")
    turtle.bgcolor("white")
    character.turtlesize(3)
    character.color("black", "red")
    character.speed(1)
    character.home()
    character.setheading(90)


def draw_range_constraint():
    """
    Draws the range constraint on the turtle interface and then re-centres the cursor.
    """
    global character

    character.speed(0)
    character.pencolor("red")
    character.penup()
    character.goto(-100, -200)
    character.pendown()
    character.goto(-100, 200)
    character.goto(100, 200)
    character.goto(100, -200)
    character.goto(-100, -200)
    character.penup()
    character.goto(0, 0)


def draw_obstacles():
    """
    Draws all obstacles on the turtle graphics grid by using the coordinates from obstacles.
    """
    global character, obstacles

    character.pencolor("red")
    character.speed(0)
    turtle.tracer(n=0, delay=0) 
    for item in obstacles:
        character.fillcolor("red")
        character.penup()
        character.goto(item[0], item[1])
        character.begin_fill()
        character.pendown()
        character.goto(item[0], item[1] + 4)
        character.goto(item[0] + 4, item[1] + 4)
        character.goto(item[0] + 4, item[1])
        character.goto(item[0], item[1])
        character.end_fill()
    turtle.tracer(True)


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global character, is_sprint, is_obstructed

    if update_position(steps):
        if is_sprint == True:
            character.speed(9)
        else:
            character.speed(1)
        character.fd(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        if is_obstructed == True:
            return True, ''+robot_name+": "+'Sorry, there is an obstacle in the way.'
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'



def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global character, is_obstructed

    character.speed(1)
    if update_position(-steps):
        character.bk(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        if is_obstructed == True:
            return True, ''+robot_name+": "+'Sorry, there is an obstacle in the way.'
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index, character

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    character.rt(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index, character

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    character.lt(90)

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    global character
    global is_sprint

    is_sprint = True
    if steps == 1:
        try:
            return do_forward(robot_name, 1)
        finally:
            is_sprint = False
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def start_world(robot_name):
    """
    Initialize graphical world with objects and constraints as program starts.
    """
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    initialize_objects()
    set_up_graphics()
    draw_obstacles()
    draw_range_constraint()
    if len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py"):
        print(robot_name + ": Loaded " + argv[2] + ".")
    elif len(argv) == 1:
        print(robot_name + ": Loaded obstacles.")