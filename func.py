import random

def user_feedback(secret_number, guess):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "too low"
    else:
        return "too high"

def computer_guess(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # You can choose any range
    
    lower_bound = 1
    upper_bound = 100
    
    while True:
        computer_guess_num = computer_guess(lower_bound, upper_bound)
        print(f"Computer guesses: {computer_guess_num}")
        
        feedback = user_feedback(secret_number, computer_guess_num)
        print(f"User says: {feedback}")
        
        if feedback == "correct":
            print("Computer guessed the correct number! Game Over.")
            break
        elif feedback == "too low":
            lower_bound = computer_guess_num + 1
        else:
            upper_bound = computer_guess_num - 1

