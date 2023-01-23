import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))



if user not in [1,2,0]:
  print('Not a valid number. You lose!')

else:
    my_list = [rock, paper, scissors]
    print(my_list[user])

    print('Computer chose:\n')

    rand = random.randint(0,2)

    print(my_list[rand])

    if user == rand:
      print('Tie! Hit refresh to play again!')
    elif user == 0:
      if rand == 1:
        print('You lose!')
      else:
        print('You win!')
    elif user == 1:
      if rand == 2:
        print('You lose!')
      else:
        print('You win!')

    elif user == 2:
      if rand == 0:
        print('You lose!')
      else:
        print('You win!')
