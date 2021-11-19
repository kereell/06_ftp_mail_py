#!/usr/bin/env python3
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print("Waiting for any incoming connections ...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input("Please enter the filename")
with open(filename, 'rb') as f:
    file_data = f.read(1024)
    conn.send(file_data)
