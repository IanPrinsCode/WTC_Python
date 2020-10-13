import random

answer = ""
turns = 0
correct = False
correct_digits_and_position = 0
correct_digits_only = 0
code = []

"""Create secret code that must be guessed by user."""
def generate_code():
    global code

    code_set = set()
    while True:
        code_set.add(random.randint(1, 8))
        if len(code_set) == 4:
            break
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    code = list(code_set)


"""Ask and receive user input into answer variable.
This function also tests if the input is the right length and in the right format(digits)."""
def get_input():
    global answer

    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        get_input()
    if not answer.isdigit():
        get_input()

"""This funtion matches input with secret code and formulates a response."""
def evaluate_input():
    global correct_digits_and_position
    global correct_digits_only

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))

"""This is the run game loop which makes it possible for the user to give multiple inputs.
This function also counts down the turns remaining using the turns variable. If the correct answer is guessed,
this function will trigger the congratulations message and terminate the run game loop."""
def run_game():
    global correct
    global turns

    turns = 0
    correct = False
    generate_code()
    # print(code)
    while not correct and turns < 12:
        get_input()
        evaluate_input()
        turns += 1
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
