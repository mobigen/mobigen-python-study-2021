import socket
from ServerSocket import ServerSocket
from SocketLogger import SocketLogger as sLogger

dic = {}

def main():
    host = "127.0.0.1"
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    sLogger.logger.info("socket is listening")

    try:
        while True:
            con, addr = s.accept()
            sLogger.logger.info('Connected to :'+str(addr[0])+':'+str(addr[1]))
            socket_thread = ServerSocket(con,dic)
            socket_thread.start()
    except Exception as e:
        sLogger.logger.error(e)
    finally:
        s.close()

if __name__ == '__main__':
    main()