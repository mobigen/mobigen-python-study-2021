import socket
import select
import struct
import logging

from threading import Thread, Event
from typing import Dict, Tuple, Union

from util import send_data_str, receive_data_str, set_logger


logger = logging.getLogger()


server_data_buffer: Dict[str, str] = {}

ip = 'localhost'
port = 6000
timeout = 10


class DataPrinter(Thread):
    """현재 가지고 있는 데이터를 주기적으로 확인하기 위한 쓰레드"""
    def __init__(self):
        super().__init__()
        self._kill = Event()
        self._interval = 5

    def run(self) -> None:
        while True:
            logger.info(f"data buffer : {server_data_buffer}")

            # ctrl+c 가 들어오면 break
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break
        logger.info("Kill printing thread")

    def kill(self):
        self._kill.set()


def run_command(data: str) -> str:
    """명령어에 따른 동작을 수행하는 함수, 결과 메세지를 반환

    :param data: (명령어, 키) or (명령어, 키, 값)
    :return: message
    """
    command, key, value = data.split(',')
    command = command.strip().lower()

    if command == 'get':
        if key in server_data_buffer:  # 키가 있는 경우
            msg = server_data_buffer[key]
        else:
            msg = "Fail"
    elif command == 'put':
        server_data_buffer[key] = value
        msg = "OK"
    else:  # 아직 지원하지 않는 명령어
        msg = "Not support command yet." \
              " Available command is [get, put]."
    return msg


def main():
    logger.info(f"Starting Socket server with [{ip}, {port}]")
    # AF_INET : domain name or IPv4 address
    # SOCK_STREAM : TCP
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # ip, port 로 소켓 바인딩
    server_socket.bind((ip, port))
    # client 요청을 받을 준비
    server_socket.listen()
    logger.info(f"Server is Ready...")

    # 열린 소켓을 관리하기 위한 server socket
    socket_list = [server_socket]

    # socket 의 address 값을 저장하는 것
    client_address_mapper = {}

    # client 소켓에 대한 정보를 관리하기 위한 객체
    while True:
        # writing 은 하지 않기 때문에 무시
        read_socket_list, _, _ = select.select(socket_list, [], [], timeout)
        if not read_socket_list:
            logger.warning(f'No connection in for {timeout} seconds.')

        # readable socket 이 발생한 경우
        for readable_socket in read_socket_list:

            if readable_socket == server_socket:  # client 가 server 로 접속한 것
                client_socket, client_address = server_socket.accept()

                # 연결된 소켓을 관리 하기 위해서 저장
                socket_list.append(client_socket)

                # client 주소를 저장하기 위한 것으로, 필수 아님.
                client_address_mapper[client_socket] = client_address

                # 연결이 성공된 것을 클라이언트에게 알려준다
                msg = "The connection is established."
                send_data_str(client_socket, msg)

                # 로그로 기록
                logger.info(f"{msg} client: {client_address}")

            else:  # client 소켓에서 데이터가 왔을 때
                try:
                    # pickle loading 으로 데이터 가져오기
                    data = receive_data_str(sock=readable_socket)
                except struct.error:  # 데이터가 제대로 오지 않았을 경우, 클라이언트 소켓과 연결 삭제
                    logger.warning(f"We lost the connection with client: {client_address_mapper[readable_socket]}")
                    readable_socket.close()
                    socket_list.remove(readable_socket)
                    break

                logger.info(f"client: {client_address_mapper[readable_socket]}, command: {data}")

                # 명령어 결과 받기
                result_data = run_command(data)

                # 명령어 결과 클라이언트로 전송
                send_data_str(sock=readable_socket, data=result_data)


if __name__ == '__main__':
    set_logger(logger)
    t = DataPrinter()
    t.start()
    try:
        main()
    except KeyboardInterrupt as e:
        logger.error(e)
    except OSError as e:
        logger.error(e)
    finally:
        t.kill()
