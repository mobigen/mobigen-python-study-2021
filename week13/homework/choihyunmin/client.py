import socket
import json


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9879))
print("Success connection")

response = client.recv(1024)
d = dict()


try:
    while True:
        data = input("Please input data (Example : PUT A B) :").split()
        if data[0].lower() == 'put':
            d[data[1]] = data[2]
        elif data[0] == 'finish':
            print("client finished")
            break
        elif not data:
            break
        send_data = json.dumps(d)
        client.send(send_data.encode())
        response = client.recv(1024)
        print(response.decode())

finally: 
    client.close()