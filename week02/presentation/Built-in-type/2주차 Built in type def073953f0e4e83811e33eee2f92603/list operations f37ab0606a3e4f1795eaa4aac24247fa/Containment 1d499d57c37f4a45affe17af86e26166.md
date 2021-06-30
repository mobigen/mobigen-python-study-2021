# Containment

Notes: 포함 또는 불포함 여부 확인
big-O: O(N)

리스트에 특정 요소가 포함되는지 혹은 불포함되는지 여부를 확인

- `x in s`: x가 리스트 s에 포함되면 True, 그 역의 결과는 False

    ```python
    ls = [1 ,2, 3]
    2 in ls

    # output: True
    ```

- `x not in`: x가 리스트 s에 불포함되면 True, 그 역의 결과는 False

    ```python
    ls = [1, 2, 3]
    2 not in ls

    # output: False
    ```