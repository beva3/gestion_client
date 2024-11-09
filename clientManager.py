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