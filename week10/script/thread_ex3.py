import select 
from time import time

def do_systemcall():
    # 운영체제에 1초간 block 한 후 제어를 프로그램에 돌려달라고 요청
    select.select([], [], [], 1)

def compute(index): 
    index += 1
    print(index)

def main():
    # 이 시스템콜을 연속으로 실행한다면?
    start = time()
    for _ in range(10):
        do_systemcall()

    for i in range(10):
        compute(i)
    
    print(time()-start)

if __name__ == "__main__":
    main()