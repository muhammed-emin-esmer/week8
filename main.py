import random   

number = random.randint(1, 10)
guess = 0
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts - 1

    if guess == number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Too bad! Try again.")

    print(f"You have {attempts} attempts left.")

if guess != number:
    print(f"Sorry, you've run out of attempts. The correct number was {number}.")
