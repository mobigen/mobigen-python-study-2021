import socket

CONFIG = {
    'host': '127.0.0.1',
    'port': 8081,
    'encoding': 'utf-8',
}


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CONFIG['host'], CONFIG['port']))

    while True:
        msg = input('\nMessage :')

        if msg:
            answer = input('\nsend? (y/n)')
            if answer == 'y':
                continue
            elif answer == 'n':
                no = "y".encode(CONFIG['encoding'])
                sock.send(no)
                break
            else:
                continue

        sock.send(msg.encode(CONFIG['encoding']))
        print('receive :', str(sock.recv(1024).decode(CONFIG['encoding'])))
    sock.close()

if __name__ == '__main__':
    client()