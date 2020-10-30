import random
from functools import reduce

global ob_list
ob_list = []


def sort_ob_list_into_rings(left, right, bottom, top):
    """
    Groups the maze rings, and removes an obstacle from each ring.
    """

    vertical_starting_point = 0
    vertical_ending_point = 72
    vertical_count_decrementer = 72

    horizontal_starting_point = 0
    horizontal_ending_point = 34
    horizontal_count_decrementer = 34

    ob_list = []
    for ring in range(9):
        ring_obs = []
        ring_obs = left[vertical_starting_point:vertical_ending_point]
        ring_obs = ring_obs + right[vertical_starting_point:vertical_ending_point]
        ring_obs = ring_obs + bottom[horizontal_starting_point:horizontal_ending_point]
        ring_obs = ring_obs + top[horizontal_starting_point:horizontal_ending_point]

        vertical_starting_point = vertical_starting_point + vertical_count_decrementer
        vertical_count_decrementer = vertical_count_decrementer -8
        vertical_ending_point = vertical_ending_point + vertical_count_decrementer

        horizontal_starting_point = horizontal_starting_point + horizontal_count_decrementer
        horizontal_count_decrementer = horizontal_count_decrementer -4
        horizontal_ending_point = horizontal_ending_point + horizontal_count_decrementer

        ring_obs.pop(random.randint(0,len(ring_obs) -1))

        ob_list.append(ring_obs)

    return list(reduce(lambda a, b: a+b, ob_list))


def get_obstacles():
    """
    Creates 9 rings worth of obstacles as a maze.
    """

    global ob_list

    top_hor = []
    condense = 85
    for y in range(180,5,-20):
        top_outer = [(x,y) for x in range(-condense,condense) if x%5 == 0]
        top_hor = top_hor + top_outer
        condense = condense -10

    bot_hor = []
    condense = 85
    for y in range(-185,-5,20):
        bot_outer = [(x,y) for x in range(-condense,condense) if x%5 == 0]
        bot_hor = bot_hor + bot_outer
        condense = condense -10

    lef_ver = []
    condense = 180
    for x in range(-90,-5,10):
        lef_outer = [(x,y) for y in range(-condense,condense) if y%5 == 0]
        lef_ver = lef_ver + lef_outer
        condense = condense -20

    rig_ver = []
    condense = 180
    for x in range(85,0,-10):
        rig_outer = [(x,y) for y in range(-condense,condense) if y%5 == 0]
        rig_ver = rig_ver +rig_outer
        condense = condense -20

    ob_list = sort_ob_list_into_rings(lef_ver, rig_ver, bot_hor, top_hor)
    return ob_list


def is_position_blocked(x,y):
    """
    Checks to see if the landing position of the robot is blocked.
    """

    global ob_list

    for i in ob_list:
        if x >= i[0] and x <= i[0] +4 and y >= i[1] and y <= i[1] +4:
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks to see if there is a obstacle
    in the way of the path travelled.
    The path travelled is from x1 to x2,
    and from y1 to y2.
    """

    if x1 > x2:
        return is_path_blocked(x2, y1, x1, y2)
    if y1 > y2:
        return is_path_blocked(x1, y2, x2, y1)

    x_count, y_count = x1, y1
    while x_count <= x2:
        if is_position_blocked(x_count, y1):
            return True
        x_count = x_count +1
    while y_count <= y2:
        if is_position_blocked(x1, y_count):
            return True
        y_count = y_count +1
    return False