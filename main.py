#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#import random
import random

#from replit import clear


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
    Function take the difficultu as parameter, and return the number of attemps user has
    """

    if answer == 'easy':
        return 10
    elif answer == 'hard':
        return 5
    else:
        return 5


#computer choose a random number between 1 and 100
number_to_guess = random.choice(range(1, 101))
print(number_to_guess)

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
        print("You ran out of attemps, you loose sorry")
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
