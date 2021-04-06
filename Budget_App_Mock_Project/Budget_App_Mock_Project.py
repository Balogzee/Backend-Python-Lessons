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
    Budgets = {"Food": {"Balance":0},"Data":{"Balance":0},"Clothing":{"Balance":0}}

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

        print("What would you like to do?:")
        print(f"1. Deposit to {self.category} Budget")
        print(f"2. Withdraw from {self.category} Budget")
        print(f"3. Balance of {self.category} Budget")
        print("4. Transfer to another Budget")

        action = input(": ")

    def deposit(self):
        pass


def init():
    print("**********Welcome**********")
    print("Select from the options below:")
    print("1. Food")
    print("2. Data")
    print("3. Clothing")

    selection = input(": ")

    if (selection == 1):
        budget = Budget(1)
    elif(selection == 2):
        budget = Budget(2)
    elif(selection == 3):
        budget = Budget(3)
    else:
        print("Invalid input")
        
    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or "Yes" or "y"):
        init()
    else:
        print("Thank you")