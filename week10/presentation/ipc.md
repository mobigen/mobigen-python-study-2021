# 멀티 프로세스 사용법

## 1. 상속하여 사용하기
```python
import multiprocessing

class Process(multiprocessing.Process):
  def __init__(self, id):
    super(Process, self).__init__()
    self.id = id

  def run(self):
    print("I'm the process with id: {}".format(self.id))

if __name__ == '__main__':
  processes = Process(1), Process(2), Process(3), Process(4)
  [p.start() for p in processes]
```

## 2. 멀티프로세스풀 사용하기(블락과 논블락)
```python
import multiprocessing

def square(x):
  return x*x

if __name__ == '__main__':
  # Pool 객체 초기화
  # 할당하지 않으면 코어수만큼 할당됩니다.
  pool = multiprocessing.Pool(processes=4)

  # Pool.map
  # 결과가 나올때까지 블락
  inputs = [0, 1, 2, 3, 4]
  outputs = pool.map(square, inputs)

  print(outputs)

  # Pool.map_async
  # outputs_async.get을 호출하기 전까지 main 스레드가 블락되지 않습니다.
  outputs_async = pool.map_async(square, inputs)
  outputs = outputs_async.get()

  print(outputs)
```

## 3. queue(IPC)를 이용하여 작업할당
```python
import multiprocessing

class MyFancyClass(object):

  def __init__(self, name):
    self.name = name

  def do_something(self):
    proc_name = multiprocessing.current_process().name
    print('%s이 %s 프로세스를 만들었습니다. ' % (self.name, proc_name))


def worker(q):
  obj = q.get()
  obj.do_something()


if __name__ == '__main__':
  queue = multiprocessing.Queue()

  p = multiprocessing.Process(target=worker, args=(queue,))
  p.start()

  queue.put(MyFancyClass('1번'))

  queue.close()
  queue.join_thread()
  p.join()
```

<br>

# 프로세스간 통신(inter-process communication, ipc)이란

프로세스 사이에 서로 데이터를 주고받는 행위 또는 그에 대한 방법이나 경로를 뜻합니다.

<br>
<br>

# 프로세스간 통신을 해야하는경우

## (1). 중요 프로세스의 안정성을 위해

하나의 프로세스에서 공유자원을 동기화한후 여러 스레드가 사용하면 데이터 공유를 상대적으로 쉽게 할수 있습니다.

그러나 하나의 프로세스가 죽어버리면 같은 프로세스의 모든 스레드가 죽어버려 위험한 상황이 올 수도 있습니다.

(ex api를 제공하는 작업과 데이터를 적재하는 작업을 하나의 프로세스에서 하는경우 최악의 경우 클라이언트에게 api가 나가지 못하는 상황이 발생할 수 있습니다.)

## (2). 싱글코어만 쓰는 언어에서의 cpu사용율을 높여 성능 최적화가 필요한경우

싱글 코어만 사용하는 파이썬에서도 스레드가 존재합니다.

그러나 싱글스레드언어는 job(스레드)이 많이 생성되더라도 

운영체제가 하나의 코어를 사용하다보니 최적의 성능을 뽑아내기 힘듭니다.

job이 많이 생성되야 하는경우 프로세스를 나눠 처리하는 방식이 효율적일 수 있습니다.


<br>
<br>

# 프로세스 통신의 종류

프로세스간 통신의 방법에는 크게 운영체제영역에서 지원하는 방식과 소켓(네트워크)을 사용하는 방식이 있습니다.

운영체제에서 지원하는 방식

-   파일(file)
-   파이프(pipe)
-   커널 메시지큐(kernel messageq)
-   공유 메모리(shared memory)

소켓(네트워크)을 사용하는 방식

-   tcp
-   http api
-   dbms (sqlite, h2 등 filedb가 아닌 db서버)
-   네트워크 메시지큐(kafka, rabbitMQ, memcache 등)

## (1). file

영속성을 대표하는 방법인 파일을 이용합니다.

하나의 프로세스가 파일을 쓰고 다른 프로세스에서 파일을 읽어가는 방식입니다.

```python
if __name__ == '__main__':
    with open('./test.txt', 'w') as my_file:
        my_file.write("hello world")
```

```python
if __name__ == '__main__':
    with open('./test.txt', 'r') as my_file:
        print(my_file.read())
```

```
$ python ./my_file_read.py
hello world
```

## (2). pipe

부모프로세스와 자식프로세스가 데이터를 교환할때 사용합니다.

부모프로세스는 fork()를 통해 자식프로세스를 생성하며 파이프를 통해 데이터교환을 할 수 있습니다.

양방향으로 데이터공유가 가능합니다.

(커널에 존재하는 IPC 기법인 pipe(|)를 python이 파싱해준 코드입니다.)

```python
import multiprocessing


def f(conn):
    print(conn.recv())
    conn.send(['world'])
    conn.close()

if __name__ == '__main__':
    # pipe는 부모프로세스와 자식프로세스가 데이터를 교환할때 사용됩니다.
    # 부모프로세스는 fork()를 통해 자식프로세스를 생성하며 파이프가 열립니다.
    parent_conn, child_conn = multiprocessing.Pipe()
    parent_conn.send(['hello'])
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
    # output
    # ['hello']
    # ['world']
```

## (3). 커널 메시지큐(kernel messageq)

현대의 메시지큐는 커널의 메시지큐가 아닌 네트워크 메시지큐(kafka, rabbitMQ, memcache 등) 를 칭하여

운영체제의 메시지큐는 커널 메시지큐, 운영체제 메시지큐 라고 부릅니다.

queue다보니 fifo 입니다. 단방향입니다.

(커널에 존재하는 IPC 기법인 messageq를 python이 파싱해준 코드입니다.)

```python
import multiprocessing

def f(q):
    q.put([42, None, 'hello world'])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

## (4). 공유 메모리(shared memory)

key, value 자료구조로 커널에서 데이터 공유하는 방식입니다.

Value와 Array를 지원합니다.

공유자원 동기화는 내부적으로 적용 되어있습니다.

(커널에 존재하는 IPC 기법인 shared memory를 python이 파싱해준 코드입니다.)


```python
import multiprocessing

def f(n, a):
    print(n.value)
    print(a[:])
    n.value = 1.35
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    # d는 double precision float를 i는 signed integer를 의미합니다.
    # typecode_to_type = {
    # 'c': ctypes.c_char,     'u': ctypes.c_wchar,
    # 'b': ctypes.c_byte,     'B': ctypes.c_ubyte,
    # 'h': ctypes.c_short,    'H': ctypes.c_ushort,
    # 'i': ctypes.c_int,      'I': ctypes.c_uint,
    # 'l': ctypes.c_long,     'L': ctypes.c_ulong,
    # 'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
    # 'f': ctypes.c_float,    'd': ctypes.c_double
    # }

    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', [1,2,3,4,5])

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print (num.value)
    print (arr[:])
```

여기서 Array는 파이썬에서 사용하는 컨테이너 개념이 아닙니다.(같은 자료형의 데이터만 넣어줘야합니다.)

여러 자료형을 넣어주고 싶다면 마샬링을 해야합니다.

이런 불편함을 해소해주기 위해 파이썬은 multiprocessing.Manager 클래스를 제공합니다.

```python
import multiprocessing

def f(d, l):
    d['hello'] = 'world'
    l.append('abc')

if __name__ == '__main__':
    manager = multiprocessing.Manager()

    d = manager.dict()
    l = manager.list([1,"2",3])

    p = multiprocessing.Process(target=f, args=(d, l))
    p.start()
    p.join()

    print(d)
    print(l)
```
<img src=./process.PNG>

위의 방법들은 하나의 PC에서만 데이터 공유가 가능합니다.

클라이언트 개발에서 주로 사용되며, 하나의 서버만 존재하는 환경에서도 사용하기 적합합니다.

(5)부터는 서버가 여러대인 경우 사용하기 적합합니다.

## (5). tcp

```python
import socket

ip = "127.0.0.1"
port = 8381

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((ip,port))

socket_server.listen(1)

conn, addr = socket_server.accept()

data = conn.recv(1024)
print(data.decode("utf-8"))

socket_server.close()
```

```python
import socket

ip = "127.0.0.1"
port = 8381

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((ip,port))

socket_client.send("hello world".encode("utf-8"))
socket_client.close()
```

소켓통신은 직렬화 역 직렬화를 꼭 해줘야 합니다.

로컬에서도 서버와 클라이언트를 구축하여 데이터 공유를 할 수 있습니다.

while문을 통해 socket접속을 유지시킨대로 데이터공유만 한다면 실시간 데이터 공유가 가능합니다.

(주식서버, 게임서버 같이 실시간 데이터가 중요한 경우 웹소켓으로 구현합니다.)

## (6). http api

```python
import http.server

from urllib.parse import urlparse



class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('hello world'.encode('utf-8'))
        return None

s=http.server.HTTPServer(('localhost',8081), MyHandler)
s.serve_forever()
```

브라우저나, http 클라이언트 프로그래밍을 하여 8081포트에 접근하면 hello world를 내려줍니다.

대부분의 언어들은 doGet doPost등을 사용해 스트림에 바이트배열을 전달하여 http 요청을 처리합니다.

장고, 플라스크 등 웹 프레임워크는 해당 라이브러리를 래핑하고 필요한 기능을 추가하여 개발 편의성을 높여준 프레임 워크입니다.



## (7). messagq

kafka, rabbitMQ, memcache 등의 네트워크 메시지큐를 이용하는 방법입니다.

MSA같은 환경에서 http api요청은 여러 프로세스간의 통신과정중 어디선가 병목에 걸려 성능저하가 발생하는경우가 빈번합니다.

비동기 queue에 데이터를 공유하여 원하는 곳에서 찾아가거나 제공해주는 방식으로 병목을 해결하기 위해 사용됩니다.

## (8). dbms

db서버를 만들어서 영속성을 유지하며 데이터를 공유하는 방식입니다.

로컬에서 프로세스끼리 데이터 공유를 하는 경우에도 파일db(sqlite, h2)를 사용하는 경우도 있습니다.
(파일디비는 하나의 커넥션만 허용하므로 단일 사용자가 단일 스레드로 작업을 하는경우가 아니라면 운영레벨에서는 사용하면 안됩니다. 테스트 코드 짤때만 써야합니다)
