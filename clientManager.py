from client import Client

class ClientManager:
    def __init__(self):
        print("Init ClientManager ...")
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"Client {client.name} added successfully.")

    def display_client(self):
        if not self.clients:
            print("No clients found.")
            return
        for client in self.clients:
            client.disply_details()
    
    def remove_client(self, client_id):
        for client in self.clients:
            if client.id == client_id:
                self.clients.remove(client)
                print(f"Client with ID {client_id} removed successfully.")
                return
        print(f"Client with ID {client_id} not found.")
    
    def search_clients(self,name):
        print(f"Searching clients... name = {name}")
        for client in self.clients:
            if client.name == name:
                client.disply_details()
                return
        print(f"Client with ID {name} not found.")
    
    def update_client(self,client_id,name=None,email=None,phone=None):
        for client in self.clients:
            if client.id == client_id:
                if name:
                    client.name = name
                if email:
                    client.email = email
                if phone:
                    client.phone = phone
                print(f"Client with ID {client_id} updated successfully.")
                return
        print(f"Client with ID {client_id} not found.")