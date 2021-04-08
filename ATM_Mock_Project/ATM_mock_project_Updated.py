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

database = {} #dictionary
loaded_data = pickle.load(open("Database.txt", "rb"))
database = loaded_data

accountNumber = 0
localtime = time.asctime(time.localtime(time.time()))
userBalance = {}
loaded_balance = pickle.load(open("Balance.txt", "rb"))
userBalance = loaded_balance
complaint = {}
loaded_complaint = pickle.load(open("Complaints.txt", "rb"))

def atm():
    print("****************************************")
    print(localtime)
    print("****************************************")

    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        atm()

    print("****************************************")
    print("Do you want to process another transaction? Y/N".title())
    response = input(":")
    if(response == "Y" or response == "Yes" or response == "y"):
        bankOperation(database[accountNumber])
    else:
        print("****************************************")
        print("Thank you for banking with us".title())
        print("****************************************")
        pickle.dump(database, open("Database.txt", "wb"))
        pickle.dump(userBalance, open("Complaints.txt", "wb"))
        pickle.dump(complaint, open("Balance.txt", "wb"))
        exit()
        pass
    

def login():
    
    print("********* Login ************")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[-1] == password):
                bankOperation(userDetails)
            else:
                print('Invalid account or password')
                login()
               
                
    
    


def register():

    print("****** Register *******")

    email = input("Enter email address: \n")
    first_name = input("Enter first name: \n")
    last_name = input("Enter last name: \n")
    password = input("Enter a password for your account: \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]
    print(database)

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    
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
        userBalance[database[accountNumber]] += depositAmount
        print("****************************************")
        print("Deposit completed".title())
        print("Balance: " + str(userBalance[database[accountNumber]]))
        
    elif(selectedOption == 2):
        print("****************************************")
        print("Withdarwal")
        print("How much would you like to withdraw?:".title())
        withdrawalAmount = int(input(":"))
        userBalance[database[accountNumber]] -= withdrawalAmount
        print("****************************************")
        print("Please Take your cash".title())
        print("Balance: " + str(userBalance[database[accountNumber]]))
        
    elif(selectedOption == 3):
        print("****************************************")
        print("Complaint")
        print("What issue will you like to report?:".title())
        input_complaint = input(":")
        complaint[database[accountNumber]] = input_complaint
        print("****************************************")
        print("Complaint Issued\nThank you for contacting us".title())
        
    elif(selectedOption == 4):
        logout()
        
    elif(selectedOption == 5):
        pickle.dump(database, open("Database.txt", "wb"))
        pickle.dump(userBalance, open("Complaints.txt", "wb"))
        pickle.dump(complaint, open("Balance.txt", "wb"))
        exit()
    else:
      
        print("Invalid option selected, please try again".title()) 

    


def generationAccountNumber():

    return random.randrange(1000000000,9999999999)

def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

atm()
