import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    
if __name__ == "__main__":
    number_guessing_game()
