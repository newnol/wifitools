'''Website crawl basic program to find the IP address of a website'''
import socket
import pyfiglet
import requests

ascii_art = pyfiglet.figlet_format("Newnol Clolab")
print(ascii_art)

hostname = input("Enter website address: ")
print(f'The {hostname} IP Address is {socket.gethostbyname(hostname)}')

# Output
#find technology IP Address is
response = requests.get(f"https://api.hackertarget.com/httpheaders/?q={hostname}")
print(response.text)
