def move_square(size):
    """Moving in square of size being passed as parameter."""
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width):
    """Moving in rectangle of length and width being passed as parameters."""
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    """Moving in a circle."""
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def move_dancing_square(length):
    """Moving in 3 squares."""
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)

def move_crop_circle(length):
    """Moving in 4 circles."""
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


def move():
    """I would call this function action(), because there can be different actions could be implemented on objects."""
    size = 10
    length = 20
    width = 10
    move_square(size)
    move_rectangle(length, width)
    move_circle()
    move_dancing_square(length)
    move_crop_circle(length)

def robot_start():
    """Start robot program."""
    move()

if __name__ == "__main__":
    robot_start()
