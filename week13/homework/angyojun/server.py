import socket
from _thread import *
import pickle
import json

ls = []
CONFIG = {
    'host': '127.0.0.1',
    'port': 8081,
    'encoding': 'utf-8',
    'save_file': 'ls.txt'
}


def put(arg, conn):
    ls.append(arg)
    print(ls)
    conn.send(bytes("ok", encoding=CONFIG['encoding']))


def get(arg, conn):
    result = json.dumps(ls)
    print(result)
    conn.send(result.encode(CONFIG['encoding']))


def save(arg, conn):
    with open(CONFIG['save_file'], "wb") as f:
        pickle.dump(ls, f)
    conn.send(bytes("ok", encoding=CONFIG['encoding']))


def client_thread(conn):
    command = {
        'put': put,
        'get': get,
        'save': save,
    }

    while True:
        data = str(
            conn.recv(1024),
            CONFIG['encoding']
        ).split(',')

        op = data[0]
        arg = {}
        if op == 'put':
            arg[data[1]] = data[2]

        command[data[0]](arg, conn)


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((CONFIG['host'], CONFIG['port']))
    sock.listen(5)

    while True:
        fd, address = sock.accept()
        start_new_thread(client_thread, (fd,))
    s.close()


if __name__ == '__main__':
    server()
