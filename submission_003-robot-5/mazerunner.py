import os
from os import curdir
from turtle import left, right
import import_helper
from sys import argv
from maze import pretty_normal_maze as obs
# if len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py"):
#     obs = import_helper.dynamic_import("maze." + argv[2])
# elif len(argv) > 2 and os.path.exists("maze/" + argv[2] + ".py") == False:
#     print("Maze file not found")
#     obs = import_helper.dynamic_import("maze.obstacles")
# else:
#     obs = import_helper.dynamic_import("maze.obstacles")


trace_back = []
blocked = []
trace_split_indexes = []

path_count = 0
is_tracing = False


def is_multi_path(current):
    """
    docstring
    """
    open_paths = 4

    if obs.is_position_blocked(current[0] - 1, current[1]) == True and (current[0] - 1, current[1]) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(current[0], current[1] + 1) == True and (current[0], current[1] + 1) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(current[0] + 1, current[1]) == True and (current[0] + 1, current[1]) not in trace_back:
        open_paths -= 1
    if obs.is_position_blocked(current[0], current[1] - 1) == True and (current[0], current[1] - 1) not in trace_back:
        open_paths -= 1

    if open_paths > 2:
        return True
    else:
        return False


def start_trace():
    """
    docstring
    """
    global is_tracing
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

    current = trace_back[trace_split_indexes[-1]]

    blocked += trace_back[trace_split_indexes[-1]:-1:]
    trace_back = trace_back[0:trace_split_indexes[-1]:]

    trace_split_indexes.pop()
    if len(trace_split_indexes) == 0:
        stop_trace()


def run_blocked_checker(current):
    """
    docstring
    """
    global blocked

    left_pos = (current[0] - 1, current[1])
    top_pos = (current[0], current[1] + 1)
    right_pos = (current[0] + 1, current[1])
    bottom_pos = (current[0], current[1] - 1)

    if obs.is_position_blocked(current[0] - 1, current[1]):
        blocked.append(left_pos)
    if obs.is_position_blocked(current[0], current[1] + 1):
        blocked.append(top_pos)
    if obs.is_position_blocked(current[0] + 1, current[1]):
        blocked.append(right_pos)
    if obs.is_position_blocked(current[0], current[1] - 1):
        blocked.append(bottom_pos)


def move_current(current):
    """
    docstring
    """
    global blocked, trace_back, path_count

    # if obs.is_position_blocked(current[0], current[1] + 1) == False and (current[0], current[1] + 1) not in trace_back:
    #     current = (current[0], current[1] + 1)
    # elif obs.is_position_blocked(current[0] - 1, current[1]) == False and (current[0] - 1, current[1]) not in trace_back:
    #     current = (current[0] - 1, current[1])
    # elif obs.is_position_blocked(current[0] + 1, current[1]) == False and (current[0] + 1, current[1]) not in trace_back:
    #     current = (current[0] + 1, current[1])
    # elif obs.is_position_blocked(current[0], current[1] - 1) == False and (current[0], current[1] - 1) not in trace_back:
    #     current = (current[0], current[1] - 1)
    if (current[0], (current[1] + 1)) not in blocked and (current[0], (current[1] + 1)) not in trace_back:
        current = (current[0], current[1] + 1)
    elif ((current[0] - 1), current[1]) not in blocked and ((current[0] - 1), current[1]) not in trace_back:
        current = (current[0] - 1, current[1])
    elif ((current[0] + 1), current[1]) not in blocked and ((current[0] + 1), current[1]) not in trace_back:
        current = (current[0] + 1, current[1])
    elif (current[0], (current[1] - 1)) not in blocked and (current[0], (current[1] - 1)) not in trace_back:
        current = (current[0], (current[1] - 1))
    else:
        retrace(current)
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


def do_mazerun():
    """
    docstring
    """
    global blocked
    current = [0, 0]
    obstacles = obs.get_obstacles()

    while is_in_range(current):
        run_blocked_checker(current)
        if is_multi_path(current):
            start_trace()
        current = move_current(current)

    print("Blocked: " + str(blocked))
    print()
    print("Path: " + str(trace_back))

do_mazerun()