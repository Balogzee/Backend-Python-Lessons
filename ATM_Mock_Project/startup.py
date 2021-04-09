import pickle
database = {"1000000000": {"first_name":"e","last_name":"e","email":"e","password":"e"}}
user_balance={"1000000000":0}
complaint={"1000000000":"Nothing to report"}

pickle.dump(database, open("ATM_Mock_Project/Database.txt", "wb"))
pickle.dump(user_balance, open("ATM_Mock_Project/Balance.txt", "wb"))
pickle.dump(complaint, open("ATM_Mock_Project/Complaints.txt", "wb"))