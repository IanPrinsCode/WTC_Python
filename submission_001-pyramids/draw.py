# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    shape = shape.lower()
    if shape != "pyramid" and shape != "square" and shape != "triangle" and shape != "diamond" and shape != "reverse triangle" and shape != "rev triangle" and shape != "revtriangle" and shape != "rhombus":
        return get_shape()
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height_param = 0
    while (height_param > 80 or height_param < 1) or str(height_param).isdigit() == False:
        try:
            height_param = int(input('Height?: '))    
        except:
            pass
    return height_param

def draw_diamond(height, outline):
    if outline == False:
        z = 1
        if (height % 2 == 0):
            z = 0
        for star_count in range(1, int(height/2 + 1)):
            print(" " * (height - star_count) + "* " * star_count)
        for star_count in range(int(height / 2 + z), 0, -1):
            print(" " * (height - star_count) + "* " * star_count)
    elif outline == True:
        z = 1 
        if (height % 2 == 0):
            z = 0
        for y in range(1, int(height / 2 + 1) + z):
            for x in range(1, 2 * int(height / 2 + 1)):
                if(y + x == int(height / 2 + 1) + 1) or (x - y == int(height / 2 + 1) - 1):
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print("")
        for y in range(int(height / 2 + 1) - 1, 0, -1):
            for x in range(1, 2 * int(height / 2 + 1)):
                if(y + x == int(height / 2 + 1) + 1) or (x - y == int(height / 2 + 1) - 1):
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print("")

def draw_rev_triangle(height, outline):
    if outline == False:
        x = 0
        z = 1
        while (x < height):
            y = 0
            while (y <= height - z):
                print('*', end = '')
                y += 1
            print('')
            x += 1   
            z += 1
    elif outline == True:
        x = 0
        z = 1
        while (x < height):
            y = 0
            while (y <= height - z):
                if (x == 0 or y == 0 or x + y == height - 1):
                    print('*', end = '')
                else:
                    print(" ", end = "")
                y += 1
            print('')
            x += 1   
            z += 1

def draw_rhombus(height, outline):
    if outline == False:
        x = 0
        z = 2
        while (x < height):
            y = 0
            i = 0
            while (y <= height - z):
                print(' ', end = '')
                y += 1
            while (i < height):
                print("*", end = "")
                i += 1
            print('')
            x += 1   
            z += 1
    elif outline == True:
        x = 0
        z = 2
        while (x < height):
            y = 0
            i = 0
            while (y <= height - z):
                print(' ', end = '')
                y += 1
            while (i < height):
                if (x == 0 or x == height - 1 or i == 0 or i == height - 1):
                    print("*", end = "")
                    i += 1
                else:
                    print(" ", end = "")
                    i += 1
            print('')
            x += 1   
            z += 1


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        star_count = 0
        for i in range(1, height + 1):
            for j in range(1, (height - i) + 1):
                print(end = " ")
            while (star_count != ((2 * i) - 1)):
                print("*", end = "")
                star_count += 1
            star_count = 0
            print("")
    elif outline == True:
        for x in range(1, height + 1):
            for y in range(1, 2 * height):
                if (x == height or x+y == height+1 or y-x == height-1):
                    print("*", end = "")
                elif (y < height + x):
                    print(" ", end = "")
            print("")




# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for y in range(0, height):
            for x in range(0, height):
                print("*", end = "")
            print("")
    elif outline == True:
        x = 0
        while (x < height):
            y = 0
            while (y < height):
                if (x == 0 or x == height - 1 or y == 0 or y == height - 1):
                    print('*', end = '')
                else:
                    print(" ", end = "")
                y += 1
            print('')
            x += 1


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        x = 0
        z = height
        while (x < height):
            y = 0
            while (y <= height - z):
                print('*', end = '')
                y += 1
            print('')
            x += 1   
            z -= 1
    elif outline == True:
        x = 0
        z = height
        while (x < height):
            y = 0
            while (y <= height - z):
                if (x == height - 1 or y == 0 or x == y):
                    print('*', end = '')
                else:
                    print(" ", end = "")
                y += 1
            print('')
            x += 1   
            z -= 1



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if (shape == "pyramid"):
        draw_pyramid(height, outline)
    if (shape == "square"):
        draw_square(height, outline)
    if (shape == "triangle"):
        draw_triangle(height, outline)
    if (shape == "diamond"):
        draw_diamond(height, outline)
    if (shape == "reverse triangle" or shape == "rev triangle" or shape == "revtriangle"):
        draw_rev_triangle(height, outline)
    if (shape == "rhombus"):
        draw_rhombus(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = False
    answer = input('Outline only? (y/N):')
    while (answer != "y" and answer != "N"):
        print('Invalid input.')
        answer = input('Outline only? (y/N):')
    if (answer == 'y'):
        outline = True
    if (answer == 'N'):
        outline = False
    return outline


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

