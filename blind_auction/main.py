from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
end_of_program = False
bidding_dict = {}
def calculate_bidding(bid_dict):
  my_list = []
  for key in bid_dict:
    my_list.append(bid_dict[key])
  highest_bid = max(my_list)
  for key in bid_dict:
     if bid_dict[key] == highest_bid:
       print(f'And the winner is {key} who bid ${bid_dict[key]}')
  
  
while not end_of_program:
  key = input('What is your name? ')
  value = input("What's your bid? $")
  bidding_dict[key] = value
  
  user = input("Do you want to continue? 'yes' or 'no'? ")
  if user == 'no':
    end_of_program = True
    calculate_bidding(bidding_dict)
  elif user == 'yes':
    calculate_bidding(bidding_dict)
    clear()

  else:
    print('Please enter a valid answer')
  
