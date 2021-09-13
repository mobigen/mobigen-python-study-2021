import pickle
import socket
import struct
import logging

from typing import Union


def send_data(sock: socket.socket, data: Union[str, tuple]) -> None:
    """연결된 소켓으로 데이터를 보내는 함수
    먼저 4바이트로 데이터 길이를 보내고, 다음에 데이터를 전송

    :param sock: 연결된 소켓
    :param data: 보낼 데이터
    :return:
    """
    payload = pickle.dumps(data)
    sock.sendall(struct.pack('>I', len(payload)))  # first 4 bytes is length of payload
    sock.sendall(payload)  # real payload


def receive_data(sock: socket.socket) -> Union[str, tuple]:
    """소켓으로 전송된 데이터 받는 함수
    처음 4바이트로 데이터 길이 확인하고, 데이터 길이 만큼 들어올때까지 데이터 가져오기

    :param sock: 연결된 소켓
    :return: 문자열 or tuple 데이터
    """
    # 데이터 길이 확인
    total_len_of_payload = struct.unpack('>I', sock.recv(4))[0]

    remain_length_of_payload = total_len_of_payload
    received_payload = b''
    while remain_length_of_payload > 0:  # 데이터 길이만큼 가져올 때 까지 반복
        received_payload += sock.recv(remain_length_of_payload)
        remain_length_of_payload = total_len_of_payload - len(received_payload)
    # 가져온 데이터를 pickle 로 로드
    data = pickle.loads(received_payload)
    return data


def set_logger(logger: logging.Logger):
    # log level
    logger.setLevel(logging.INFO)

    # log message format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # to print at console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
