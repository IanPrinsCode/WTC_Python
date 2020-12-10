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


def make_one_unit_obstacles(parameter_list):
    """
    docstring
    """
    pass


def get_open_coordinates():
    """
    docstring
    """
    obstacles = obs.get_obstacles()
    all_coordinates = []
    one_unit_obstacles = []

    for i in range(-100, 101, 1):
        for j in range(-200, 201, 1):
            all_coordinates.append((i, j))

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
            my_dict.update({left_pos : checked})

    # if top_pos in my_dict.keys() and obs.is_position_blocked(top_pos[0], top_pos[1]) == False:
    if top_pos in my_dict.keys():
        if my_dict[top_pos] == 0:
            my_dict.update({top_pos : checked})

    # if right_pos in my_dict.keys() and obs.is_position_blocked(right_pos[0], right_pos[1]) == False:
    if right_pos in my_dict.keys():
        if my_dict[right_pos] == 0:
            my_dict.update({left_pos : checked})

    # if bottom_pos in my_dict.keys() and obs.is_position_blocked(bottom_pos[0], bottom_pos[1]) == False:
    if bottom_pos in my_dict.keys():
        if my_dict[bottom_pos] == 0:
            my_dict.update({bottom_pos : checked})

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

        # print(last_val)



def do_mazerun(robot_name):
    """
    docstring
    """
    my_dict = {}

    position_x = world.position_x
    position_y = world.position_y
    current = (position_x, position_y)

    # all_coordinates = get_all_coordinates()
    open_coordinates = get_open_coordinates()
    my_dict = map_coordinates_to_values(my_dict, open_coordinates)
    end_point = find_top_exit(open_coordinates)
    i = 1

    my_dict.update({current : i})

    while my_dict[end_point] == 0:
    # while i < 10000:
        for key, value in my_dict.items():
            if value == i:
                my_dict = run_block_checker(my_dict, key, i)
        i += 1

    for key, value in my_dict.items():
        if value > 1:
            print((key, value))

    path = retrace_path(my_dict, end_point, current)

    print(path)


