import time
import Authentication as auth
import pickle

localtime = time.asctime(time.localtime(time.time()))
userBalance = []
loaded_balance = pickle.load(open("Balance.txt", "rb"))
userBalance = loaded_balance
complaint = {}
loaded_complaint = pickle.load(open("Complaints.txt", "rb"))

def atm():
    print("****************************************")
    print(localtime)
    print("****************************************")

    auth.init()
    transactions()

    print("****************************************")
    print("Do you want to process another transaction? Y/N".title())
    response = input(":")
    if(response == "Y" or response == "Yes" or response == "y"):
        transactions()
    else:
        print("****************************************")
        print("Thank you for banking with us".title())
        print("****************************************")
        pickle.dump(auth.database, open("Database.txt", "wb"))
        pickle.dump(userBalance, open("Complaints.txt", "wb"))
        pickle.dump(complaint, open("Balance.txt", "wb"))
        exit()
        pass

def transactions():
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
        userBalance[auth.database.index(auth.accountNumber)] += depositAmount
        print("****************************************")
        print("Deposit completed".title())
        print("Balance: " + str(userBalance[auth.database.index(auth.accountNumber)]))
        
    elif(selectedOption == 2):
        print("****************************************")
        print("Withdarwal")
        print("How much would you like to withdraw?:".title())
        withdrawalAmount = int(input(":"))
        userBalance[auth.database.index(auth.accountNumber)] -= withdrawalAmount
        print("****************************************")
        print("Please Take your cash".title())
        print("Balance: " + str(userBalance[auth.database.index(auth.accountNumber)]))
        
    elif(selectedOption == 3):
        print("****************************************")
        print("Complaint")
        print("What issue will you like to report?:".title())
        complaint.update(auth.accountNumber, input(":"))
        print("****************************************")
        print("Complaint Issued\nThank you for contacting us".title())
        
    elif(selectedOption == 4):
        auth.logout()
        
    elif(selectedOption == 5):
        pickle.dump(auth.database, open("Database.txt", "wb"))
        pickle.dump(userBalance, open("Complaints.txt", "wb"))
        pickle.dump(complaint, open("Balance.txt", "wb"))
        exit()
    else:
      
        print("Invalid option selected, please try again".title())

    
atm()


