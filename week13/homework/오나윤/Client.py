import socket

from SocketLogger import SocketLogger as sLogger

def main():
    host = "127.0.0.1"
    port = 9000

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    try:
        while True:
            send_msg = input('\nMessage :') # block, try,catch, select([sys.stdin],,1)con.send("")

            #stop sending data
            if send_msg == 'quit':
                ans = input('\nDo you want to continue(y/n) :') #block
                if ans == 'y':
                    continue
                elif ans == 'n':
                    s.send("quit".encode('utf-8')) #server 소켓이 죽은 경우 처리
                    break
                else:
                    print("y or n")
                    continue
            s.send(send_msg.encode('utf-8')) #server 소켓이 죽은 경우 처리
            recv_msg = s.recv(1024)
            sLogger.logger.info('Received from the server :'+str(recv_msg.decode('utf-8')))
    except Exception as e:
        sLogger.logger.error(e)
    finally:
        s.close()

if __name__ == '__main__':
    main()
