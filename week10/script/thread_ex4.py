import select 
from time import time
from threading import Thread

class SytemcallThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        do_systemcall()

def do_systemcall():
    select.select([],[],[],1)

def compute(index): 
    index += 1
    print(index)

def main():
    start = time()
    threads = []
    for _ in range(10):
        thread = SytemcallThread()
        thread.start()
        threads.append(thread)

    for i in range(10):
        compute(i)

    for thread in threads:
        thread.join()

    print(time()-start)

if __name__ == "__main__":
    main()