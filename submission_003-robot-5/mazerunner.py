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


def get_open_coordinates():
    """
    docstring
    """
    obstacles = obs.get_obstacles()
    all_coordinates = []

    for i in range(-100, 101):
        for j in range(-200, 201):
            all_coordinates.append((i, j))

    open_coordinates = [x for x in all_coordinates if x not in obstacles]

    return open_coordinates


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
    # checked = i + 1

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if obs.is_position_blocked(left_pos[0], left_pos[1]) == False:
        if my_dict[left_pos] == 0:
            # my_dict[left_pos] = checked
            my_dict.update({(left_pos) : i + 1})
    if obs.is_position_blocked(top_pos[0], top_pos[1]) == False:
        if my_dict[top_pos] == 0:
            # my_dict[top_pos] = checked
            my_dict.update({(top_pos) : i + 1})
    if obs.is_position_blocked(right_pos[0], right_pos[1]) == False:
        if my_dict[right_pos] == 0:
            # my_dict[right_pos] = checked
            my_dict.update({(left_pos) : i + 1})
    if obs.is_position_blocked(bottom_pos[0], bottom_pos[1]) == False:
        if my_dict[bottom_pos] == 0:
            # my_dict[bottom_pos] = checked
            my_dict.update({(bottom_pos) : i + 1})

    print(i)
    print(my_dict[bottom_pos])
    
    return my_dict


def do_mazerun(robot_name):
    """
    docstring
    """
    my_dict = {}

    position_x = world.position_x
    position_y = world.position_y
    current = (position_x, position_y)

    open_coordinates = get_open_coordinates()
    my_dict = map_coordinates_to_values(my_dict, open_coordinates)
    end_point = find_top_exit(open_coordinates)
    i = 1

    my_dict.update({(current) : i})

    # while my_dict[end_point] == 0:
    while i < 300:
        for value, key in my_dict.items():
            if key == i:
                my_dict = run_block_checker(my_dict, value, i)
            i += 1

    # for key, value in my_dict.items():
    #     if value > 6:
    #         print((key, value))
    





# def run_blocked_checker(current):
#     """
#     docstring
#     """
#     global blocked

#     left_pos = (current[0] - 1, current[1])
#     top_pos = (current[0], current[1] + 1)
#     right_pos = (current[0] + 1, current[1])
#     bottom_pos = (current[0], current[1] - 1)

#     if obs.is_position_blocked(left_pos[0], left_pos[1]):
#         blocked.append(left_pos)
#     if obs.is_position_blocked(top_pos[0], top_pos[1]):
#         blocked.append(top_pos)
#     if obs.is_position_blocked(right_pos[0], right_pos[1]):
#         blocked.append(right_pos)
#     if obs.is_position_blocked(bottom_pos[0], bottom_pos[1]):
#         blocked.append(bottom_pos)


# def move_current(current):
#     """
#     docstring
#     """
#     global blocked, trace_back

#     left_pos = (current[0] - 1, current[1])
#     top_pos = (current[0], current[1] + 1)
#     right_pos = (current[0] + 1, current[1])
#     bottom_pos = (current[0], current[1] - 1)

#     if (top_pos) not in blocked and (top_pos) not in trace_back:
#         current = (top_pos)
#     elif (left_pos) not in blocked and (left_pos) not in trace_back:
#         current = (left_pos)
#     elif (right_pos) not in blocked and (right_pos) not in trace_back:
#         current = (right_pos)
#     elif (bottom_pos) not in blocked and (bottom_pos) not in trace_back:
#         current = (bottom_pos)
#     # return current
#     # trace_back.append(current)
#     # return current