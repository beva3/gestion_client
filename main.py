from client import Client
from clientManager import ClientManager

# creat an instance of ClientManager
manager = ClientManager()

# client 
clients = [
    Client(1, "John Doe", "john.doe@example.com", "1234567890"),
    Client(2, "Jane Smith", "jane.smith@example.com", "0987654321"),
    Client(3, "Alice Johnson", "alice.johnson@example.com", "9876543210")  # duplicate id, this will cause an error
]

# add somme client
for client in clients:
    manager.add_client(client)

