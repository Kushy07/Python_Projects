
from replit import clear
from art import logo



def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}



def calculator():
  print(logo)
  num1 = float(input("Enter the number: "))
  for _ in operations:
    print(_)
  
  op = input("Enter the operation: ")
  
  
  num2 = float(input("Enter next number: "))
  
  
  answer = operations[op](num1, num2)
  
  print(f"{num1} {op} {num2} = {answer}")
  
  end_of_program = False
  
  while not end_of_program:
    user_input = input('''Do you wanna continue? Type 'y' for 
     yes and 'n' for no.: ''')
  
    if user_input == 'n':
      end_of_program = True
      clear()
      calculator()
      
  
    else:
      new_op = input('Enter the operation: ')
      num3 = float(input("Enter the next number: "))
      new_answer = operations[new_op](answer, num3)
      print(f"{answer} {new_op} {num3} = {new_answer}")
      answer = new_answer

calculator()
