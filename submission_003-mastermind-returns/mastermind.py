import random

"""Function that creates the 4 digit code, using random digits from 1 to 8. This code is being generated into a set
so that no doubles occur. Then it is transfered into a list and passed as a return value."""
def create_code():
    secret_code_set = set()
    while True:
        secret_code_set.add(random.randint(1, 8))
        if len(secret_code_set ) == 4:
            break
    secret_code_list = list(secret_code_set)
    return secret_code_list

"""Displays instructions to the user."""
def show_instructions():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

"""Show the results from one turn."""
def show_results(correct_digits_and_position, correct_digits_only):
    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))

"""Handle the logic of taking a turn, which includes:
    * get answer from user
    * check if answer is valid
    * check correctness of answer
"""
def take_turn(code):
    answer = input("Input 4 digit code: ")
    for digit in answer:
        if digit.isdigit() == False:
            take_turn(code)
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    show_results(correct_digits_and_position, correct_digits_only)

    return correct_digits_and_position

"""Show Code that was created to user."""
def show_code(code):
    print('The code was: '+str(code))

"""Checks correctness of answer and shows output to user."""
def check_correctness(correct, turns, correct_digits_and_position):
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: ' + str(12 - turns))
    return correct

"""This is the run game loop which makes it possible for the user to give multiple inputs.
This function also counts down the turns remaining using the turns variable. If the correct answer is guessed,
this function will trigger the congratulations message and terminate the run game loop."""
def run_game():
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_digits_and_position = take_turn(code)
        turns += 1
        correct = check_correctness(correct, turns, correct_digits_and_position)

    show_code(code)


if __name__ == "__main__":
    run_game()
