#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print (logo)
print("Welcome to the number guessing game")
print("I'm thinking a number between 1 to 100")
answer = random.randint(1, 100)
print(f"Passt. The correct number is {answer}")
level = input("Choose a difficultity. Type 'easy' or 'hard'?")

max_attempts = 0
if level == 'easy':
  max_attempts = 10
else:
  max_attempts = 5

current_attempts = max_attempts
end = False
while not end:
  print(f"You have {current_attempts} remaining to guess the number")
  guess = int(input("Make a guess: "))
  
  if guess == answer:
    end = True
    print(f"You got it. The answer is {answer}")
  elif guess < answer:
    print("Too low")
    current_attempts -= 1
  else:
    print("Too high")
    current_attempts -= 1