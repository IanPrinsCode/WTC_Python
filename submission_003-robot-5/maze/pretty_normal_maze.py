import turtle
import functools
from random import randint

obstacles = []

def gen_horisontal(start_x, end_x, y_value):
    """
    docstring
    """
    global obstacles

    for i in range(11):
        door = randint(start_x, end_x)
        for x in range(start_x, end_x, 4):
            if door in range(x - 4, x) and i % 2 != 0:
                continue
            obstacles.append((x, y_value))
        y_value += 40
        if i < 5:
            start_x += 20
            end_x -= 20
        else:
            start_x -= 20
            end_x += 20


def gen_vertical(start_y, end_y, x_value):
    """
    docstring
    """
    global obstacles

    for i in range(11):
        door = randint(start_y, end_y)
        for y in range(start_y, end_y, 4):
            if i == 5:
                continue
            if door in range(y - 4, y) and i % 2 == 0:
                continue
            obstacles.append((x_value, y))
        x_value += 20
        if i < 5:
            start_y += 40
            end_y -= 40
        else:
            start_y -= 40
            end_y += 40


def create_random_obstacles():
    """
    Generates list of obstacle coordinates that will draw out the maze constraint in turtle graphics.
    """
    global obstacles
    start_x = -100
    end_x = 100
    start_y = -200
    end_y = 201
    obstacles.clear()

    gen_horisontal(start_x, end_x, start_y)
    gen_vertical(start_y, end_y, start_x)

    print()
    print("obstacle_list" + str(obstacles))
    print()
    return obstacles


def get_obstacles():
    """
    Returns the list of generated and saved obstacle coordinates.
    """
    global obstacles

    if len(obstacles) == 0:
        obstacles = create_random_obstacles()
    return obstacles


def is_position_blocked(x, y):
    """
    Tests if the robot will land on an obstacle for a certain movement.  Returns True if it will and False otherwise.
    """
    global obstacles

    for item in obstacles:
        if x >= item[0] and x <= (item[0] + 4) and y >= item[1] and y <= (item[1] + 4):
            return True 
        else:
            return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Tests if the robot will move over an obstacle for a certain movement.  Returns True if it will and False otherwise.
    """
    global obstacles

    max_x = max([x1, x2])
    min_x = min([x1, x2])
    for item in obstacles:
        x_axis = False
        y_axis = False
        if y1 == y2:
            for i in range(item[1], item[1] + 5):
                if i == y1:
                    x_axis = True
            for i in range(min_x, max_x + 1):
                if i >= item[0] and i <= item[0] + 4:
                    y_axis = True
        if x_axis == True and y_axis == True:
            return True

    max_y = max([y1, y2])
    min_y = min([y1, y2])
    for item in obstacles:
        x_axis = False
        y_axis = False
        if x1 == x2:
            for i in range(item[0], item[0] + 5):
                if i == x1:
                    x_axis = True
            for i in range(min_y, max_y + 1):
                if i >= item[1] and i <= item[1] + 4:
                    y_axis = True
        if x_axis == True and y_axis == True:
            return True

    return False
