import socket
from _thread import *
import pickle
import json
li = []

def save(con):
    with open("list.txt", "wb") as f:
        #result = json.dumps(li)
        #print(result)
        pickle.dump(li, f)

def client_thread(con):
    try:
        while True:
            data = con.recv(1024)
            str_data = str(data, 'utf-8')

            arg_data = str_data.split(",")
            command = arg_data[0]

            if str_data == 'y':
                break
            elif command == 'put':
                obj = {}
                key = arg_data[1]
                value = arg_data[2]
                obj[key] = value
                li.append(obj)
                print(li)
                con.send(bytes("ok", encoding ="utf-8"))
            elif command == 'get':
                result = json.dumps(li)
                print(result)
                con.send(result.encode("utf-8"))
            elif command == 'save':
                save(con)
                con.send(bytes("ok", encoding="utf-8"))
            else:
                print(str_data)
                con.send(data)
    except Exception as e:
        con.send(bytes("fail", encoding ="utf-8"))
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