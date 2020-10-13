"""The different functions in this class return possible commands in a list
of strings. These lists are used for matching with the input. There is a piece
in the program that checks if the input command contains one of these valid
commands and then triggers the necessary functions based on if the input is
valid and if so, what it is asking the program to do."""
class RobotCommands:
    def get_commands():
        command_list = [
            "off",
            "help",
            "right",
            "left"
        ]
        return command_list
    def get_movements():
        movements_list = [
            "forward",
            "back",
            "sprint"
        ]
        return movements_list


"""This function receives an input and saves it into a variable as the
robot's name. This program returns the name in uppercase, because all
print statements in the rest of the program that include the robot's name,
must print the name in uppercase. This function also prints the hello
message once it has received an input."""
def name_robot():
    robot_name = input("What do you want to name your robot? ")
    print(robot_name.upper() + ": Hello kiddo!")
    return robot_name.upper()


"""After a name is received, this function gets called to receive an
input from the user for the program to execute. It tests if the input
is a valid command. If it is invalid, the program prints an error message
and asks for input again. The function returns the command, so that it
can be interpreted and executed somewhere else in the program. The robot's
name is being passed as a parameter so that it can be used in the dialogue
that is being printed."""
def get_input(robot_name):
    command_list = RobotCommands.get_commands()
    movements_list = RobotCommands.get_movements()
    command = input(robot_name + ": What must I do next? ")
    command_lower = command.lower()
    command_struct = list(command.split())
    if command_lower not in command_list and not any(ele in command_lower for ele in movements_list):
        print(robot_name + ": Sorry, I did not understand '" + command + "'.")
    if any(ele in command_lower for ele in movements_list) and len(command_struct) == 1:
        print(robot_name + ": Sorry, I did not understand '" + command + "'.")
    if len(command_struct) > 2:
        print(robot_name + ": Sorry, I did not understand '" + command + "'.")
    return command_lower


"""This function is called when the "right" command is used. The current
position that the robot is facing is being passed as a parameter. This function
changes the face position accordingly based on the current position, and returns
the new face position."""
def change_position_right(face_position):
    if face_position == "front":
        face_position = "right"
    elif face_position == "right":
        face_position = "back"
    elif face_position == "back":
        face_position = "left"
    elif face_position == "left":
        face_position = "front"
    return face_position


"""This function is called when the "left" command is used. The current position
that the robot is facing is being passed as a parameter. This function changes
the face position accordingly based on the current position, and returns the new
face position."""
def change_position_left(face_position):
    if face_position == "front":
        face_position = "left"
    elif face_position == "right":
        face_position = "front"
    elif face_position == "back":
        face_position = "right"
    elif face_position == "left":
        face_position = "back"
    return face_position


"""Implements the forward movement of move_size on the coordinates according to
the current face_position and returns the new coordinates values."""
def implement_movement_forward(face_position, coordinates, move_size):
    if face_position == "front":
        coordinates[1] += move_size
    if face_position == "right":
        coordinates[0] += move_size
    if face_position == "back":
        coordinates[1] -= move_size
    if face_position == "left":
        coordinates[0] -= move_size
    return coordinates


"""Implements the backwards movement of move_size on the coordinates according to
the current face_position and returns the new coordinates values."""
def implement_movement_backwards(face_position, coordinates, move_size):
    if face_position == "front":
        coordinates[1] -= move_size
    if face_position == "right":
        coordinates[0] -= move_size
    if face_position == "back":
        coordinates[1] += move_size
    if face_position == "left":
        coordinates[0] += move_size
    return coordinates


"""Tests if the new coordinates after the current forwards command is executed will
be within the valid range. Returns a boolean value indicating if the command will be valid.
If it is valid, another function will be called to execute the forward movement."""
def test_range_forward(face_position, coordinates, move_size):
    is_valid = True
    if face_position == "front":
        if coordinates[1] + move_size >= 201:
            is_valid = False
    if face_position == "right":
        if coordinates[0] + move_size >= 101:
            is_valid = False
    if face_position == "back":
        if coordinates[1] - move_size <= -201:
            is_valid = False
    if face_position == "left":
        if coordinates[0] - move_size <= -101:
            is_valid = False
    return is_valid


"""Tests if the new coordinates after the current backwards command is executed will be
within the valid range. Returns a boolean value indicating if the command will be valid.
If it is valid, another function will be called to execute the backward movement."""
def test_range_backwards(face_position, coordinates, move_size):
    is_valid = True
    if face_position == "front":
        if coordinates[1] - move_size <= -201:
            is_valid = False
    if face_position == "right":
        if coordinates[0] - move_size <= -101:
            is_valid = False
    if face_position == "back":
        if coordinates[1] + move_size >= 201:
            is_valid = False
    if face_position == "left":
        if coordinates[0] + move_size >= 101:
            is_valid = False
    return is_valid


"""Prints out the sprint message recursively when the sprint command is entered."""
def do_sprint(robot_name, coordinates, move_size):
    if move_size != 0:
        print(*" > " + robot_name.upper() + " moved forward by " + str(move_size) + " steps.", sep="")
        do_sprint(robot_name, coordinates, move_size - 1)

def display_help():
    help_string = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move robot forward
BACK - move robot backwards
RIGHT - turn robot to the right
LEFT - turn robot to the left
SPRINT - robot sprints forward"""
    return help_string


"""This function binds all the smaller functions together. Input gets received
and is then interpreted here. This function searches for keywords in the input
and then triggers the appropriate functionality related to that keyword.
This function also prints error messages, gives feedback on what the program
is doing and updates on the robot's coordinates."""
def robot_start():
    face_position = "front"
    robot_name = name_robot()
    command_list = RobotCommands.get_commands()
    movements_list = RobotCommands.get_movements()
    coordinates = [0, 0]
    while True:
        command = get_input(robot_name)
        command_struct = list(command.split())
        if any(ele in command for ele in movements_list) and len(command_struct) == 1:
            continue
        for i in range(len(movements_list)):
            if movements_list[i] in command.lower():
                movement_struct = command.split(" ")
        if command.lower() == "off":
            print(robot_name.upper() + ": Shutting down..")
            break
        if command == "help":
            # print("I can understand these commands:")
            # print(*command_list[0].upper() + "  - Shut down robot", sep="")
            # print(*command_list[1].upper() + " - provide information about commands", sep="")
            # print(*movements_list[0].upper() + " - move robot forward", sep="")
            # print(*movements_list[1].upper() + " - move robot backwards", sep="")
            # print(*command_list[2].upper() + " - turn robot to the right", sep="")
            # print(*command_list[3].upper() + " - turn robot to the left", sep="")
            # print(*movements_list[2].upper() + " - robot sprints forward", sep="")
            print(display_help())

        if "sprint" in command.lower() and len(command_struct) == 2:
            mov_sum = 0
            for i in range(int(movement_struct[1]) + 1):
                mov_sum += i
            valid_range = test_range_forward(face_position, coordinates, mov_sum)
            if valid_range == False:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
                continue
            do_sprint(robot_name, coordinates, int(movement_struct[1]))
            coordinates = implement_movement_forward(face_position, coordinates, mov_sum)
            print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
        if "forward" in command.lower() and len(command_struct) == 2:
            valid_range = test_range_forward(face_position, coordinates, int(movement_struct[1]))
            if valid_range == False:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
                continue
            coordinates = implement_movement_forward(face_position, coordinates, int(movement_struct[1]))
            print(*" > " + robot_name.upper() + " moved forward by " + movement_struct[1] + " steps.", sep="")
            print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
        if "back" in command.lower() and len(command_struct) == 2:
            valid_range = test_range_backwards(face_position, coordinates, int(movement_struct[1]))
            if valid_range == False:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
                continue
            coordinates = implement_movement_backwards(face_position, coordinates, int(movement_struct[1]))
            print(*" > " + robot_name.upper() + " moved back by " + movement_struct[1] + " steps.", sep="")
            print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
        if command == "right":
            face_position = change_position_right(face_position)
            print(*" > " + robot_name + " turned right.", sep="")
            print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")
        if command == "left":
            face_position = change_position_left(face_position)
            print(*" > " + robot_name + " turned left.", sep="")
            print(*" > " + robot_name.upper() + " now at position " + "("+str(coordinates[0])+","+str(coordinates[1])+").", sep="")


"""This is the main. It initializes the run of the whole program."""
if __name__ == "__main__":
    robot_start()

