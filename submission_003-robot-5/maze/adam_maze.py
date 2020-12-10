import random


obstacles = []


def generate_obstacles():
    global obstacles
    carve_list = []

    obstacles.clear()

    for j in range(-200, 200, 5):
        for i in range (-100, 105, 5):
            current = [i, j]
            if current != [0, 0] and current != [0,-5] and current != [0,5]:
                obstacles.append(current)

    current = [-95, -195]
    (w,x,y,z) = (190,95,-195,-95)
    while w > -0:
        while current[1] < w:
            if current in obstacles:
                obstacles.remove(current)    
            current[1] += 5

        while current[0] < x:
            if current in obstacles:
                obstacles.remove(current) 
            current[0] += 5

        while current[1] > y:
            if current in obstacles:
                obstacles.remove(current)
            current[1] -= 5

        while current[0] > z:
            if current in obstacles:
                obstacles.remove(current) 
            current[0] -= 5

        current[0] += 10
        current[1] += 10
        (w,x,y,z) = (w - 10, x - 10, y + 10, z + 10)

    obstacles.remove([-100,0])
    obstacles.remove([100,0])
    obstacles.remove([0,-200]) 
    obstacles.remove([0,195]) 

   
    for j in range(-195, 195, 5):
        for i in range (-95, 100, 15):
            current = [i, j]
            if current in obstacles and (current[0] == -current[1] or -current[0] == current[1]):
                obstacles.remove(current)
        for i in range (-95, 100, 37):
            current = [i, j]
            if current in obstacles and (current[0] == -current[1] or -current[0] == current[1]):
                obstacles.remove(current)
        for i in range (-95, 100, 65):
            current = [i, j]
            if current in obstacles and (current[0] == -current[1] or -current[0] == current[1]):
                obstacles.remove(current)
        for i in range (-95, 100, 35):
            current = [i, j]
            if current in obstacles and (current[0] == -current[1] or -current[0] == current[1]):
                obstacles.remove(current)


    return obstacles


def is_position_blocked(x,y):
    for i in range(len(obstacles)):
        if ((x <= obstacles[i][0] + 4) and (x >= obstacles[i][0])) and ((y <= obstacles[i][1] + 4) and (y >= obstacles[i][1])):
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    for i in range(len(obstacles)):
        if y1 == y2:
            if (x1 < obstacles[i][0] < x2 or x1 > obstacles[i][0] > x2):
                return True    
        if x1 == x2:        
            if (y1 < obstacles[i][1] < y2 or y1 > obstacles[i][1] > y2):
                return True
    return False


def get_obstacles():
    global obstacles
    #for x in obstacles:
    #    if x == (0,0):
    #        obstacles.remove(x)
    return obstacles