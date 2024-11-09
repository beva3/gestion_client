from client import Client

class ClientManager:
    def __init__(self):
        print("Init ClientManager ...")
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"Client {client.name} added successfully.")
