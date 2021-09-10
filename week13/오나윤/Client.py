import socket


def main():
    host = "127.0.0.1"
    port = 9000

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    while True:
        send_msg = input('\nMessage :')

        #stop sending data
        if send_msg == 'y':
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            elif ans == 'n':
                s.send("y".encode('utf-8'))
                break
            else:
                print("y or n")
                continue
        s.send(send_msg.encode('utf-8'))
        recv_msg = s.recv(1024)
        print('Received from the server :',str(recv_msg.decode('utf-8')))


    s.close()
if __name__ == '__main__':
    main()
