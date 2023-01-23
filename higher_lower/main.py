from random import choice
from game_data import data
from art import vs
from art import logo
from replit import clear


def pick():
  return choice(data)

correct = 0
A = pick()
B = pick()


def check(A,B):
  if A['follower_count'] > B['follower_count']:
    return 1
  elif A['follower_count'] < B['follower_count']:
    return -1
  else:
    return 0
    
  

end_of_program = False


while not end_of_program:

  while A == B:
    pick(B)
  clear()
  print(logo)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  user = input(f"Against B: {B['name']}, a {B['description']}, from {B['country']}: ")
  clear()
  if user == 'A':
    if check(A,B) == 1:
      correct += 1
      print(f"You're right! Current score: {correct}")
      B = pick()
  
    else:
      print(f"Sorry! That's wrong. Final score: {correct}")
      end_of_program = True
  
  elif user == 'B':
    if check(A,B) == -1:
      correct += 1
      print(f"You're right! Current score: {correct}")
      A = B
      B = pick()
  
    else:
      print(f"Sorry! That's wrong. Final score: {correct}")
      end_of_program = True
    
