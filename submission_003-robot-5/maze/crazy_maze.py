import random

#obstacle list
obstacles = []


def draw_x_wall_door(x1,x2,y):
    """
    draw_x_wall_door function draws walls with a randomly placed exit
    on the top and bottom boundaries of the map
    """
    global obstacles
    door = random.randint(x1,x2)
    while x1 <= x2:
        position = (x1,y)
        obstacles.append(position)
        x1+=4
        if door in range(x1 -4, x1):
            obstacles.pop()


def draw_y_wall_door(y1,y2,x):
    """
    draw_y_wall_door function draws walls with a randomly placed exit
    on the left and right boundary lines of the map
    """
    global obstacles
    door = random.randint(y1,y2)
    while y1 <= y2:
        position = (x,y1)
        obstacles.append(position)
        y1+=4
        if door in range(y1 -4, y1):
            obstacles.pop()


def is_position_blocked(x, y):               
    """
    is_position_blocked checks if the new destination
    of the robot is the position of an obstacle and 
    returns True or False accordingly.
    """

    for item in obstacles:        
        if (x >= item[0] and x <= item[0] + 4) and (y >= item[1] \
            and y <= item[1] + 4):
            return True
    return False                                    


def is_path_blocked(x1, y1, x2, y2):         
    """                                      
    the is_path_blocked function checks if there 
    are any obstacles in the path between    
    the starting point and end point         
    """                                      

    global obstacles                         

    max_x = max([x1, x2])                    
    min_x = min([x1, x2])                    
    max_y = max([y1, y2])                    
    min_y = min([y1, y2])                    

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
    The Function get_obstacles() checks if the global list is empty
    then runs the gen_obstacles() if its an empty list 
    after that it returns the list
    """
    global obstacles
    
    if len(obstacles) == 0:
        draw_boarder()
        draw_maze()
    return obstacles                                   


def draw_wall_x(x1,x2,y):
    """
    creates all the horizontal walls on the map
    """
    global obstacles
    while x1 <= x2:
        position = (x1,y)
        obstacles.append(position)
        x1+=4


def draw_wall_y(y1,y2,x):
    """
    creates all the vertical walls on the map
    """
    global obstacles
    while y1 <= y2:
        position = (x,y1)
        obstacles.append(position)
        y1+=4


def  draw_maze():
    """
    calls the draw_wall_x and draw_wall_y function
    and draws the appropriate walls accordingly
    """
    #x_walls:
    draw_wall_x(-100,-20,0)
    draw_wall_x(-80,-30,175)
    draw_wall_x(20,70,160)
    draw_wall_x(-60,70,140)
    draw_wall_x(-100,-30,100)
    draw_wall_x(20,95,75)
    draw_wall_x(-80,-55,50)
    draw_wall_x(-30,40,50)
    draw_wall_x(-30,20,25)
    draw_wall_x(35,75,25)
    draw_wall_x(-60,-40,-25)
    draw_wall_x(-20,35,-25)
    draw_wall_x(-75,20,-75)
    draw_wall_x(40,99,-75)
    draw_wall_x(-100,70,-115)
    draw_wall_x(-80,-50,-150)
    draw_wall_x(-30,0,-150)
    draw_wall_x(35,70,-150)
    draw_wall_x(-30,35,-175)
    #y_walls:
    draw_wall_y(-200,-175,20)
    draw_wall_y(-200,-150,-80)
    draw_wall_y(-155,-125,-50)
    draw_wall_y(-175,-130,25)
    draw_wall_y(-150,-90,0)
    draw_wall_y(-150,-125,70)
    draw_wall_y(-150,-115,50)
    draw_wall_y(-100,-75,-30)
    draw_wall_y(-85,-25,20)
    draw_wall_y(-75,-20,-50)
    draw_wall_y(-75,-20,60)
    draw_wall_y(0,25,-25)
    draw_wall_y(-25,50,35)
    draw_wall_y(0,25,-25)
    draw_wall_y(50,100,-75)
    draw_wall_y(75,100,20)
    draw_wall_y(70,140,-20)
    draw_wall_y(100,175,-80)
    draw_wall_y(140,175,-30)
    draw_wall_y(150,200,0)
    draw_wall_y(150,200,70)


def draw_boarder():
    """
    the draw_boarder function draws places walls around the boundary
    of the map with random exits on each wall
    """
    draw_x_wall_door(-100,97,198)
    draw_x_wall_door(-100,97,-200)
    draw_y_wall_door(-200,197,-100)
    draw_y_wall_door(-200,200,98)