# imports
import random

#global variables
obstacles_list = []

# def start():
#     obstacle = get_obstacles()


def obstacle_create():
    """[This function will create a random x and y poision a certain random times and return it.]

    Returns:
        [A list]: [A list a x and y coordinates.]
    """
    global obstacles_list

    obstacles_list.clear()
    obstacles_list = maze_make()
    return obstacles_list


def get_obstacles():
    """[This function will get the coordinates list]

    Returns:
        [A list]: [A list a x and y coordinates.]
    """
    global obstacles_list

    if not obstacles_list:
        obstacles_list = obstacle_create()
    return obstacles_list

def is_position_blocked(x,y):
    """[This function will check if the coordinates that is being moved to han an obstacle.]

    Args:
        x ([int]): [x coordinate that will be moved to]
        y ([int]): [y coordinate that will be moved to]

    Returns:
        [Boolean]: [If there is an obstacle. True for yes and False for no]
    """
    global obstacles_list
    
    for value in obstacles_list:
        x_test = value[0] <= x <= (value[0] + 4)
        y_test = value[1] <= y <= (value[1] + 4)
        if x_test and y_test:
            return True 
    return False



def is_path_blocked(x1,y1, x2, y2):
    """[summary]

    Args:
        x1 ([int]): [x starting coordinate]
        y1 ([int]): [y starting coordinate]
        x2 ([int]): [x ending coordinate]
        y2 ([int]): [y ending coordinate]

    Returns:
       [Boolean]: [If there is an obstacle. True for yes and False for no]
    """
    global obstacles_list
    # print(obstacles_list)
    max_x = max([x1, x2])
    min_x = min([x1, x2])
    
    for value in obstacles_list:
        x_condition = False
        y_condition = False
        if y1 == y2:
            for i in range(value[1], value[1] + 5):
                if i == y1:
                    x_condition = True
            for i in range(int(min_x), int(max_x) + 1):
                if i >= value[0] and i <= value[0] + 4:
                    y_condition = True
        if x_condition == True and y_condition == True:
            return True

    max_y = max([y1, y2])
    min_y = min([y1, y2])
    for value in obstacles_list:
        x_condition = False
        y_condition = False
        if x1 == x2:
            for i in range(value[0], value[0] + 5):
                if i == x1:
                    x_condition = True
            for i in range(min_y, max_y + 1):
                if i >= value[1] and i <= value[1] + 4:
                    y_condition = True
        if x_condition == True and y_condition == True:
            return True

    return False


def maze_grid_maker():
    global obstacles_list
        
    y_condition = -195
    y = 195
    x = 95
    x_condition = -95
    while x >= x_condition:
        y = 195
        while y >= y_condition:
            obstacles_list.append([x,y])
            y=y-5
        x=x-5
    # print(len(obstacles_list))
    return obstacles_list


def maze_path_maker_v(maze_position_coord,end_coord1,end_coord2,remove_ob_list,i):
    maze_position_coord = [i+10,0]
    
    while maze_position_coord[1] != (end_coord1[1]*-1):
        S_neighbour = [(maze_position_coord[0]),(maze_position_coord[1]-5)]
        maze_position_coord = S_neighbour
        remove_ob_list.append(maze_position_coord)
    
    while maze_position_coord[1] != end_coord1[1]:
        N_neighbour = [(maze_position_coord[0]),(maze_position_coord[1]+5)]
        maze_position_coord = N_neighbour
        remove_ob_list.append(maze_position_coord)

    maze_position_coord = [i+10,0]

    while maze_position_coord[1] != (end_coord2[1]*-1):
        S_neighbour = [(maze_position_coord[0]),(maze_position_coord[1]-5)]
        maze_position_coord = S_neighbour
        remove_ob_list.append(maze_position_coord)
    
    while maze_position_coord[1] != end_coord2[1]:
        N_neighbour = [(maze_position_coord[0]),(maze_position_coord[1]+5)]
        maze_position_coord = N_neighbour
        remove_ob_list.append(maze_position_coord)

    return remove_ob_list


def maze_path_maker_h(maze_position_coord,end_coord1,end_coord2,remove_ob_list,i):
    maze_position_coord = [0,i+5]
    
    while maze_position_coord[0] != end_coord1[0]:
        E_neighbour = [(maze_position_coord[0]+5),(maze_position_coord[1])]
        maze_position_coord = E_neighbour
        remove_ob_list.append(maze_position_coord)
    
    maze_position_coord = [0,i+5]

    while maze_position_coord[0] != end_coord2[0]:
        W_neighbour = [(maze_position_coord[0]-5),(maze_position_coord[1])]
        maze_position_coord = W_neighbour
        remove_ob_list.append(maze_position_coord)
    
    

    return remove_ob_list


def starting_point_clear():
    remove_ob_list = []
    start_coord = [0,0]

    N_start_coord = [0,5]
    E_start_coord = [5,0]
    S_start_coord = [0,-5]
    W_start_coord = [-5,0]

    NE_start_coord = [5,5]
    SE_start_coord = [5,-5]
    SW_start_coord = [-5,-5]
    NW_start_coord = [-5,5]

    end_coord1 = [95,195]
    end_coord2 = [-95,195]
    end_coord3 = [-95,-195]
    end_coord4 = [95,-195]

    remove_ob_list.append(start_coord)
    
    remove_ob_list.append(N_start_coord)
    remove_ob_list.append(E_start_coord)
    remove_ob_list.append(S_start_coord)
    remove_ob_list.append(W_start_coord)

    remove_ob_list.append(NW_start_coord)
    remove_ob_list.append(SW_start_coord)
    remove_ob_list.append(SE_start_coord)
    remove_ob_list.append(NE_start_coord)

    remove_ob_list.append(end_coord1)
    remove_ob_list.append(end_coord2)
    remove_ob_list.append(end_coord3)
    remove_ob_list.append(end_coord4)
    
    return remove_ob_list


def maze_random_grid_create(remove_ob_list):
    maze_position_coord = [0,0]

    end_coord1 = [75,195]
    end_coord2 = [-75,195]
    for i in range(-100,101,15):
        remove_ob_list = maze_path_maker_v(maze_position_coord,end_coord1,end_coord2,remove_ob_list,i)

    end_coord1 = [95,190]
    end_coord2 = [-95,-190]
    for i in range(-200,191,30):
        remove_ob_list = maze_path_maker_h(maze_position_coord,end_coord1,end_coord2,remove_ob_list,i)
    
    return remove_ob_list


def random_maze_creation(new_x,new_y,ob_list,x,y):
    new_ob_list = []
    x = new_x
    y = new_y
    
    if x > 95 or y > 195:
        return ob_list
    
    N_start_coord = [x,y]
    E_start_coord = [x,y]
    S_start_coord = [x,(y*-1)]
    W_start_coord = [(x*-1),y]

    NE_start_coord = [x,y]
    SE_start_coord = [x,(y*-1)]
    SW_start_coord = [(x*-1),(y*-1)]
    NW_start_coord = [(x*-1),y]

    new_ob_list.append(N_start_coord)
    new_ob_list.append(E_start_coord)
    new_ob_list.append(S_start_coord)
    new_ob_list.append(W_start_coord)
    new_ob_list.append(NE_start_coord)
    new_ob_list.append(SE_start_coord)
    new_ob_list.append(SW_start_coord)
    new_ob_list.append(NW_start_coord)
    for i in new_ob_list: 
        ob_list.append(i)
    random_maze_creation(new_x+5,new_y+5,ob_list,x,y)
    return ob_list


def maze_remover(remove_ob_list,ob_list):
    for i in remove_ob_list:
        if i in ob_list:
            ob_list.remove(i)
    return ob_list

def print_message(name):
    print(name +" : Loaded simple_maze.")

def maze_make():
    global obstacles_list
    #print(len(obstacles_list))
    maze_full_list = maze_grid_maker()
    maze_starting_point_list = starting_point_clear()
    maze_grid_list = maze_random_grid_create(maze_starting_point_list)
    maze_random_create_list = random_maze_creation(-30,-130,maze_grid_list,0,0)
    maze_remover(maze_random_create_list,maze_full_list)
    # print(len(obstacles_list))
    # print(len(maze_random_create_list))
    return obstacles_list




# if __name__ == '__main__':
#     get_obstacles()


#     # print(is_path_blocked(0,23, 11, 23))
#     print(is_position_blocked(-40,0))