from time import time

def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i

def main():
    numbers = [21390790, 12147590, 14166370, 18394850]
    start = time()

    # 순서대로 계산
    for number in numbers:
        a = list(factorize(number))
        print(a)

    print(time()-start)

if __name__ == "__main__":
    main()