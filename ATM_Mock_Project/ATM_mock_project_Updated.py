#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random
import pickle
import time

localtime = time.asctime(time.localtime(time.time()))

class Bank():
    database = {"1000000000": {"first_name":"e","last_name":"e","email":"e","password":"e"}} #dictionary
    loaded_data = pickle.load(open("ATM_Mock_Project/Database.txt", "rb"))
    database = loaded_data

    accountNumbers = database.keys()

    
    #userBalance = {"1000000000":20000}
    loaded_balance = pickle.load(open("ATM_Mock_Project/Balance.txt", "rb"))
    userBalance = loaded_balance
    #complaint = {"1000000000":"Jesus"}
    loaded_complaint = pickle.load(open("ATM_Mock_Project/Complaints.txt", "rb"))
    complaint = loaded_complaint
    
    def __init__(self):
        pass



    def login(self):
        
        print("********* Login ************")

        self.accountNumber = input("What is your account number? \n")
        self.password = input("What is your password \n")

        for Keys,Values in self.database.items():
            
            if(self.accountNumber == Keys):
                if(self.password == Values["password"]):
                    self.bankOperation(Values, self.accountNumber)
                    return
                else:
                    print('Invalid account or password')
                    self.login()
            else:
                pass
                
                    
        
        


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

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %s" % self.accountNumber)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        self.login()

    def bankOperation(self, user, accountNumber):

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
            print("Deposit completed".title())
            print("Balance: " + str(self.userBalance[accountNumber]))
            
        elif(selectedOption == 2):
            print("****************************************")
            print("Withdarwal")
            print("How much would you like to withdraw?:".title())
            withdrawalAmount = int(input(":"))
            self.userBalance[accountNumber] -= withdrawalAmount
            print("****************************************")
            print("Please Take your cash".title())
            print("Balance: " + str(self.userBalance[accountNumber]))
            
        elif(selectedOption == 3):
            print("****************************************")
            print("Complaint")
            print("What issue will you like to report?:".title())
            input_complaint = input(":")
            self.complaint[accountNumber] = input_complaint
            print("****************************************")
            print("Complaint Issued\nThank you for contacting us")
            
        elif(selectedOption == 4):
            self.logout()
            
        elif(selectedOption == 5):
            pickle.dump(self.database, open("ATM_Mock_Project/Database.txt", "wb"))
            pickle.dump(self.userBalance, open("ATM_Mock_Project/Balance.txt", "wb"))
            pickle.dump(self.complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))
            exit()
        else:
        
            print("Invalid option selected, please try again".title()) 
        return

        


    def generationAccountNumber(self):

        return str(random.randrange(1000000000,9999999999))

    def logout(self):
        self.login()

#### ACTUAL BANKING SYSTEM #####
def atm():
    print("****************************************")
    print(localtime)
    print("****************************************")

    new_session = Bank()

    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        new_session.login()
    elif(haveAccount == 2):
        
        new_session.register()
    else:
        print("You have selected invalid option")
        atm()

    anotherTransaction = True
    while(anotherTransaction):
        print("****************************************")
        print("Do you want to process another transaction? Y/N".title())
        response = input(":")
        if(response == "Y" or response == "Yes" or response == "y"):
            # values = new_session.database.get(new_session.accountNumber)
            # print(values)
            # new_session.bankOperation(values, new_session.accountNumber)
            new_session.login()
        else:
            anotherTransaction = False
            print("****************************************")
            print("Thank you for banking with us".title())
            print("****************************************")
            pickle.dump(new_session.database, open("ATM_Mock_Project/Database.txt", "wb"))
            pickle.dump(new_session.userBalance, open("ATM_Mock_Project/Balance.txt", "wb"))
            pickle.dump(new_session.complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))
            exit()
            pass
        


atm()
