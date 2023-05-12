import random
from replit import clear
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_the_answer(guess, answer, lives):
  if guess > answer:
    print('To high 😱')
    return lives - 1
  elif guess < answer:
    print('To low 😭')
    return lives - 1
  else:
    print(f"You win 😃 answer is {answer}")


def set_difficulty():
  level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL


def game():
  print(logo)
  answer = random.randint(1, 100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")


  lives = set_difficulty()


  guess = 0
  while guess != answer:
    print(f"You have {lives} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))


    lives = check_the_answer(guess, answer, lives)
    if lives == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()