import socket
import sys
from typing import Any
import pickle

HOST='127.0.0.1'
PORT=9999


#socket 생성
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'quit':
        break

    if cmd[0] == 'put':
        data = str(cmd).encode()
        client_socket.send(data)

    # client_socket.send(message.encode())
    if cmd[0] == 'get':
        data = str(cmd).encode()
        client_socket.send(data)

        data = client_socket.recv(1024)
        print(data.decode())

    # print('received from the server:',repr(data.decode()))

client_socket.close()

