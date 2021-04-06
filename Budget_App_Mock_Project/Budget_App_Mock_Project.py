class Budget:
    """
    This is a Budget class
    """
    Budget_balance = [0,0,0] #Food, data, and clothing
    Budgets = ["Food", "Data", "Clothing"]
    

    def __init__(self, category):
        self.category = category - 1


    def actions(self):
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
            print("Invalid input")
            pass

   
    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: \n"))
            print("Processing......................")
            self.Budget_balance[self.category] += amount
            print("Transaction Completed!")

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")
        


    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: \n"))
            print("Processing......................")
            if(self.Budget_balance[self.category] != 0 or amount < self.Budget_balance[self.category]):
                self.Budget_balance[self.category] -= amount
                print("Transaction Completed!")

            else:
                print("Insufficient Funds!")

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")


    def balance(self):
        print(f"You have {self.Budget_balance[self.category]} in your {self.Budgets[self.category]} Budget")
        print("Transaction Completed!")
        pass


    def transfer(self):
        try:
            
            print("Choose budget to transfer to: ")
            print("1. Food")
            print("2. Data")
            print("3. Clothing")
            selection = int(input(": "))
            
            if(selection <= 3):
                selection -= 1

                amount = int(input("Enter amount to transfer: \n"))
                        
                if(selection == (self.category-1)):
                    print("Same account selected")
                    print("Transaction failed!")

                elif(self.Budget_balance[selection] != 0 or amount < self.Budget_balance[selection]):
                    print("Processing......................")
                    self.Budget_balance[selection] -= amount
                    self.Budget_balance[(self.category - 1)] += amount
                                            
                    print("Transaction Completed!")
                    
                else:
                    print("Insufficient Funds!")

            else:
                print("Invalid input")
                

        except ValueError as verr:
            print(f"Error: {verr}")
            print("Transaction failed")
        except IndexError as ierr:
            print(f"Error: {ierr}")
            print("Transaction failed")
        except:
            print("Error occured!")

    
    


def init():
    print("**********Welcome to MyBudget**********")
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

        
    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or retry == "Yes" or retry == "y" or retry == "yes"):
        init()
    else:
        print("Thank you")


init()