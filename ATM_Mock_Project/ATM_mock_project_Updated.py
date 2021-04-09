import random
import pickle
import time

localtime = time.asctime(time.localtime(time.time()))

class Bank():
    """
    This is a Bank class, which carries out banking transactions
    """

    database = {"1000000000": {"first_name":"e","last_name":"e","email":"e","password":"e"}} #dictionary
    loaded_data = pickle.load(open("ATM_Mock_Project/Database.txt", "rb"))
    database = loaded_data

    loaded_balance = pickle.load(open("ATM_Mock_Project/Balance.txt", "rb"))
    userBalance = loaded_balance
    
    loaded_complaint = pickle.load(open("ATM_Mock_Project/Complaints.txt", "rb"))
    complaint = loaded_complaint
    
    def __init__(self):
        pass


    def login(self):
        number_of_attempts  = 1
        while(number_of_attempts < 4):
            print("********* Login ************")

            self.accountNumber = input("What is your account number? \n")
            self.password = input("What is your password \n")
        
            if(self.accountNumber in self.database):

                if(self.password == self.database[self.accountNumber]["password"]):
                    self.bankOperation(self.database[self.accountNumber], self.accountNumber)
                    number_of_attempts = 5

                else:
                    print("****************************************")
                    print('Invalid account or password')
                    print(f'Number of tries left: {3-number_of_attempts}')
                    number_of_attempts += 1
                    
            else:
                print("****************************************")
                print('Invalid account or password')
                print(f'Number of tries left: {3-number_of_attempts}')
                number_of_attempts += 1
                pass
        
        if (number_of_attempts == 4):
            time.sleep(1)
            print("****************************************")
            print("You have exceeded the number of tries")
            wait = 1
            while(wait <16):
                print(f"Wait for {16-wait}secs") #15secs is used to test, time can be increased to 1min
                time.sleep(1)
                wait += 1
                
                    
    def register(self):

        print("****** Register *******")

        self.email = input("Enter email address: \n")
        self.first_name = input("Enter first name: \n")
        self.last_name = input("Enter last name: \n")
        self.password = input("Enter a password for your account: \n")

        self.accountNumber = self.generationAccountNumber()

        self.database[self.accountNumber] = { "first_name":self.first_name, "last_name":self.last_name, "email":self.email, "password":self.password }
        self.userBalance[self.accountNumber] = 0
        self.complaint[self.accountNumber] = ""
        pickle.dump(self.database, open("ATM_Mock_Project/Database.txt", "wb"))
        pickle.dump(self.userBalance, open("ATM_Mock_Project/Balance.txt", "wb"))
        pickle.dump(self.complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))

        time.sleep(1)
        print("Your Account Has been created")
        print("****************************************")
        print("Your account number is: %s" % self.accountNumber)
        print("Make sure you keep it safe")
        print("Redirecting to login....................")
        print("****************************************")
        time.sleep(3)

        self.login()

    
    def bankOperation(self, user, accountNumber):
        print("****************************************")

        print("Welcome %s %s " % ( user["first_name"], user["last_name"] ) )
        
        print("Please Select An Option:")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Complaint")
        print("4. Logout")
        print("5. Exit: \n")
        selectedOption = int(input())

        if(selectedOption == 1):
            print("****************************************")
            print("Deposit")
            print("How much would you like to deposit:".title())
            depositAmount = int(input(":"))
            self.userBalance[accountNumber] += depositAmount
            print("****************************************")
            time.sleep(1)
            print("Deposit completed".title())
            print("Balance: " + str(self.userBalance[accountNumber]))
            
        elif(selectedOption == 2):
            print("****************************************")
            print("Withdarwal")
            print("How much would you like to withdraw?:".title())
            withdrawalAmount = int(input(":"))
            if (withdrawalAmount < self.userBalance[accountNumber]):
                self.userBalance[accountNumber] -= withdrawalAmount
                print("****************************************")
                time.sleep(1)
                print("Please Take your cash".title())
                print("Balance: " + str(self.userBalance[accountNumber]))
            else:
                print("****************************************")
                print("Insufficient Funds!")
            
        elif(selectedOption == 3):
            print("****************************************")
            print("Complaint")
            print("What issue will you like to report?:".title())
            input_complaint = input(":")
            self.complaint[accountNumber] = input_complaint
            print("****************************************")
            time.sleep(1)
            print("Complaint Issued\nThank you for contacting us")
            
        elif(selectedOption == 4):
            self.logout()
            
        elif(selectedOption == 5):
            pickle.dump(self.database, open("ATM_Mock_Project/Database.txt", "wb"))
            pickle.dump(self.userBalance, open("ATM_Mock_Project/Balance.txt", "wb"))
            pickle.dump(self.complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))
            exit()
        else:
            print("****************************************")
            print("Invalid option selected, please try again".title()) 

        
    def generationAccountNumber(self):

        return str(random.randrange(1000000000,9999999999))

    
    def logout(self):
        time.sleep(1)
        self.login()



#### ACTUAL BANKING SYSTEM #####
def atm():
    print("****************************************")
    print(localtime)
    print("****************************************")

    new_session = Bank()

    time.sleep(1)
    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        new_session.login()
    elif(haveAccount == 2):
        
        new_session.register()
    else:
        print("****************************************")
        print("You have selected invalid option")
        atm()

    anotherTransaction = True
    while(anotherTransaction):
        time.sleep(1)
        print("****************************************")
        print("Do you want to process another transaction? Y/N".title())
        response = input(":")
        if(response == "Y" or response == "Yes" or response == "y"):
            new_session.login()
        else:
            anotherTransaction = False
            time.sleep(1)
            print("****************************************")
            print("Thank you for banking with us".title())
            print("****************************************")
            pickle.dump(new_session.database, open("ATM_Mock_Project/Database.txt", "wb"))
            pickle.dump(new_session.userBalance, open("ATM_Mock_Project/Balance.txt", "wb"))
            pickle.dump(new_session.complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))
            exit()
            pass
        


atm()
