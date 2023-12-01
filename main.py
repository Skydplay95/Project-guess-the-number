#import random
import random

#import logo
from art import logo


#function guess
def guess(guess_attempt):
    """
    function take user guess as parameter, compare it to the number to find
    """
    if guess_attempt < number_to_guess:
        return "Too low"
    elif guess_attempt > number_to_guess:
        return "Too high"
    else:
        return user_guess


#function to determine number of attemps
def user_difficulty(answer):
    """
    Function take the difficulty as parameter, and return the number of attemps user has
    """

    if answer == 'easy':
        return 10
    elif answer == 'hard':
        return 5
    else:
        return 5


print(logo)

print(
    "Welcome to the guessing game, will you succeed to guess the random number ?"
)
print("The number to guess is between 1 and 100.")

#computer choose a random number between 1 and 100
number_to_guess = random.choice(range(1, 101))

#user choose difficultys
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attemps = user_difficulty(difficulty)
#print amount of user attemps giving the difficulty choosen
print(f"You have {attemps} remaing to guess right")

game_end = False
#while loop to make multiple guess
while not game_end:

    #user make a guess
    user_guess = int(input("Make a guess: "))
    print(guess(user_guess))

    #if user guess attemps fall to 1, one more attemps and it's over
    if attemps == 1:
        print(f"You ran out of attemps,the number was {number_to_guess}, you loose sorry")
        game_end = True
    #if user guess is wrong, minus 1 attempts
    elif guess(user_guess) != number_to_guess:
        attemps -= 1
        print(f"You have {attemps} remaining to guess right")
        print("Guess again")
        #if user has no more attempts, game end
    else:
        #user guess it right
        print(f"You guess it right, the number was {number_to_guess}")
        #clear()
        game_end = True
