
g_var = 1


def method_global():
    global g_var  # 주석하면 에러가 발생
    g_var += 1
    print(f"method_global = {g_var}")


# def method_global_error():
#     g_var += 1


def method_local():
    g_var = 0
    g_var += 1
    print(f"method_local = {g_var}")


def method_nonlocal():
    nl_var = 0

    def a():
        nonlocal nl_var
        nl_var += 1
        print(f"method_nonlocal -> a = {nl_var}")

    print(f"method_nonlocal = {nl_var}")
    a()
    print(f"method_nonlocal = {nl_var}")


if __name__ == '__main__':
    print(f"main = {g_var}")
    method_global()
    print(f"main = {g_var}")
    method_local()
    print(f"main = {g_var}")

    method_nonlocal()
