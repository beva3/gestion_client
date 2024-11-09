class Client:
    def __init__(self,id,name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def disply_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}")