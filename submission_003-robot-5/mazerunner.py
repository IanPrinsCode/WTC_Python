import robot
import import_helper
from sys import argv
if len(argv) > 1 and argv[1] == 'turtle':
    from world.turtle import world
else:
    from world.text import world
if len(argv) == 3:
    try:
        obs = import_helper.dynamic_import("maze.{}".format(argv[2]))
    except ModuleNotFoundError:
        import maze.obstacles as obs
else:
    import maze.obstacles as obs


def do_move_forward(robot_name):
    """
    Does forward movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    robot.handle_command(robot_name, 'forward 1')


def do_move_right(robot_name):
    """
    Does right movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    robot.handle_command(robot_name, 'right')
    robot.handle_command(robot_name, 'forward 1')


def do_move_back(robot_name):
    """
    Does backward movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    robot.handle_command(robot_name, 'right')
    robot.handle_command(robot_name, 'right')
    robot.handle_command(robot_name, 'forward 1')


def do_move_left(robot_name):
    """
    Does left movement in robot world.

    Parameters:
        robot_name (str): Robot's name used for prints.

    Returns:
        none
    """
    robot.handle_command(robot_name, 'left')
    robot.handle_command(robot_name, 'forward 1')


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
    Gets all open coordinates in the grid using the is_position_blocked from the maze file.

    Parameters:
        none

    Returns:
        open_coordinates (list): List of open coordinates.
    """
    all_coordinates = get_all_coordinates()

    open_coordinates = [x for x in all_coordinates if not obs.is_position_blocked(x[0], x[1])]

    return open_coordinates


def get_all_coordinates():
    """
    Finds all possible coordinates in the grid

    Parameters:
        none

    Returns:
        all_coordinates (list): All coordinates in grid.
    """
    all_coordinates = []

    for i in range(-100, 101, 1):
        for j in range(-200, 201, 1):
            all_coordinates.append((i, j))

    return all_coordinates


def map_coordinates_to_values(my_dict, open_coordinates):
    """
    Maps all open_coordinates to a value used to track the shortest path.

    Parameters:
        my_dict (dict): Empty dictionary.
        open_coordinates (list): All open coordinates.

    Returns:
        my_dict (dict): Dictionary with open_coordinates each mapped to the value 0.
    """
    for position in open_coordinates:
        my_dict.update({position : 0})

    return my_dict


def find_top_exit():
    """
    Finds an endpoint for the mazerun by scanning the top line of the grid.

    Parameters:
        none

    Returns:
        The coordinate of the exit. (if it finds an exit)
        none (if it does not find an exit)
    """
    for i in range(201):
        if not obs.is_position_blocked(-100 + i, 200):
            return (-100 + i, 200)
    return None


def find_left_exit():
    """
    Finds an endpoint for the mazerun by scanning the left line of the grid.

    Parameters:
        none

    Returns:
        The coordinate of the exit. (if it finds an exit)
        none (if it does not find an exit)
    """
    for j in range(401):
        if not obs.is_position_blocked(-100, -200 + j):
            return (-100, -200 + j)
    return None


def find_bottom_exit():
    """
    Finds an endpoint for the mazerun by scanning the bottom line of the grid.

    Parameters:
        none

    Returns:
        The coordinate of the exit. (if it finds an exit)
        none (if it does not find an exit)
    """
    for i in range(201):
        if not obs.is_position_blocked(-100 + i, -200):
            return (-100 + i, -200)
    return None

    
def find_right_exit():
    """
    Finds an endpoint for the mazerun by scanning the right line of the grid.

    Parameters:
        none

    Returns:
        The coordinate of the exit. (if it finds an exit)
        none (if it does not find an exit)
    """
    for j in range(401):
        if not obs.is_position_blocked(100, -200 + j):
            return (100, -200 + j)
    return None


def run_block_checker(my_dict, current, i):
    """
    For each coordinate mapped to value i in my_dict, this function changes the value of
    all neighbouring positions to i+1 if that position's value is still 0 and also not blocked
    by an obstacle.

    Parameters:
        my_dict (dict): Current dictionary of coordinates and values.
        current (tuple): The current coordinate being checked.
        i (int): The value associated with current.

    Returns:
        my_dict (dict): Dictionary with updated values on  each loop.
    """
    checked = i + 1

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if left_pos in my_dict.keys():
        if my_dict[left_pos] == 0:
            my_dict[left_pos] = checked

    if top_pos in my_dict.keys():
        if my_dict[top_pos] == 0:
            my_dict[top_pos] = checked

    if right_pos in my_dict.keys():
        if my_dict[right_pos] == 0:
            my_dict[right_pos] = checked

    if bottom_pos in my_dict.keys():
        if my_dict[bottom_pos] == 0:
            my_dict[bottom_pos] = checked

    return my_dict


def retrace_path(my_dict, current, start_point):
    """
    Retraces the shortest path, by starting at the endpoint and moving through coordinates while
    decrementing the values associated with the coordinates. On each step adding coordinates
    to path (list).

    Parameters:
        my_dict (dict): Dictionary containing all possible paths.
        current (tuple): The end_point of the shortest path is passed as current.
        start_point (tuple): The starting point of the pathfinder is passed as start_point.

    Returns:
        path (list): The end path in reverse.
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
    Main for doing mazerun.

    Parameters:
        robot_name (str): Robot's name, used for prints.
        arg (str): Sencond arg passed alongside 'mazerun' (direction to solve).

    Returns:
        none
    """
    my_dict = {}

    position_x = world.position_x
    position_y = world.position_y
    current = (position_x, position_y)
    i = 1

    print(' > ' + robot_name + ' starting maze run..')

    open_coordinates = get_open_coordinates()
    my_dict = map_coordinates_to_values(my_dict, open_coordinates)

    # interpreting different second args (which maze exit to use)
    if arg == 'left':
        end_point = find_left_exit()
    elif arg == 'right':
        end_point = find_right_exit()
    elif arg == 'bottom':
        end_point = find_bottom_exit()
    else:
        end_point = find_top_exit()
        arg = 'top'

    if end_point == None:
        return True, ' > ' + robot_name + ': There is no way out of the maze!'

    # set the start point to 1 in the grid of zeros
    my_dict.update({current : i})
    
    # main path-finding loop
    while my_dict[end_point] == 0:
        for key, value in my_dict.items():
            if value == i:
                my_dict = run_block_checker(my_dict, key, i)
        i += 1

    path = retrace_path(my_dict, end_point, current)
    # reverse path for use in do_movements
    path = path[::-1]

    do_movements(robot_name, path)

    return True, ' > ' + robot_name + ': I am at the ' + arg + ' edge.'