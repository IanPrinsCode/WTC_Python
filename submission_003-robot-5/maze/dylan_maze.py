import random, sys

maze = {}
blocks = []


def create_grid():
    """
    =   generate_maze() creates a 2-dimensional grid in the form
        of a dictionary. Each key is a coordinate in the form 
        "x,y" and the values are either 1 or 0. It initializes the 
        the dictionary with all values set to 1.
        1. Values of 1 represent coordinates which the robot has not
           visited.
        2. The maze must have a starting point. To ensure that the
           maze which is generated is different each time the program
           is run, the starting point is set as a random coordinate.
           The value of the starting point is set to 0 to indicate
           that the robot has visited the coordinate.
        3. This function calls the depth-first search algorithm, 
           maze_generator, passing it the value of the starting point.   
    """
    global maze
    # Create a maze, each block is assigned a value of 1.
    
    for y in range(1, 79):
            for x in range(1, 40):
                dict_name = "{},{}".format(x,y)
                maze[dict_name] = 1
     
     
    # Create Random starting cell:
    x = random.randint(1, 39)
    y = random.randint(1, 78)
    while x % 2 == 0 and y % 2 == 0:
        x = random.randint(1, 39)
        y = random.randint(1, 78)

    # Set the visited value of the starting coordinate to 0:
    starting_point = "{},{}".format(x,y)
    maze[starting_point] = 0

    maze_generator(x, y)
    

def maze_generator(x, y):
    """
    =   maze_generator() is a depth-first search algorithm. It will
        follow the following procedure until the maze is created.
        1. Generate an int array with 4 random numbers to represent directions.
        2. Start a for loop to go for 4 times.
        3. Set up an if, elif statement to take care of 4 directions.
        4. For that direction, check if the new cell will be out of 
           maze or if it’s a path already open. If so, do nothing.
        5. If the cell in that direction is a wall, set that cell to 
           path and call recursive method passing the new current position.
    """
    global maze
     # 4 random directions
    random_directions = generate_random_directions()
    
    # Check whether each direction is visited:
    
    for numbers in range(1,5):
        num = random_directions[numbers - 1]
        if num == 1:
            #　Check whether the 2 western cells have been visited
            if x - 2 <= 1:
                continue
            if maze[f"{x - 2},{y}"] != 0:
                maze[f"{x - 2},{y}"] = 0
                maze[f"{x - 1},{y}"] = 0
                maze_generator(x - 2, y)
        elif num == 2:
            # Check whether the 2 northern cells have been visited
            if y + 2 >= 78:
                continue
            if maze[f"{x},{y + 2}"] != 0:
                maze[f"{x},{y + 2}"] = 0
                maze[f"{x},{y + 1}"] = 0
                maze_generator(x, y + 2)
        elif num == 3:
            # Check whether the 2 eastern cells have been visited
            if x + 2 >= 38:
                continue
            if maze[f"{x + 2},{y}"] != 0: 
                maze[f"{x + 2},{y}"] = 0
                maze[f"{x + 1},{y}"] = 0
                maze_generator(x + 2, y)  
        elif num == 4: # West
            # Check whether the 2 western cells have been visited
            if y - 2 <= 1:
                continue
            if maze[f"{x},{y - 2}"] != 0:
                maze[f"{x},{y - 2}"] = 0
                maze[f"{x},{y - 1}"] = 0
                maze_generator(x, y - 2)
            


def generate_random_directions():
    """
    generate_random_directions() shuffles the randoms
    list and returns it. The goal of this function is to 
    create a random series of directions in which the 
    algorithm checks surrounding coordinates.  
    """
    randoms = [1,2,3,4]
    
    random.shuffle(randoms)
    
    return randoms
 

def get_obstacles():
    """
    get_obstacles() executes the other functions in this module.
    It returns a list of tuples. Each tuple represents the location
    of an obstacle in the robot's navigable area.
    1. get_obstacles() calls a helper function, 
       convert_coordinates_to_tuples(), so that it can return a list
       of tuples instead of a dictionary.
    """
    global maze, blocks

    create_grid()

    obstacles = {}
    # Returning a dictionary of all obstacle coordinates:
    for (key, value) in maze.items():
        if value == 0:
            obstacles[key] = value

    convert_coordinates_to_tuples(obstacles)
    
    clear_maze_center()
    
    return blocks


def convert_coordinates_to_tuples(obstacle_dictionary):
    """
    convert_coordinates_to_tuples() will iterate through the
    dictionary of obstacles and populate the blocks list
    with obstacles in their tuple-form. It calculates x and
    y values based on the quadrants in which the robot
    moves. The quadrants referred to below are as follows:
     1 | 2
    ___|___
       | 
     3 | 4
    """
    global blocks

    for key in obstacle_dictionary.keys():
        coordinates = key.split(',')
        x = int(coordinates[0])
        y = int(coordinates[1])

        # If the x value of the dict is in quadrant 1 or 3:
        if x <= 19:
            tuple_x = -(100) + (x * 5)
        # If the x value of the dict is in quadrant 2 or 4:
        elif x >= 20:
            tuple_x = (x - 20) * 5

        tuple_y = -(((y-40) * 5) + 5)

        blocks.append((tuple_x,tuple_y))


def clear_maze_center():
    """
    This function clears the central area of the maze so that
    the robot can freely navigate from its starting point.
    """
    global blocks

    invalid_coordinates = []
    for nums in range(-25, 25):
        invalid_coordinates.append(nums)

    blocks = [item for item in blocks if not (item[0] in invalid_coordinates and item[1] in invalid_coordinates)]


def is_position_blocked(x,y):
    """
    is_position_blocked() will check whether a coordinate (x, y)
    falls within the scope of an obstacle.
    1. First, it gets the coordinates contained in the blocks variable.
    2. For each coordinate, it will populate the obstacle_area local
       variable with all coordinates that are a part of that obstacle.
       This means that each coordinate that falls within the bounds of
       an obstacle will be contained in obstacle_area
    3. Finally, it will check whether the coordinate supplied by the
       function call is one of the coordinates in the obstacle_area
    """
    global blocks
    obstacle_area = []
    for item in blocks:
        for x_coordinate in range(0, 5):
            for y_coordinate in range(0,5):
                obstacle_area.append((item[0] + x_coordinate, item[1] + y_coordinate))   
    if (x, y) in obstacle_area:
        return True
    else:
        return False

"""
TODO: Fix the order of parameters.
"""
def is_path_blocked(x1, y1, x2, y2):
    """
    is_path_blocked() will check the path ahead of the robot for
    obstacles.
    1. If it is moving along the x axis, it uses the change in x-coordinates
       and calls is_position_blocked() as a helper function for each coordinate.
       If, at any point, the robot encounters an obstacle along the path, it
       will inform the user that there is an obstacle in the way.
    2. If it is moving along the y axis, it uses the change in y-coordinates
       and calls is_position_blocked() as a helper function for each coordinate.
       If, at any point, the robot encounters an obstacle along the path, it
       will inform the user that there is an obstacle in the way.
    3. The robot can move in 4 directions, so a check is performed for whether
       the robot is moving up down, left or right.        
    """
    if x1 == x2:
        if y1 < y2:
            for nums in range(y1, y2 + 1):
                if is_position_blocked(x1, nums):
                    return True
        elif y1 > y2:
            for nums in range(y1, y2 - 1, -1):
                if is_position_blocked(x1, nums):
                    return True
        return False
    elif y1 == y2:
        if x1 < x2:
            for nums in range(x1, x2 + 1):
                if is_position_blocked(nums, y1):
                    return True
        elif x1 > x2:
            for nums in range(x1, x2 - 1, -1):
                if is_position_blocked(nums, y1):
                    return True
        return False
