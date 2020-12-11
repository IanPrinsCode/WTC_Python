from robot import handle_command
from maze import obstacles
import os
import import_helper
from sys import argv
if len(argv) > 1 and argv[1] == 'turtle':
    from world.turtle import world
else:
    from world.text import world
if len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py"):
    obs = import_helper.dynamic_import("maze." + argv[2])
elif len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py") == False:
    print("Maze file not found")
    obs = import_helper.dynamic_import("maze.obstacles")
else:
    obs = import_helper.dynamic_import("maze.obstacles")

# if len(argv) == 3:
#     try:
#         obstacles = import_helper.dynamic_import("maze.{}".format(sys.argv[2]))
#     except ModuleNotFoundError:
#         import maze.obstacles as obstacles
# else:
#     import maze.obstacles as obstacles


def do_move_forward(robot_name):
    """
    Does forward movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    handle_command(robot_name, 'forward 1')


def do_move_right(robot_name):
    """
    Does right movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'forward 1')


def do_move_back(robot_name):
    """
    Does backward movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'forward 1')


def do_move_left(robot_name):
    """
    Does left movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    handle_command(robot_name, 'left')
    handle_command(robot_name, 'forward 1')


def do_movements(robot_name, path):
    """
    Initiates movements for the robot to run the maze after
    the path is already found.

    Parameters:
        robot_name (str): Robot's name used for prints.
        path (list): Contains coordinates of the path to exit the maze.

    Returns:
        none
    """
    directions = ['forward', 'right', 'back', 'left']
    position_x = world.position_x
    position_y = world.position_y
    current_direction_index = world.current_direction_index
    
    while len(path) > 1:
        
        left_pos = (position_x - 1, position_y)
        top_pos = (position_x, position_y + 1)
        right_pos = (position_x + 1, position_y)
        bottom_pos = (position_x, position_y - 1)

        if directions[current_direction_index] == 'forward':
            if path[1] == top_pos:
                do_move_forward(robot_name)
                current_direction_index = 0
            if path[1] == right_pos:
                do_move_right(robot_name)
                current_direction_index = 1
            if path[1] == bottom_pos:
                do_move_back(robot_name)
                current_direction_index = 2
            if path[1] == left_pos:
                do_move_left(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'left':
            if path[1] == top_pos:
                do_move_right(robot_name)
                current_direction_index = 0
            if path[1] == right_pos:
                do_move_back(robot_name)
                current_direction_index = 1
            if path[1] == bottom_pos:
                do_move_left(robot_name)
                current_direction_index = 2
            if path[1] == left_pos:
                do_move_forward(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'back':
            if path[1] == top_pos:
                do_move_back(robot_name)
                current_direction_index = 0
            if path[1] == right_pos:
                do_move_left(robot_name)
                current_direction_index = 1
            if path[1] == bottom_pos:
                do_move_forward(robot_name)
                current_direction_index = 2
            if path[1] == left_pos:
                do_move_right(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'right':
            if path[1] == top_pos:
                do_move_left(robot_name)
                current_direction_index = 0
            if path[1] == right_pos:
                do_move_forward(robot_name)
                current_direction_index = 1
            if path[1] == bottom_pos:
                do_move_right(robot_name)
                current_direction_index = 2
            if path[1] == left_pos:
                do_move_back(robot_name)
                current_direction_index = 3
        path.pop(0)
        position_x = path[0][0]
        position_y = path[0][1]


def get_open_coordinates():
    """
    Gets all open coordinates in the grid using the obstcles list from the maze file.

    Parameters:
        none

    Returns:
        open_coordinates (list): List of open coordinates.
    """
    obstacles = obs.get_obstacles()
    one_unit_obstacles = []

    all_coordinates = get_all_coordinates()
    print('wow jeezz boet')
    for x, y in obstacles:
        for i in range(0, 5):
            for j in range(0, 5):
                one_unit_obstacles.append((x + i, y + j))

    open_coordinates = [x for x in all_coordinates if x not in one_unit_obstacles]

    return open_coordinates


def get_all_coordinates():
    """
    docstring
    """
    all_coordinates = []

    for i in range(-100, 101, 1):
        for j in range(-200, 201, 1):
            all_coordinates.append((i, j))

    return all_coordinates


def map_coordinates_to_values(my_dict, open_coordinates):
    """
    docstring
    """
    for position in open_coordinates:
        my_dict.update({position : 0})

    return my_dict


def find_top_exit(open_coordinates):
    """
    docstring
    """
    for x, y in open_coordinates:
        if y == 200:
            end_point = (x, y)
            return end_point


def find_left_exit(open_coordinates):
    """
    docstring
    """
    for x, y in open_coordinates:
        if x == -100:
            end_point = (x, y)
            return end_point


def find_bottom_exit(open_coordinates):
    """
    docstring
    """
    for x, y in open_coordinates:
        if y == -200:
            end_point = (x, y)
            return end_point


def find_right_exit(open_coordinates):
    """
    docstring
    """
    for x, y in open_coordinates:
        if x == 100:
            end_point = (x, y)
            return end_point


def run_block_checker(my_dict, current, i):
    """
    docstring
    """
    checked = i + 1

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    # if left_pos in my_dict.keys() and obs.is_position_blocked(left_pos[0], left_pos[1]) == False:
    if left_pos in my_dict.keys():
        if my_dict[left_pos] == 0:
            my_dict[left_pos] = checked
            # my_dict.update({left_pos : checked})

    # if top_pos in my_dict.keys() and obs.is_position_blocked(top_pos[0], top_pos[1]) == False:
    if top_pos in my_dict.keys():
        if my_dict[top_pos] == 0:
            my_dict[top_pos] = checked
            # my_dict.update({top_pos : checked})

    # if right_pos in my_dict.keys() and obs.is_position_blocked(right_pos[0], right_pos[1]) == False:
    if right_pos in my_dict.keys():
        if my_dict[right_pos] == 0:
            my_dict[right_pos] = checked
            # my_dict.update({left_pos : checked})

    # if bottom_pos in my_dict.keys() and obs.is_position_blocked(bottom_pos[0], bottom_pos[1]) == False:
    if bottom_pos in my_dict.keys():
        if my_dict[bottom_pos] == 0:
            my_dict[bottom_pos] = checked
            # my_dict.update({bottom_pos : checked})

    return my_dict


def retrace_path(my_dict, current, start_point):
    """
    docstring
    """
    path = []
    last_val = my_dict[current]
    

    while current != start_point:

        left_pos = (current[0] - 1, current[1])
        top_pos = (current[0], current[1] + 1)
        right_pos = (current[0] + 1, current[1])
        bottom_pos = (current[0], current[1] - 1)

        if left_pos in my_dict.keys():
            if my_dict[left_pos] == last_val - 1:
                path.append(left_pos)
                last_val -= 1
                current = left_pos

        if top_pos in my_dict.keys():
            if my_dict[top_pos] == last_val - 1:
                path.append(top_pos)
                last_val -= 1
                current = top_pos

        if right_pos in my_dict.keys():
            if my_dict[right_pos] == last_val - 1:
                path.append(right_pos)
                last_val -= 1
                current = right_pos

        if bottom_pos in my_dict.keys():
            if my_dict[bottom_pos] == last_val - 1:
                path.append(bottom_pos)
                last_val -= 1
                current = bottom_pos

    return path


def do_mazerun(robot_name, arg):
    """
    docstring
    """
    my_dict = {}

    position_x = world.position_x
    position_y = world.position_y
    current = (position_x, position_y)
    i = 1

    print(' > ' + robot_name + ' starting maze run..')

    open_coordinates = get_open_coordinates()
    my_dict = map_coordinates_to_values(my_dict, open_coordinates)

    if arg == 'left':
        end_point = find_left_exit(open_coordinates)
    if arg == 'right':
        end_point = find_right_exit(open_coordinates)
    if arg == 'bottom':
        end_point = find_bottom_exit(open_coordinates)
    else:
        end_point = find_top_exit(open_coordinates)

    # 
    # remember to add accounting for if end_point is none
    #

    # set the start point to 1 in the grid of zeros
    my_dict.update({current : i})
    
    # main path-finding loop
    while my_dict[end_point] == 0:
        for key, value in my_dict.items():
            if value == i:
                my_dict = run_block_checker(my_dict, key, i)
        i += 1

    # find path out of all possible paths by decrementing from exit point
    path = retrace_path(my_dict, end_point, current)
    # inverse path for use in do_movements
    path = path[::-1]

    do_movements(robot_name, path)





    if __name__ == "__main__":
        one_unit_obstacles = []


        for i in range(0, 5):
            for j in range(0, 5):
                one_unit_obstacles.append((1 + i, 1 + j))

        print(len(one_unit_obstacles))