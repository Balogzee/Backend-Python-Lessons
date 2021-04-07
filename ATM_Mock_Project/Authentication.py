#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random
import pickle

database = {} #dictionary
loaded_data = pickle.load(open("Database.txt", "rb"))
database = loaded_data

accountNumber = 0

def init():
    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    
    print("********* Login ************")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
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

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    return 

    


def generationAccountNumber():

    return random.randrange(1000000000,9999999999)

def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

init()
