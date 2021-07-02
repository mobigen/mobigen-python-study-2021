# 요소 삽입(Insert)

Notes: 데이터 삽입
big-O: O(N)

`insert(a, b)`: 리스트의 특정위치 **a**에 **b**라는 값을 삽입

```python
ls = [1, 2, 3]
ls.insert(0, 4)      # 0번째 위치에 4라는 값을 삽입
ls

# output: [4, 1, 2, 3]

ls.insert(3, 5)      # 3번째 위치에 5라는 값을 삽입
ls

# output: [4, 1, 2, 5, 3]
```

리스트의 범위 밖에 있는 위치값을 지정시 리스트 맨 마지막에 값이 삽입

```python
ls = [1, 2, 3]
ls.insert(100, 6)    # 100번째 위치에 6이라는 값을 삽입
ls

# output: [1, 2, 3, 6]
```