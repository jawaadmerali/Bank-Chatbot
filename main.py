
def init_chat():

  account_creation = input("Welcome! How are you today? \n(Click q to leave at any time)\n")
  if account_creation == "q":
    quit()


def username():
  user_firstname = input("To get started, let us create an account. Enter your first name \n")
  if user_firstname == "q":
    quit()
  user_lastname = input("Enter your last name \n")
  if user_lastname == "q":
    quit()
  print("Hi " + user_firstname + " " + user_lastname +  " Let us know pick an account best for you")

def account():
  account_choice = input("\n We have multiple account options for you! \n Would you like an account to help you save money? \n (Enter - savings) \n \n Would you like to manage your withdrawls and deposit? \n (Enter - manage money)\n \n Would you like an account to manage your expenses to see how much \n money you will have left? \n (Enter - expenses) \n \n")
  while account_choice != "savings" and account_choice!="manage money" and account_choice != "expenses":
    print("That is not a valid entry. Enter either (savings), (expenses) or (manage money) ")
    account_choice = input("\n We have multiple account options for you! \n Would you like an account to help you save money? \n (Enter - savings) \n \n Would you like to manage your withdrawls and deposit? \n (Enter - manage money)\n \n Would you like an account to manage your expenses to see how much \n money you will have left? \n (Enter - expenses) \n \n")


  if account_choice == "expenses":
    expense = int(input("Enter how much total money you have in your account (Only numbers)$ "))
    expense_house = int(input("Enter the total amount of any mortgage expenses $ (Only numbers)"))
    expense_food = int(input("Enter the total amount of any food expenses $ (Only numbers)"))
    expense_leisure = int(input("Enter the total amount of any leisure expenses $ (Only numbers)"))
    expense_utility = int(input("Enter the total amount of any utility expenses $ (Only numbers)"))
    expense_school = int(input("Enter the total amount of any school expenses $ (Only numbers)"))
    expense_insurance = int(input("Enter the total amount of any insurance expenses $ (Only numbers)"))
    expense_other = int(input("Enter any other expenses $ (Only numbers)"))
    expense_total =expense_house+expense_food+expense_leisure+expense_utility+expense_school+expense_insurance + expense_other
    print("Based on all your expenses, you have $ " + str(expense-expense_total) + " left to spend in your account")
    print("\n Run again to restart")
    quit()


  if account_choice == "q":
    quit()
  if account_choice == "savings":
    account = int(input("Enter how much money you make annualy $ "))
    calc_saving = account*0.15
    print("Based on the 15% recommended savings, you should save " + str(calc_saving) + " $")
    print(" \n Run again to restart")
    quit()
  if account_choice == "manage money":        
    money = int(input("How much money do you have? $ "))
    
  withdraw_deposit = input("Would you like to withdraw or deposit money? ")
  if withdraw_deposit == "deposit":
    deposit = int(input("How much money would you like to deposit in dollars? $ "))    
    print("Your deposit was successful. You now have " + str(money+deposit) + " dollars in your account")
    print("\n If you would like to start again, restart")
    quit()

  if withdraw_deposit == "withdraw":
    much_withdraw = int(input("How much money would you like to withdraw in dollars? $ "))
  if much_withdraw > money:
      print("You do not have that much money in your account to withdraw")
      quit()
  else:
      print("Your withdrawl was successful. You now have " + str(money-much_withdraw) + " dollars in your account")
      print("\n If you would like to start again, restart")
      quit()


    

if __name__ == "__main__":
  init_chat()
  username()
  account()






