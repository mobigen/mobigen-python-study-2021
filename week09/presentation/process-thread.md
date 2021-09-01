## 프로세스와 스레드

### 프로세스

- 운영체제에서 생성(fork)되며 메모리에 적재되어 실행되는 프로그램을 말합니다.
- 운영체제는 코드와 데이터를 디스크에서 메모리로 가져와 PCB를 생성, 실행합니다.
- 프로세스 하나가 죽더라도 다른 프로세스에는 영향이 가지 않습니다.
- 자원 공유를 하려면 IPC(Inter Process Comunication; 커널 메시지 큐, 공유메모리 등)를 사용해야합니다.
- Context switching 이 느립니다.(프로세스는 공유하는 영역이 없어서 캐시데이터를 다 버리고 다시 캐시를 만드는 과정이 일어나 속도가 느립니다.)

### 스레드

- 프로세스 내부에서 생성되며 실제로 작업을 하는 주체 입니다.(job이라고도 합니다)
- 스레드에 문제가 생겨 프로세스가 죽는다면 모든 스레드가 같이 죽어버릴 위험성이 있습니다.
- 하나의 프로세스에서 작업을 하므로 자원공유 자체는 쉽습니다.
- 공유는 쉽지만 쓰기작업을 한다면 동기화 문제를 신경써야합니다.
- Context switching 이 빠릅니다.(스레드는 공유하는 자원이 많아서 CPU의 캐시데이터를 사용할수 있어 빠릅니다.)

### Context switching이란
- 문맥교환이라고도 하며 cpu가 실행하는 작업을 변경하는것을 말합니다.
- I/O request를 처리할때 cpu는 순간적으로 이 job을 위해 일을 하지 않습니다.(선점형이라고 하며처리해야할 다른일을 합니다)IO가 끝나는순간 cpu는 해당 job을 위해 다시 일을 하게 됩니다.

### 작업단위

-   운영체제의 입장에서 작업단위 : 프로세스
-   CPU입장에서 작업단위 : 스레드(job) 

## 메모리구조

<img src="./memory.PNG" width="80%" height="50%">


-   스레드는 code영역, data영역 head영역은 공유하고 stack은 영역은 공유하지않습니다.
-   heap영역의 자원을 사용할때 concurrent 자료구조를 사용하거나 직접 lock을 걸어줘야 합니다. 

## 싱글스레드언어와 멀티스레드언어

### 싱글스레드언어

스레드가 하나인 언어로 javascript가 대표적입니다.

파이썬도 병렬처리를 위한 스레드를 갖고있습니다.

그러나 운영체제가 싱글스레드언어의 스레드를 cpu에 직접 할당하지 못합니다.

cpu는 동시에 하나의 코어만 사용하여 스레드를 처리합니다.

코드상의 로직은 동시에 진행되지만 cpu가 순차적으로 한줄씩 처리한다고 생각하면 됩니다.

멀티 스레딩보다는 멀티 테스킹에 가깝습니다.

파이썬은 멀티스레드언어로 불리기보다는 싱글스레드언어, 싱글코어 언어 등 동시에 하나의 CPU만 사용하는 언어로 불립니다.

정확하게는 GIL때문에 하나의 프로세스가 동시에 하나의 코어밖에 사용하지 못하는 언어입니다.


### 멀티스레드언어 

- 스레드가 여러개인 언어로 java, c#, golang 등이 있습니다.

- 멀티스레드언어는 운영체제가 스레드의 작업을 cpu에 직접 할당할 수 있습니다.

## 멀티스레드언어의 스레드 사용

- 멀티스레드 언어로 thread를 만들어 동작시키면 운영체제는 cpu에게 thread의 일을 스케줄링하여 동시에 작업합니다.

- 여러개의 일을 동시에 할 수 있습니다.(현시점 싱글코어의 cpu는 거의 없고 하이퍼스레딩을 사용해 복잡하게 사용합니다.)

c#의 스레드 예제입니다.

```cs
using System;
using System.Threading;

namespace development
{
    class Program
    {
        static void Main(string[] args)
        {
            Thread th1 = new Thread(Work);
            Thread th2 = new Thread(Work);
            Thread th3 = new Thread(Work);
            Thread th4 = new Thread(Work);
            Thread th5 = new Thread(Work);
            Thread th6 = new Thread(Work);
            Thread th7 = new Thread(Work);
            Thread th8 = new Thread(Work);

            th1.Start();
            th2.Start();
            th3.Start();
            th4.Start();
            th5.Start();
            th6.Start();
            th7.Start();
            th8.Start();

            th1.Join();
            th2.Join();
            th3.Join();
            th4.Join();
            th5.Join();
            th6.Join();
            th7.Join();
            th8.Join();
        }
        private static void Work()
        {
            int result = 0;
            for (int i = 0; i < 10000000; i++)
            {
                result += i;
                Console.WriteLine(result);
            }
        }
    }
}
```

스레드 8개에 Work라는 메서드를 할당해서 실행시켰습니다.

Work는 천만 까지의 수를 더하면서 출력하는 메서드입니다.

## 파이썬의 스레드 사용

- python도 스레드를 제공하지만 스레드를 각각 cpu에 할당시키지는 않습니다.(동시에 하나의 코어만 스레드 여러개를 위해 일합니다.)

동일한 코드를 python으로 작성하였습니다.

```py
from threading import Thread

def work():
    result = 0
    for i in range(10000000):
      result += i
      print(result)

if __name__ == "__main__":
    th1 = Thread(target=work)
    th2 = Thread(target=work)
    th3 = Thread(target=work)
    th4 = Thread(target=work)
    th5 = Thread(target=work)
    th6 = Thread(target=work)
    th7 = Thread(target=work)
    th8 = Thread(target=work)
    th9 = Thread(target=work)

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th9.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()
    th9.join()
```

## CPU 사용량 확인

아래는 cpu사용량 그래프입니다.

(타 앱의 영향을 최소화하기위하여 실행은 cmd 명령프롬프트를 사용하였습니다)

8개의 스레드를 만들어 작업했으니

멀티스레드 언어는 8개의 코어를 비슷하게 사용하고

싱글스레드(싱글코어) 언어인 파이썬은 하나의 코어만 사용해서 1개의 코어의 사용량만 올라가고 아래와같은 결과가 나올것 같습니다.

<br>
<br>
<br>

### 예상되는 cpu 사용량(c#, python 순서)
<div>
<img src="./expect2.PNG" width="40%" height="20%">
<img src="./expect.PNG" width="40%" height="20%">
</div>


### 실제 cpu 사용량(c#, python 순서)
<div>
<img src="./python.PNG" width="40%" height="20%">
<img src="./dotnet.PNG" width="40%" height="20%">
</div>

운영체제는 cpu를 그런식으로 동작시키지 않습니다.

c#으로 작성한 프로그램에서는 cpu사용량이 평균적으로 60~70이 나왔고

python으로 작성한 프로그램에서는 cpu사용량이 평균적으로 40~50이 나왔습니다.

(동일한 일을 하는데 CPU사용량이 높다는건 상대적으로 빠르게 일을 처리한다고 볼 수 있습니다.)

### cpu사용량이 생각과 다르게 나온 이유

운영체제가 cpu에 job을 스케줄링할 때 하나의 일을 하더라도 여러 코어로 왔다갔다 하며 일을 하게 합니다.

파이썬은 GIL(Global Interpreter Lock)이 존재하여 동시에 하나의 코어에서만 일을 하는 언어입니다.

빠르게 여러개의 코어를 왔다갔다하는 방식으로 cpu를 사용합니다.(컨텍스트 스위칭)

스레드를 아무리 쪼개봐야 cpu를 동시에 사용하지 못합니다.

c#, java등의 스레드는 운영체제가 cpu에 직접 스케줄링 합니다.

이론상 8개의 코어에 동일한작업이 하나씩 할당 돼야 하지만 운영체제의 복잡한 스케줄링기법에 따라 스케줄링 됐습니다.(CPU의 6번과 8번 스레드는 상대적으로 놀고있습니다) 

그래도 CPU에 직접 스케줄링하니 동시에 CPU를 사용할수 있어 CPU사용량도 높게나올뿐만 아니라 컨텍스트 스위칭이 적고 안정적(캐시사용)이라 그래프가 훨씬 평온한것을 확인할 수 있습니다.(좌측은 엄청난 컨텍스트스위칭에 그래프가 요동칩니다.)

## 스레드가 쓰이는 곳

스레드풀, 비동기 등등 뭘 사용하더라도 병렬처리는 스레드를 하나씩 먹습니다.

tcp stateful socket서버를 만드는경우 클라이언트 하나하나가 모두 스레드를 하나씩 먹습니다.

flask, django node 등 웹프레임워크를 사용하여 구축한 was도 클라이언트의 요청이 http로 들어오는순간 스레드를 하나 먹습니다.(http는 스레드 먹고 tcp열고 통신이 끝나자 마자 스레드를 죽여버립니다 stateless)

이론상 동시에 수많은 사람이 서버를 사용하면 서버의 CPU는 위와같이 사용되어 싱글스레드(싱글코어)언어인 파이썬은 멀티스레드언어보다 성능적으로 뒤쳐질 수 있습니다.

실제로 대규모 트래픽이 생기는 웹 api서버를 구축할때 장고, 플라스크, 익스프레스 등은 잘 사용되지 않습니다.

(c, c++을 제외한 멀티스레드 언어의 성능은 Rust와 golang이 가장 빠르고, 그뒤로 닷넷과 java가 뒤따르고 있습니다.)

## 프로세스가 쓰이는곳

싱글스레드(싱글코어) 언어를 사용하지만 CPU를 동시에 사용하고 싶은경우(자원공유가 어렵다는 단점이 있습니다.)

자원을 공유할 필요가 없다면 프로세스가 죽더라도 다른프로세스에 영향이 가지 않게 해야하는 경우

운영체제의 다른 프로세스를 이용해야 하는경우

도커이미지로 컨테이너를 실행하는경우
