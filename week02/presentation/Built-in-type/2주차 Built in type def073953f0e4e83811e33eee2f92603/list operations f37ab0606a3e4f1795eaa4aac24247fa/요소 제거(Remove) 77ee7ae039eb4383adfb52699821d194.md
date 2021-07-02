# 요소 제거(Remove)

Notes: 데이터 삭제
big-O: O(N)

remove(x) 함수는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수

```python
ls = [1, 2, 3, 1, 2, 3]
ls.remove(3)
a

# output: [1, 2, 1, 2, 3]
```

리스트에 존재하지 않는 값을 삭제하려고하면 ValueError 발생

```python
ls = [1, 2]
ls.remove(3)        # 리스트에 존재하지않는 3이라는 값을 삭제하려고 시도
```

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-4-171d0deff567> in <module>
      1 ls = [1, 2]
----> 2 ls.remove(3)

ValueError: list.remove(x): x not in list
```