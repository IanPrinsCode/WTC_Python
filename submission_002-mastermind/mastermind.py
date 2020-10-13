import random

def generate_secret_code():
    secret_code_set = set()
    while True:
        secret_code_set.add(random.randint(1, 8))
        if len(secret_code_set ) == 4:
            break
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    secret_code_list = list(secret_code_set)
    return secret_code_list

def get_input():
    digits = input("Input 4 digit code: ")
    while ("0" in digits or "9" in digits) or (digits.isdigit() != True) or len(digits) != 4:
        if len(digits) != 4:
            print("Please enter exactly 4 digits.")
            digits = input("Input 4 digit code: ")
        else:
            digits = input("Input 4 digit code: ")
    dig_list = []
    for dig in digits:
        dig_list.append(int(dig))
    return dig_list

def evaluate_input(secret_code, answer_code, guesses):
    if secret_code == answer_code:
        do_correct_answer(secret_code)
    else:
        guesses -= 1
        do_wrong_answer(secret_code, answer_code, guesses)
    return guesses


def do_correct_answer(secret_code):
    print("Number of correct digits in correct place:     4")
    print("Number of correct digits not in correct place: 0")
    print("Congratulations! You are a codebreaker!")
    print("The code was: ", end="")
    for i in range(0, 4):
        print(secret_code[i], end="")

def do_wrong_answer(secret_code, answer_code, guesses):
    cor_dig = 0
    cor_dig_spot = 0
    for y in range(len(secret_code)):
        for x in range(len(answer_code)):
            if secret_code[y] == answer_code[x] and x == y:
                cor_dig_spot += 1
            if secret_code[y] == answer_code[x] and x != y:
                cor_dig += 1
    print("Number of correct digits in correct place:     " + str(cor_dig_spot))
    print("Number of correct digits not in correct place: " + str(cor_dig))
    print("Turns left: " + str(guesses))

def run_game():
    """
    TODO: implement Mastermind code here
    """
    guesses = 12
    secret_code = generate_secret_code()
    # print(secret_code)
    answer_code = 0 
    while guesses != 0:
        if answer_code != secret_code:
            answer_code = get_input()
        guesses = evaluate_input(secret_code, answer_code, guesses)
        if answer_code == secret_code:
            break


if __name__ == "__main__":
    run_game()
