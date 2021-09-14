import json
import socket
import threading

server_dict = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 10002))
server_socket.listen(5)

def t_server(client_socket, data):
    global server_dict
    try:
        key = list(json.loads(data).keys())[0]
        val = json.loads(data)
        if key == 'put':
            try:
                server_dict = dict(server_dict, **val['put'])
                client_socket.send('Ok'.encode())
            except Exception:
                client_socket.send('Fail'.encode())

        elif key == 'get':
            put_value = json.dumps({'result': server_dict[val['get']]}).encode('utf-8')
            client_socket.sendall(put_value)

    except Exception as e:
        print(e)
        client_socket.close()

if __name__ == "__main__":

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        threading.Thread(target=t_server, args=(client_socket, data, )).start()
