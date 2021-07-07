class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

if __name__ == '__main__':
    try:
        eagle = Eagle()
        eagle.fly()
    except Exception as e:
        print(e)

    try:
            4 / 0
    except ZeroDivisionError as e:
            print(e)

    f = None
    
    try:
        f = open("test.txt", "r")
    except Exception as e:
        print(e)
    finally:
        if f :
            f.close()

    try:
        a = [1, 2]
        print(a[3])
        4 / 0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except IndexError:
        print("인덱싱 할 수 없습니다.")

    try:
        a = [1, 2]
        print(a[3])
        4 / 0
    except IndexError:
        try:
            print("인덱싱 할 수 없습니다.")
            4 / 0
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")

    try:
            age = int(input('나이를 입력하세요: '))
    except:
            print('입력이 정확하지 않습니다.')
    else:
            if age <= 18:
                    print('미성년자는 출입금지입니다.')
            else:
                    print('환영합니다.')



