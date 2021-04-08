import time

localtime = time.asctime(time.localtime(time.time()))
userNames = ["Seun", "Joy", "Ife"]
userPassword = ["Seun", "Joy", "Ife"]
userBalance = [20000, 30000, 50000]
complaint = []

def atm():
    print("****************************************")
    print(localtime)
    print("****************************************")

    print("Hello there!".title())
    name = input("Please Enter Your Name: \n".title())
    if(name in userNames):
        password = input("Enter Password: \n".title())
        if(password == userPassword[userNames.index(name)]):
            print("****************************************")
            print("Welcome, " + str(name))
            print("Please Select An Option".title())
            print("1. Withdrawal")
            print("2. Deposit")
            print("3. Complaint:")
            
            selectedOption = int(input(":"))

            if(selectedOption == 1): #Withdrawal
                print("****************************************")
                print("Withdarwal")
                print("How much would you like to withdraw?:".title())
                withdrawalAmount = int(input(":"))
                userBalance[userNames.index(name)] -= withdrawalAmount
                print("****************************************")
                print("Please Take your cash".title())
                print("Balance: " + str(userBalance[userNames.index(name)]))
                
            elif(selectedOption == 2): #Deposit
                print("****************************************")
                print("Deposit")
                print("How much would you like to deposit:".title())
                depositAmount = int(input(":"))
                userBalance[userNames.index(name)] += depositAmount
                print("****************************************")
                print("Deposit completed".title())
                print("Balance: " + str(userBalance[userNames.index(name)]))

            elif(selectedOption == 3): #Complaint
                print("****************************************")
                print("Complaint")
                print("What issue will you like to report?:".title())
                complaint.append(input(":"))
                print("****************************************")
                print("Thank you for contacting us".title())

            else:
                print("Invalid Option Selected, please try again".title())

        else:
            print("Password Incorrect, please try again".title())

    else:
        print("No name found, please try again".title())

    print("****************************************")
    print("Do you want to process another transaction? Y/N".title())
    response = input(":")
    if(response == "Y" or response == "Yes" or response == "y"):
        atm()
    else:
        print("****************************************")
        print("Thank you for banking with us".title())
        print("****************************************")
        pass

atm()