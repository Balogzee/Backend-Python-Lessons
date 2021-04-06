# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.

class Budget:
    """
    This is a Budget class
    """
    Budget_balance = [0,0,0] #Food, data, and clothing
    

    def __init__(self, category):
        self.category = category

        if (self.category == "1"):
            self.category == "Food"
        elif (self.category == "2"):
            self.category == "Data"
        elif (self.category == "3"):
            self.category == "Clothing"
        else:
            pass

        self.actions()

       
    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit"))
            print("Processing......................")
            amount += self.Budget_balance[self.category]
            self.Budget_balance[self.category] = amount
        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")
        


    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw"))
            print("Processing......................")
            if(self.Budget_balance[self.category] != 0 or amount < self.Budget_balance[self.category]):
                amount -= self.Budget_balance[self.category]
                self.Budget_balance[self.category] = amount

            else:
                print("Insufficient Funds!")
        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")


    def balance(self):
        pass
    def transfer(self):
        try:
            print("Choose budget to transfer from: ")
            print("1. Food")
            print("2. Data")
            print("3. Clothing")
            selection1 = int(input(": "))

            print("Choose budget to transfer to: ")
            print("1. Food")
            print("2. Data")
            print("3. Clothing")
            selection2 = int(input(": "))
            
            amount = int(input("Enter amount to transfer"))
            print("Processing......................")
            if(self.Budget_balance[self.category] != 0 or amount < self.Budget_balance[self.category]):
                amount -= self.Budget_balance[self.category]
                self.Budget_balance[self.category] = amount
            
            else:
                print("Insufficient Funds!")
        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")
        pass



    def actions(self):
        print("What would you like to do?:")
        print(f"1. Deposit to {self.category} Budget")
        print(f"2. Withdraw from {self.category} Budget")
        print(f"3. Check balance of {self.category} Budget")
        print("4. Transfer to another Budget")

        action = input(": ")

        if (action == "1"):
            self.deposit()

        elif(action == "2"):
            self.withdraw()

        elif(action == "3"):
            self.balance()

        elif(action == "4"):
            self.transfer()
        else:
            print("Invalid input")
            pass


    


def init():
    print("**********Welcome to MyBudget**********")
    print("Select from the budgets below:")
    print("1. Food")
    print("2. Data")
    print("3. Clothing")

    selection = input(": ")

    if (selection == "1"):
        budget = Budget(1)
    elif(selection == "2"):
        budget = Budget(2)
    elif(selection == "3"):
        budget = Budget(3)
    else:
        print("Invalid input")
        
    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or "Yes" or "y"):
        init()
    else:
        print("Thank you")