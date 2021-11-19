#!/usr/bin/env python3
import socket

s = socket.socket()
host = input("Please enter the host address of the sender: ")
port = 8080
s.connect((host, port))
print("Connected ...")

filename = input("Please, enter a name for the incoming file:")
with open(filename, "wb") as f:
    file_data = s.recv(1024)
    f.write(file_data)
    f.close()
    print("File has been recieved succussfully")
