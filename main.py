# Define a class to represent a mobile phone
class MobilePhone:
    # Constructor to initialize phone properties
    def __init__(self, brand, model, storage_capacity, price):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity 
        self.price = price 

    # Method to display all phone details
    def DisplayPhoneDetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage_capacity}GB")
        print(f"Price: ${self.price}")
        print()


#program that creates two phone objects and displays their info
phone1 = MobilePhone("Apple", "iPhone 16", 128, 999)
phone2 = MobilePhone("Samsung", "Galaxy S26", 256, 799)

phone1.DisplayPhoneDetails()
phone2.DisplayPhoneDetails()
