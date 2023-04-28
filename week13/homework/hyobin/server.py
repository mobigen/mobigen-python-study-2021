import socket
from _thread import *
import pickle

#thread를 생성하는 threaded함수 구현
def threaded(client_socket,addr):
    print('Connected by :',addr[0],':',addr[1]) #addr[0]은 ip,addr[1]은 port

    while True:
        data = client_socket.recv(1024) #client가 보낸 메세지를 받아 data에 저장
        cmd = eval(data.decode('utf-8'))

        if not cmd:
            break
        
        if cmd[0] == 'put':
            stored[cmd[1]] = cmd[2]
            print('dict:' , stored)

        if cmd[0] == 'get':
            client_socket.send(stored[cmd[1]].encode())
        
        
        # client_socket.send(data) #client에 받은 데이터 재전송

    client_socket.close()


HOST='127.0.0.1'
PORT = 9999

#socket생성 후 listen상태 만들기
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((HOST,PORT))
server_socket.listen()

print('server start')

stored = dict()

while True:
    print('wait')

    client_socket,addr = server_socket.accept()
    start_new_thread(threaded(client_socket,addr))

server_socket.close()

