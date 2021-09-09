import socket
from _thread import *
import pickle
li = []

def save(con):
    with open("list.txt", "wb") as f:
        send_data = ",".join(li)
        print(send_data)
        con.send(send_data.encode("utf-8"))
        pickle.dump(send_data, f)

def client_thread(con):
    try:
        while True:
            data = con.recv(1024)
            str_data = str(data, 'utf-8')

            if str_data == 'y':
                break
            elif 'put' in str_data[0:3]:
                li.append(str_data.split(" ")[1])
                print(li)
                con.send(data)
            elif 'get' in str_data[0:3]:
                send_data = ",".join(li)
                print(send_data)
                con.send(send_data.encode("utf-8"))
            elif 'save' in str_data[0:4]:
                save(con)
            else:
                print(str_data)
                con.send(data)
    except Exception as e:
        print("close")

def main():
    host = "127.0.0.1"
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("socket is listening")

    while True:
        con, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        start_new_thread(client_thread, (con,))
    s.close()

if __name__ == '__main__':
    main()
