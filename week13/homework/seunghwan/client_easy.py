import select
import socket
import logging
import sys

from util import send_data_str, receive_data_str, set_logger


logger = logging.getLogger()

timeout = 10


def main():
    # AF_INET : domain name or IPv4 address
    # SOCK_STREAM : TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server 와 연결
    client_socket.connect(('localhost', 6000))

    # server 와 연결이 잘되었는지 결과 받기
    connection_msg = receive_data_str(client_socket)
    logger.info(connection_msg)

    std_input = [sys.stdin]

    while client_socket:
        # 명령어 인풋으로 받기
        print("\nenter command [get, put, close]: ")
        std_input, _, _ = select.select(std_input, [], [], 10)
        if not std_input:
            logger.warning(f'No input in for {timeout} seconds.')
            continue
        command = std_input[0].readline().lower().strip()
        if command not in ['get', 'put', 'close']:  # 명령어가 지원되지 않으면 에러
            logger.warning("Not support command yet.\nAvailable command is [get, put, close].\n")
            continue
        if command == 'close':
            client_socket.close()
            break

        print("enter key: ")
        std_input, _, _ = select.select(std_input, [], [], 10)
        if not std_input:
            logger.warning(f'No input in for {timeout} seconds.')
            continue
        key = std_input[0].readline().strip()
        value = None
        if command == 'put':
            print("enter value: ")
            std_input, _, _ = select.select(std_input, [], [], 10)
            if not std_input:
                logger.warning(f'No input in for {timeout} seconds.')
                continue
            value = std_input[0].readline()

        # server 로 데이터 전송
        send_data_str(client_socket, f'{command},{key},{value}')

        # 명령어 결과 받기
        response = receive_data_str(client_socket)
        logger.info(response)


if __name__ == '__main__':
    set_logger(logger)
    main()
