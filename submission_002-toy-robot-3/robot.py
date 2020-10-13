"""This class controlls the tracking of previous commands into a list.  Creating an instance
of this class will create an empty history_list.  The track() function appends only the relevent
commands into the history-list.  get_history() returns the history_list, which is used when doing
replay commands."""
class History():
    def __init__(self):
        self.history_list = []

    def track(self, command):
        track = False
        if command not in ['replay', 'off', 'help', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent']:
            track = True
        if 'replay' in command or 'reversed' in command or 'silent' in command and command != 'replay reversed silent':
            track = False
        if track == True:
            self.history_list.append(command)

    def get_history(self):
        return self.history_list


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


"""This function asks for input and saves the robot's name into a variable.  It then returns
the name in uppercase."""
def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name.upper()


"""Asks the user for a command, and validate it as well.  Only return a valid command."""
def get_command(robot_name):
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command.lower()):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    return command.lower()


"""Splits the string at the first space character, to get the actual command, as well as the
argument(s) for the command
:return: (command, argument)"""
def split_command_input(command):
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


"""Tests if the string value is an int or not
:param value: a string value to test
:return: True if it is an int"""
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


"""Returns a boolean indicating if the robot can understand the command or not.  Also checks if
there is an argument to the command, and if it a valid int."""
def valid_command(command):
    (command_name, args) = split_command_input(command)
    if command_name == 'replay' and command != 'replay':
        return test_replay_range(args)
        
    return command_name.lower() in valid_commands


"""This function takes all of the arguments of the input, except the first one, finds the range
argument and tests if the range is valid or not.  If it is valid, it gets removed from args.
It also searches for all valid keywords and removes them from args.  A boolean is being returned.
If there are no arguments left in args, it means that all of the arguments were valid, thus returning
True.  If arguments are still present it returns False."""
def test_replay_range(args):
    arg_list = args.lower().split(' ')
    if len(arg_list) > 0:

        for i in arg_list:
            if i.isdigit():
                arg_list.remove(i)
        for i in arg_list:
            if i.find('-') and len(i.split('-')) == 2:
                for j in i.split('-'):
                    if j.isdigit():
                        is_digit = True
                    else:
                        is_digit = False
                if is_digit:
                    if i.split('-')[0] < i.split('-')[1]:
                        return False
                    arg_list.remove(i)
    if 'reversed' in arg_list:
        arg_list.remove('reversed')
    if 'silent' in arg_list:
        arg_list.remove('silent')
    
    if len(arg_list) == 0:
        return True
    else:
        return False


"""Displays command outputs on the console for all the various commands."""
def output(name, message):
    print(''+name+": "+message)


"""Provides help information to the user
:return: (True, help text) to indicate robot can continue after this command was handled."""
def do_help():
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous movement commands
REPLAY SILENT - replay previous commands without output of single commands
REPLAY REVERSED - replay previous commands in reverse
REPLAY REVERSED SILENT - replay commands in reverse without output"""


"""Displays the current position of the robot after every movement command"""
def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


"""Checks if the new position will still fall within the max area limit
:param new_x: the new/proposed x position
:param new_y: the new/proposed y position
:return: True if allowed, i.e. it falls in the allowed area, else False"""
def is_position_allowed(new_x, new_y):
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


"""Update the current x and y positions given the current direction, and specific nr of steps
:param steps:
:return: True if the position was updated, else False"""
def update_position(steps):
    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


"""Moves the robot forward the number of steps
:param robot_name:
:param steps:
:return: (True, forward output text)"""
def do_forward(robot_name, steps):
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


"""Moves the robot forward the number of steps
:param robot_name:
:param steps:
:return: (True, forward output text)"""
def do_back(robot_name, steps):
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


"""Do a 90 degree turn to the right
:param robot_name:
:return: (True, right turn output text)"""
def do_right_turn(robot_name):
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


"""Do a 90 degree turn to the left
:param robot_name:
:return: (True, left turn output text)"""
def do_left_turn(robot_name):
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


"""Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
:param robot_name:
:param steps:
:return: (True, forward output)"""
def do_sprint(robot_name, steps):

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


"""Runs the history_list in a loop to replay all previous movement commands.  Receives robot_name as parameter for
output string."""
def do_replay(robot_name):
    global is_replay_silent, history, temp_history
    command_count = 0

    for command in history.get_history():
        handle_command(robot_name, command)
        command_count += 1
    return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands.'


"""Runs the history_list in a loop to replay all previous movement commands.  Receives robot_name as parameter for
output string.  The is_replay_silent boolean is implemented on the print statement so that output is not given for
the replay of these commands."""
def do_replay_silent(robot_name):
    global is_replay_silent, history
    is_replay_silent = True
    command_count = 0

    for command in history.get_history():
        handle_command(robot_name, command)
        command_count += 1
    is_replay_silent = False
    return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands silently.'


"""Reverses the history_list and then runs it in a loop to replay all previous movement commands in reverse.  Receives
robot_name as parameter for output string.  """
def do_replay_reversed(robot_name):
    command_count = 0

    for command in history.get_history()[::-1]:
        handle_command(robot_name, command)
        command_count += 1
    return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands in reverse.'


"""Reverses the history_list and then runs it in a loop to replay all previous movement commands in reverse.  Receives
robot_name as parameter for output string.  The is_replay_silent boolean is implemented on the print statement so that
output is not given for the replay of these commands."""
def do_replay_reversed_silent(robot_name):
    global is_replay_silent
    is_replay_silent = True
    command_count = 0

    for command in history.get_history()[::-1]:
        handle_command(robot_name, command)
        command_count += 1
    is_replay_silent = False
    return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands in reverse silently.'


"""Robot_name is passed as parameter to be returned in the output string.  args in passed as parameter and inspected for
flagging keywords.  If 'silent' is found in args, the is_replay_silent boolean is implemented so that output strings are
not printed.  If 'reversed' is found in args, the history_list is reversed and saved into a new temp_history.  The range
argument in args is then tested if it is one number or a range containing a '-', and the appropriate function is then called
to implement the range on the new temp_history.  The function runs a loop on the new specialized temp_history to give desired
output."""
def do_replay_range(robot_name, args):
    global history, temp_history, is_replay_silent
    num_range = ""
    command_count = 0

    new_arg = rearrange_command(args)
    temp_history = history.get_history()
    
    if 'silent' in args:
        is_replay_silent = True
    if 'reversed' in args:
        temp_history = temp_history[::-1]
    if new_arg[0].find('-') == True:
        num_range = new_arg[0].split('-')
        temp_history = get_range_nums(temp_history, num_range)
    else:
        num_range = new_arg[0]
        temp_history = get_range_num(temp_history, int(num_range))

    for command in temp_history:
        handle_command(robot_name, command)
        command_count += 1
    is_replay_silent = False
    if 'silent' in args and 'reversed' in args:
        return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands in reverse silently.'
    elif 'silent' in args:
        return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands silently.'
    elif 'reversed' in args:
        return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands in reverse.'
    else:
        return True, ' > '+robot_name+' replayed ' + str(command_count) + ' commands.'


"""Parameters received are the temp_history, used as history list in do_replay_range(), and the num_range as two digits
separated by a dash.  This function changes the temp_history according to the desired range and returns the new temp_history."""
def get_range_nums(temp_history, num_range):
    global history

    temp_history = temp_history[int(num_range[1])-1:int(num_range[0])-1:]
    return temp_history


"""Parameters received are the temp_history, used as history list in do_replay_range(), and the num_range as one digit.
This function changes the temp_history according to the desired range and returns the new temp_history."""
def get_range_num(temp_history, num_range):
    global history
    
    temp_history = temp_history[len(history.get_history())-num_range::]
    return temp_history


"""This function receives args as a parameter.  Valid keywords are searched, removed and then re-appended into a list
so that the program knows exactly where which argument is in args.  This simplifies the implementation of flags later
in the program."""
def rearrange_command(args):
    global new_arg
    new_arg = []
    arg_list = args.lower().split(' ')
    if len(arg_list) > 0:

        for i in arg_list:
            if i.isdigit():
                arg_list.remove(i)
                new_arg.append(i)
        for i in arg_list:
            if i.find('-') and len(i.split('-')) == 2:
                for j in i.split('-'):
                    if j.isdigit():
                        is_digit = True
                    else:
                        is_digit = False
                if is_digit:
                    new_arg.append(i)

        if 'reversed' in arg_list:
            arg_list.remove('reversed')
            new_arg.append('reversed')
        if 'silent' in arg_list:
            arg_list.remove('silent')
            new_arg.append('silent')
    return new_arg


"""Handles a command by asking different functions to handle each command.
:param robot_name: the name given to robot
:param command: the command entered by user
:return: `True` if the robot must continue after the command, or else `False` if robot must shutdown"""
def handle_command(robot_name, command):
    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command == 'replay':
        (do_next, command_output) = do_replay(robot_name)
    elif command == 'replay silent':
        (do_next, command_output) = do_replay_silent(robot_name)
    elif command == 'replay reversed':
        (do_next, command_output) = do_replay_reversed(robot_name)
    elif command == 'replay reversed silent':
        (do_next, command_output) = do_replay_reversed_silent(robot_name)
    elif 'replay' or 'reversed' or 'silent' in command:
        (do_next, command_output) = do_replay_range(robot_name, arg)

    if is_replay_silent == False:
        print(command_output)
        if command != 'help':
            show_position(robot_name)
    return do_next


"""This is the entry point for starting my robot"""
def robot_start():
    global history
    global temp_history
    global is_replay_silent
    history = History()
    temp_history = []
    is_replay_silent = False

    global position_x, position_y, current_direction_index

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    history.track(command)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        history.track(command)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
