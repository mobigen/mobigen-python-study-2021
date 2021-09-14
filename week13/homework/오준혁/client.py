import json
import socket
import sys

def socket_func(cmd, args):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 10002))
    if cmd.lower() == 'put':
        put_value = json.dumps({cmd: {args[0]: args[1]}}).encode('utf-8')
        client_socket.sendall(put_value)
        print(client_socket.recv(1024).decode('utf-8'))

    elif cmd.lower() == 'get':
        get_value = json.dumps({cmd: args[0]}).encode('utf-8')
        client_socket.sendall(get_value)
        print(client_socket.recv(1024).decode('utf-8'))

if __name__ == "__main__":
    socket_func(sys.argv[1], sys.argv[2:])
