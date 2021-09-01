from util import counter, timer

LOOP_CNT = 1000000
GROUP_MOD = LOOP_CNT // 10


@timer
@counter
def get_values():
    result = []
    for i in range(LOOP_CNT):
        result.append({
            "id": i,
            "group": i // GROUP_MOD,
            "name": chr(i // GROUP_MOD),
        })
    return result


@timer
@counter
def get_values_generator():
    # TO-DO
    pass


if __name__ == '__main__':
    print(get_values())
