class User():
    def __init__(self, name, address, phone_number,):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.borrowed_books = []

    def user_info(self):
        print(f'Name: {self.name}')
        print(f'address: {self.address}')
        print(f'Phone Number: {self.phone_number}')

#may need to change borrow_books value or set it inside the parameters