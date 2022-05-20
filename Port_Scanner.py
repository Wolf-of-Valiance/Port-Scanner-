#! usr/bin/python3

import socket
#Defining Values
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("Enter a website: ")
port = int(input("Enter a port: "))
IP = socket.gethostbyname(target)
results = sock.connect_ex((target,port))
#Initiate TCP Handshake
if sock.connect_ex((target,port)):
  print(results)
  #If Connection is Successful (socket.connect_ex returns the value of 0 if the TCP connection is recieved)
if results == 0:
    print("The port is open! ")
    print("The IP address of the website is: " + IP)
  #If connection is not resolved
else: 
    print("Connection was not established or blocked.")
