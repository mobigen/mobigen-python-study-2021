import socket
import logging

from util import send_data, receive_data, set_logger


logger = logging.getLogger()


def main():
    # AF_INET : domain name or IPv4 address
    # SOCK_STREAM : TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server 와 연결
    client_socket.connect(('localhost', 6000))

    # server 와 연결이 잘되었는지 결과 받기
    connection_msg = receive_data(client_socket)
    logger.info(connection_msg)

    while client_socket:
        # 명령어 인풋으로 받기
        command = input("\nenter command [get, put, close]: ").lower().strip()
        if command not in ['get', 'put', 'close']:  # 명령어가 지원되지 않으면 에러
            logger.warning("Not support command yet.\nAvailable command is [get, put, close].\n")
            continue
        if command == 'close':
            client_socket.close()
            break

        key = input("enter key: ").strip()
        value = None
        if command == 'put':
            value = input("enter value: ")

        # server 로 데이터 전송
        send_data(client_socket, (command, key, value))

        # 명령어 결과 받기
        response = receive_data(client_socket)
        logger.info(response)


if __name__ == '__main__':
    set_logger(logger)
    main()
