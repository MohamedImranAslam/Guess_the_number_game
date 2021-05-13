import random
from art import logo
print(logo)
easy_level = 10
hard_level = 5

def check_answer (guess,answer,turns):
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it, The answer is {guess}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
  if level == 'easy':
    return easy_level
  elif level == 'hard':
    return hard_level

def game():
  print("Welcome to number guessing game !!")
  answer = random.randint(1,100)


  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess a number")
    guess = int(input("Make a guess : "))
    turns = check_answer(guess,answer,turns)
    if turns == 0 :
      print("You  have run out of guesses, You lose")
      return

game()