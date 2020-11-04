import random

# globals
obstacles = []

def create_random_obstacles():
    """
    Generates random coordinate tuples and appends them into the empty obstacles list.
    """
    global obstacles
    obstacles.clear()

    obstacles = [(random.randint(-100, 100), random.randint(-200, 200)) for i in range(random.randint(0, 10))]

    return obstacles


def is_position_blocked(x, y):
    """
    Tests if the robot will land on an obstacle for a certain movement.  Returns True if it will and False otherwise.
    """
    global obstacles

    

    for item in obstacles:
        if x >= item[0] and x <= (item[0] + 4) and y >= item[1] and y <= (item[1] + 4):
            return True 
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

def get_obstacles():
    """
    Returns the list of generated and saved obstacle coordinates.
    """
    global obstacles
    
    if len(obstacles) == 0:
        obstacles = create_random_obstacles()
    return obstacles