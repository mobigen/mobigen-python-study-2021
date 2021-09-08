from time import time
from threading import Thread

class FactorizedThread(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))
        print(self.factors)

def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i 

def main():
    numbers = [21390790, 12147590, 14166370, 18394850]
    start = time()
    
    # numbers 갯수만큼 theread 만들어서 실행
    threads = []

    for number in numbers:
        thread = FactorizedThread(number)
        thread.start()
        threads.append(thread)

    # 스레드 완료 기다림 
    for thread in threads :
        thread.join()

    print(time()-start)

if __name__ == "__main__":
    main()