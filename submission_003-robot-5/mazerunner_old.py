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

# variables tracking position and direction
# position_x = 0
# position_y = 0
# directions = ['forward', 'right', 'back', 'left']
# current_direction_index = 0

trace_back = []
blocked = []
trace_split_indexes = []
is_tracing = False


def is_multi_path(current):
    """
    docstring
    """
    open_paths = 4

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if obs.is_position_blocked(left_pos[0], left_pos[1]) == True and (left_pos) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(top_pos[0], top_pos[1]) == True and (top_pos) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(right_pos[0], right_pos[1]) == True and (right_pos) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(bottom_pos[0], bottom_pos[1]) == True and (bottom_pos) not in trace_back:
        open_paths -= 1

    if open_paths > 1:
        return True
    else:
        return False


def start_trace():
    """
    docstring
    """
    global is_tracing, trace_split_indexes, trace_back

    trace_split_indexes.append(len(trace_back) - 1)
    is_tracing = True


def stop_trace():
    """
    docstring
    """
    global is_tracing
    is_tracing = False


def retrace(current):
    """
    docstring
    """
    global trace_back, is_tracing, blocked, trace_split_indexes

    # if len(trace_split_indexes) != 0:
    current = trace_back[trace_split_indexes[-1]]

    blocked += trace_back[trace_split_indexes[-1]:-1:]
    trace_back = trace_back[0:trace_split_indexes[-1]:]

    trace_split_indexes.pop()
    if len(trace_split_indexes) == 0:
        stop_trace()
    return current


def run_blocked_checker(current):
    """
    docstring
    """
    global blocked

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if obs.is_position_blocked(left_pos[0], left_pos[1]):
        blocked.append(left_pos)
    if obs.is_position_blocked(top_pos[0], top_pos[1]):
        blocked.append(top_pos)
    if obs.is_position_blocked(right_pos[0], right_pos[1]):
        blocked.append(right_pos)
    if obs.is_position_blocked(bottom_pos[0], bottom_pos[1]):
        blocked.append(bottom_pos)


def move_current(current):
    """
    docstring
    """
    global blocked, trace_back

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if (top_pos) not in blocked and (top_pos) not in trace_back:
        current = (top_pos)
    elif (left_pos) not in blocked and (left_pos) not in trace_back:
        current = (left_pos)
    elif (right_pos) not in blocked and (right_pos) not in trace_back:
        current = (right_pos)
    elif (bottom_pos) not in blocked and (bottom_pos) not in trace_back:
        current = (bottom_pos)
    else:
        current = retrace(current)
        return current
    trace_back.append(current)
    return current


def is_in_range(current):
    """
    docstring
    """
    if current[0] == -100 or current[0] == 100:
        return False
    elif current[1] == -200 or current[1] == 200:
        return False
    else:
        return True


def do_move_forward(robot_name):
    """
    docstring
    """
    handle_command(robot_name, 'forward 1')


def do_move_right(robot_name):
    """
    docstring
    """
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'forward 1')


def do_move_back(robot_name):
    """
    docstring
    """
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'right')
    handle_command(robot_name, 'forward 1')


def do_move_left(robot_name):
    """
    docstring
    """
    handle_command(robot_name, 'left')
    handle_command(robot_name, 'forward 1')


def do_movements(robot_name, position_x, position_y, current_direction_index):
    """
    docstring
    """
    global trace_back
    directions = ['forward', 'right', 'back', 'left']
    

    while len(trace_back) > 1:
        
        left_pos = (position_x - 1, position_y)
        top_pos = (position_x, position_y + 1)
        right_pos = (position_x + 1, position_y)
        bottom_pos = (position_x, position_y - 1)

        if directions[current_direction_index] == 'forward':
            if trace_back[1] == top_pos:
                do_move_forward(robot_name)
                current_direction_index = 0
            if trace_back[1] == right_pos:
                do_move_right(robot_name)
                current_direction_index = 1
            if trace_back[1] == bottom_pos:
                do_move_back(robot_name)
                current_direction_index = 2
            if trace_back[1] == left_pos:
                do_move_left(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'left':
            if trace_back[1] == top_pos:
                do_move_right(robot_name)
                current_direction_index = 0
            if trace_back[1] == right_pos:
                do_move_back(robot_name)
                current_direction_index = 1
            if trace_back[1] == bottom_pos:
                do_move_left(robot_name)
                current_direction_index = 2
            if trace_back[1] == left_pos:
                do_move_forward(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'back':
            if trace_back[1] == top_pos:
                do_move_back(robot_name)
                current_direction_index = 0
            if trace_back[1] == right_pos:
                do_move_left(robot_name)
                current_direction_index = 1
            if trace_back[1] == bottom_pos:
                do_move_forward(robot_name)
                current_direction_index = 2
            if trace_back[1] == left_pos:
                do_move_right(robot_name)
                current_direction_index = 3

        elif directions[current_direction_index] == 'right':
            if trace_back[1] == top_pos:
                do_move_left(robot_name)
                current_direction_index = 0
            if trace_back[1] == right_pos:
                do_move_forward(robot_name)
                current_direction_index = 1
            if trace_back[1] == bottom_pos:
                do_move_right(robot_name)
                current_direction_index = 2
            if trace_back[1] == left_pos:
                do_move_back(robot_name)
                current_direction_index = 3
        trace_back.pop(0)
        position_x = trace_back[0][0]
        position_y = trace_back[0][1]


def do_mazerun(robot_name):
    """
    docstring
    """
    # global position_x, position_y, directions, current_direction_index
    global trace_back, trace_split_indexes, blocked

    position_x = world.position_x
    position_y = world.position_y
    current_direction_index = world.current_direction_index

    trace_back = []
    trace_split_indexes = []
    blocked = []
    current = [position_x, position_y]

    while is_in_range(current):
        run_blocked_checker(current)
        if is_multi_path(current):
            start_trace()
        current = move_current(current)

    do_movements(robot_name, position_x, position_y, current_direction_index)
    # for point in trace_back:

    # print("Blocked: " + str(blocked))
    # print()
    # print("Path: " + str(trace_back))

# do_mazerun()