class Customer:
    """
    This is a customer Class
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def welcome(self):
        print(f"Welcome {self.name}")

Customer1 = Customer("Oluwaseun Balogun", "sda@gmail.com")
Customer2 = Customer("Jeremiah Joseph","sfda@yahoo.com")

Customer1.welcome()