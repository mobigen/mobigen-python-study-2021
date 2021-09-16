from threading import Thread
import pickle
from SocketLogger import SocketLogger as sLogger

class ServerSocket(Thread):
    def __init__(self,con,dic):
        super(ServerSocket, self).__init__()
        self._con = con
        self._dic = dic

    def save(self):
        with open("list.txt", "wb") as f:
            pickle.dump(self._dic, f)

    def send_data(self, content):
        return bytes(content, encoding="utf-8")

    def run(self):
        try:
            while True:
                data = self._con.recv(1024)

                if data == '':  # connection is closed
                    raise Exception("Client is killed")

                str_data = str(data, 'utf-8')
                arg_data = str_data.split(",")
                command = arg_data[0]

                if str_data == 'quit':
                    raise Exception("Client closes")
                elif command == 'put':
                    key = arg_data[1]
                    value = arg_data[2]
                    self._dic[key] = value
                    sLogger.logger.info(self._dic)
                    self._con.send(self.send_data("ok"))
                elif command == 'get':
                    key = arg_data[1]
                    sLogger.logger.info(self._dic.get(key))
                    self._con.send(self._dic.get(key).encode("utf-8"))
                elif command == 'save':
                    self.save(self._con)
                    self._con.send(self.send_data("ok"))
                else:
                    sLogger.logger.info(str_data)
                    self._con.send(data)
        except Exception as e:
            sLogger.logger.error(e)
            self._con.send(self.send_data("fail"))