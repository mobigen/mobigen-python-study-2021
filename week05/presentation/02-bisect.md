# 배열 이진 분할 알고리즘

Created: July 4, 2021 1:37 PM
Tags: bisect

# 1. 배열 이진 분할

: 정렬된 리스트를 삽입 후에 다시 정렬할 필요 없도록 관리할 수 있도록 지원한다.

**[특징]**

- 이진탐색을 쉽게 구현하게끔 해주는 함수
- 이진탐색을 직접 코드로 구현할 수 있지만 bisect함수를 이용하여 구현 시간을 줄일 수 있다.

- (참고) 이진탐색이란?

    검색해야할 대상(array)을 절반씩 잘라서 찾으려는 target의 범위를 포함하는 serve대상에서 같은 방법으로 찾는 탐색기법

    ⇒ 속도가 빠르다는 장점이 있지만, 배열이 정렬되어 있어야 한다는 제약이 있다.

### 제공되는 함수

1. **bisect_left(a, x, lo=0, hi=len(a)) / bisect_right(a, x, lo=0, hi=len(a)) :** iterable에 value를 삽입할 위치를 찾는다. 이미 value가 존재한다면 왼쪽에 삽입하게 된다. 그리고 삽입될 인덱스를 반환한다.

    ```python
    from bisect import bisect_left, bisect_right 

    nums = [0,1,2,3,4,5,6,7,8,9] 
    n = 5 
    print(bisect_left(nums, n)) 
    print(bisect_right(nums, n))

    #결과값
    # 5
    # 6
    ```

2. **bisect(a, x, lo=0, hi=len(a)) :** 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 리턴한다(= bisect_right와 동일)

    ```python
    import bisect

    result = []
    for score in [33, 99, 77, 70, 89, 90, 100]:
    		# 점수가 정렬되어 삽입될 수 있는 포지션을 반환
        pos = bisect.bisect([60, 70, 80, 90], score)  
        grade = 'FDCBA'[pos]
        result.append(grade)

    print(result)

    #['F', 'A', 'C', 'C', 'B', 'A', 'A']
    ```

3. **insort_left(a, x, lo=0, hi=len(a)) / insort_right(a, x, lo=0, hi=len(a)): 오름차순으로 정렬된 시퀀스에 value를 삽입한다.**

    ```python
    import bisect

    a = [60,70,80,90]
    bisect.insort_left(a, 85)
    bisect.insort_right(a, 85)

    print(a)

    #결과
    # [60,70,80,85,90]
    # [60,70,80,85,90]
    ```

4. **insort(a, x, lo=0, hi=len(a)) : 정렬될 수 있는 위치에 해당 항목을 삽입한다**

    ```python
    import bisect

    a = [60,70,80,90]
    bisect.insort(a, 85)

    print(a)

    #결과
    # [60,70,80,85,90]
    ```
