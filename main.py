from client import Client
from clientManager import ClientManager

# creat an instance of ClientManager
manager = ClientManager()

# client 
clients = [
    Client(1, "John Doe", "john.doe@example.com", "1234567890"),
    Client(2, "Jane Smith", "jane.smith@example.com", "0987654321"),
    Client(3, "Alice Johnson", "alice.johnson@example.com", "9876543210"), 
    Client(4, "Dupont", "dupont@example.com", "0123456789"), 
    Client(5, "Martin", "martin@example.com", "0123456790"),
    Client(6, "Durand", "durand@example.com", "0123456791"), 
    Client(7, "Lefevre", "lefevre@example.com", "0123456792"), 
    Client(8, "Moreau", "moreau@example.com", "0123456793")
]

# add somme client
for client in clients:
    manager.add_client(client)
# display all clients
manager.display_client()

# remove a client if id is even
for client in clients:
    if client.id % 2 == 0:
        manager.remove_client(client.id)

# display client
manager.display_client()

