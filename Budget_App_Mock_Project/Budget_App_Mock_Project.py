class Budget:
    """
    This is a Budget class
    """
    Budget_balance = [0,0,0] #Food, data, and clothing
    Budgets = ["Food", "Data", "Clothing"]

    """
    To save the changes of the Budget_balance after each operation
    Another class can be created on another file 
    And the Budget Balances will be placed there
    Then you can import the file into this class
    And make any update to the Budget Balance from here
    """
    

    def __init__(self, category):
        self.category = category - 1


    def actions(self):
        print("************" * 3)
        print("What would you like to do?:")
        print(f"1. Deposit to {self.Budgets[self.category]} Budget")
        print(f"2. Withdraw from {self.Budgets[self.category]} Budget")
        print(f"3. Check balance of {self.Budgets[self.category]} Budget")
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
            print("************" * 3)
            print("Invalid input")
            pass

   
    def deposit(self):
        try:
            print("************" * 3)
            amount = int(input("Enter amount to deposit: \n"))
            print("Processing......................")
            self.Budget_balance[self.category] += amount
            print("************" * 3)
            print("Transaction Completed!")

        except ValueError as verr:
            print("************" * 3)
            print(f"Error: {verr}")
            print("Transaction failed")
        


    def withdraw(self):
        try:
            print("************" * 3)
            amount = int(input("Enter amount to withdraw: \n"))
            print("Processing......................")
            if(self.Budget_balance[self.category] != 0 or amount < self.Budget_balance[self.category]):
                self.Budget_balance[self.category] -= amount
                print("************" * 3)
                print("Transaction Completed!")

            else:
                print("************" * 3)
                print("Insufficient Funds!")

        except ValueError as verr:
            print("************" * 3)
            print(f"Error: {verr}")
            print("Transaction failed")


    def balance(self):
        print("************" * 3)
        print(f"You have {self.Budget_balance[self.category]} in your {self.Budgets[self.category]} Budget")
        print("************" * 3)
        print("Transaction Completed!")
        pass


    def transfer(self):
        try:
            print("************" * 3)
            print("Choose budget to transfer to: ")
            print("1. Food")
            print("2. Data")
            print("3. Clothing")
            selection = int(input(": "))
            
            if(selection <= 3):
                selection -= 1
                
                print("************" * 3)
                amount = int(input("Enter amount to transfer: \n"))
                        
                if(selection == self.category):
                    print("************" * 3)
                    print("Same account selected")
                    print("Transaction failed!")

                elif(self.Budget_balance[selection] != 0 or amount < self.Budget_balance[selection]):
                    print("************" * 3)
                    print("Processing......................")
                    self.Budget_balance[selection] -= amount
                    self.Budget_balance[(self.category - 1)] += amount

                    print("************" * 3)                        
                    print("Transaction Completed!")
                    
                else:
                    print("************" * 3)
                    print("Insufficient Funds!")

            else:
                print("*************" * 3)
                print("Invalid input")
                

        except ValueError as verr:
            print("************" * 3)
            print(f"Error: {verr}")
            print("Transaction failed")
        except IndexError as ierr:
            print("************" * 3)
            print(f"Error: {ierr}")
            print("Transaction failed")
        except:
            print("************" * 3)
            print("Error occured!")

    
    


def init():
    print("*********Welcome to MyBudget*********")
    print("Select from the budgets below:")
    print("1. Food")
    print("2. Data")
    print("3. Clothing")

    selection = input(": ")

    if (selection == "1"):
        budget = Budget(1)
        budget.actions()
    elif(selection == "2"):
        budget = Budget(2)
        budget.actions()
    elif(selection == "3"):
        budget = Budget(3)
        budget.actions()
    else:
        print("Invalid input")

    print("************" * 3)  
    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or retry == "Yes" or retry == "y" or retry == "yes"):
        init()
    else:
        print("************" * 3)
        print("Thank you")
        print("************" * 3)


init()