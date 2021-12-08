import socket
hostname = input("Enter website address: ")
print(f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')