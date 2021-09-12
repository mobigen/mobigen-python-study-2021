import socket
import json
from _thread import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9879))
server.listen(3)
print("waiting connection")


def receive(connection):
    connection.send(bytes('Welcome to SERVER', 'utf-8'))
    try:
        while True:
            data = connection.recv(2048)
            data = json.loads(data.decode())
            if data:
                reply = "RETURN : OK"
            elif not data:
                reply = "RETURN : FINISHED"
                break
            print(f"GET [from {addr[1]}] : {data}")
            connection.sendall(bytes(reply, 'utf-8'))
            with open(f'./dump_file/{addr[1]}test.txt', 'w') as f:
                f.write(f"{json.dumps(data, indent=2)}")
    except:
        connection.close()    
        

while True:
    client, addr = server.accept()
    print(f"Connected to {str(addr[0])} : {str(addr[1])}")
    start_new_thread(receive, (client, ))
    
