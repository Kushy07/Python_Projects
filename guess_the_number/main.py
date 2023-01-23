from random import randint
from art import logo




print(logo)
print("Welcome to the guessing game.\nI am thinking of a number between 1 and 100.")
guess = randint(1,100)
# print(f'The number is {guess}')
user = input("Choose a difficulty: Type 'hard' or 'easy': ")
my_dict = {
  'hard': 5,
  'easy': 10
}

def check(attempt):
  if attempt > guess:
    print('Too high!')
  elif attempt < guess:
    print('Too low!')

  else:
    return 0
  

while my_dict[user] > 0:
  attempt = int(input(f"You have {my_dict[user]} attempt(s) to guess the number.  "))
  
  if check(attempt) == 0:
    print(f'Congrats! You got it! The number is {attempt}.')
    my_dict[user] = -1
  

  else:
    
    my_dict[user] -= 1
    if my_dict[user] == 0:
      print('You lose!')

