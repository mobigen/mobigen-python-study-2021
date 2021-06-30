# 리스트 정렬(Sort)

`sort()`, `sorted()` 함수를 통해 Iterable한 자료형을 정렬하는 것이 가능

디폴트 정렬 기준은 문자열은 알파벳, 숫자는 오름차순으로 정렬

## 기본 사용 예시

1. `list.sort()`
    - 원본 리스트를 변형하여 정렬

        ```python
        num_ls = [1, 4, 3, 2]
        ls.sort()
        ls
        # output [1, 2, 3, 4, 5]

        num_ls = ['d', 'a', 'c', 'b']
        ls.sort()
        ls
        # output: ['a', 'b', 'c', 'd']
        ```

2. `sorted(list)`
    - 정렬된 결과를 반환시키고 **원본은 변형시키지 않는다.**

        ```python
        num_ls = [5, 2, 3, 1, 4]
        sorted(num_ls)
        # output: [1, 2, 3, 4, 5]

        num_ls
        # output: [5, 2, 3, 1, 4]
        ```

## Paramter 사용

`key`, `reverse` 를 인자를 사용하면 원하는 형태로 정렬을 조작가능

1. `reverse`
    - reverse에 bool값을 인자로 전달하여 사용
    - 디폴트 값은 `reverse=False` (오름차순)
    - reverse를 True로 지정하면 내림차순으로 정렬 가능

        ```python
        num_list = [15, 22, 8, 79, 10]
        num_list.sort(reverse=True)
        print(num_list)

        # output: [79, 22, 15, 10, 8]
        ```

2. `key`
    - key인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하며 순서대로 정렬합니다.
    - key를 사용한 정렬 예시

        ```python
        ls = [[0, 4], [1, 3], [2, 2], [3, 1]]
        print(sorted(ls, key=lambda x : x[1]))

        # [[3, 1], [2, 2], [1, 3], [0, 4]]
        ```

        - `lambda x : x[1]`
            - 정렬 대상의 각 요소(단일 리스트)를 받아들이고 리스트의 1번째 요소를 반환
            - 리스트의 1번째 요소를 기준하여 오름차순 정렬