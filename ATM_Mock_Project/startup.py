import pickle
database= {}
user_balance=[]
complaint={}

pickle.dump(database, open("Database.txt", "wb"))
pickle.dump(user_balance, open("Complaints.txt", "wb"))
pickle.dump(complaint, open("Balance.txt", "wb"))