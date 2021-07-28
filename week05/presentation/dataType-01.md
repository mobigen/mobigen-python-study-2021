✔목차

# 1. 힙 큐 알고리즘

: **이진트리**기반의 **최소힙(min heap)** 자료구조를 제공

⇒ 힙 큐는 어떤 알고리즘에 쓰일까 ? 우선순위 큐 알고리즘에 주로 쓰인다.

 * **우선순위 큐**란? FIFO 구조와 달리, 들어간 순서에 상관없이 우선순위가 높은 것이 먼저 나오는 것을 의미한다.

- 이진트리란?

    각각의 노드가 최대 두개의 자식 노드를 가지는 트리자료 구조이다. 

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c9e1734f-9fee-4821-b70f-1e2e29c8c1dc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c9e1734f-9fee-4821-b70f-1e2e29c8c1dc/Untitled.png)

- 최대 힙으로 활용하려면?

    힙에 튜플을 원소로 추가하거나 삭제하면 튜플 내에서 맨앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하면 된다. 따라서 최대힙을 만드려면 각 값에대한 우선순위를 구한 후, 튜플을 힙에 추가하거나 삭제하면 된다. 값을 읽어올때는 각 튜플에서 인덱스 1에 있는 값을 가져오면 된다.

    ```python
    import heapq

    heap = [4, 1, 7, 3, 8, 5]
    result = []

    for item in heap:
        heapq.heappush(result, (-item, item))

    while result:
        print(heapq.heappop(result)[1])

    #결과
    # 8
    # 7
    # 5
    # 4
    # 3
    # 1
    ```

**[특징]**

- 원소들이 항상 정렬된 상태로 추가되고 삭제된다.
- pop () 하면 가장 작은 요소가 반환 = root(즉, heap[0]) 은 가장 작은 요소
- 모든 부모 노드가 자식보다 작거나 같은 값을 갖는 이진트리.
- ★ heap모듈은 파이썬의 보통의 리스트를 최소힙처럼 다룰 수 있도록 도와준다. Java의 PriorityQueue 클래스처럼 리스트와 별개의 자료구조가 **아님**을 유의해야 한다. → 그렇기 때문에 빈리스트를 생성한 다음, 이 리스트를 인자로 넘겨야 한다.

### heapq가 제공하는 함수

1.  **heappush(heap, item)** : item을 heap으로 push한다.

    ```python
    import heapq

    heap = []

    heapq.heappush(heap, 4)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    print(heap)
    import heapq

    heap = []

    heapq.heappush(heap, 4)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    heapq.heappush(heap, 11)
    #heapq.heappushpop(heap, 11)
    print(heap)
    #결과 : [1, 3, 4, 4, 8]
    ```

2. **heappop(heap)** : heap에서 가장 작은 항목을 pop하고 반환한다. 단, 힙이 비어있으면 IndexError가 발생한다.

    ```python
    print(heapq.heappop(heap)) # 가장작은 원소를 pop하면서 반환
    print(heap)

    print(heap[0]) # 가장작은 원소를 pop하지 않고 읽기만 함 

    # 결과
    # 1
    # [3, 4, 4, 8]
    # 3
    ```

3. **heappushpop(heap, item)** : 힙에 item을 push한 다음, 가장 작은 항목을 pop하고 반환한다. 이 함수는 heappush()→heappop() 과정을 거치는 것 보다 효율적이다.

    ```python
    import heapq

    heap = []

    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    # heapq.heappush(heap, 11)
    # heapq.heappop(heap)
    #heap.sort()
    print(heapq.heappushpop(heap, 20)) # 제일 작은 1 반환
    print(heap)

    #결과 
    # 1
    # [3, 4, 11, 8]
    ```

4. **heapify(heap)** : 이미 원소가 들어있는 리스트를 힙으로 만들 수 있다.
    - 성능은 인자로 넘기는 리스트의 원소수에 비례 → O(N)

    ```python
    import heapq

    heap = [4, 1, 7, 3, 8, 5]
    heapq.heapify(heap) # heap으로 만들어지면서 자동정렬이 된다.
    print(heap)

    #결과
    # [1, 3, 5, 4, 8, 7]
    ```

5. **heapreplace(heap, item)** : 힙에서 가장 작은 항목을 pop하고 반환하며, item도 push한다. heappop() → heappush()를 하는 것보다 더 효율적이다. 

    ```python
    import heapq

    heap = []

    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    print(heapq.heapreplace(heap, 20))
    print(heap)

    #결과
    # 1
    # [3, 4, 20, 8]
    ```

6. **merge(*iterables, key=None, reverse=True)** : 여러 정렬된 입력을 단일 정렬된 출력으로 병합한다.
    - sorted와 다른점은, iterable을 반환하며, 데이터를 한번에 메모리로 가져오지 않는다는 점이다.
    - reverse=True로 하여 최대>최소로 정렬하고 싶다면 각 입력을 최대 > 최소로 정렬해야 한다.

    ```python
    from heapq import *
    nums1 = [2,4,1,7]
    nums2 = [3,8,5,4]
    result = []

    nums1.sort()
    nums2.sort()
    result = list(merge(nums1, nums2))
    print(result)

    #결과
    # [2, 3, 4, 1, 7, 8, 5, 4] -> 정렬을 하지 않았을 경우
    # [1, 2, 3, 4, 4, 5, 7, 8] -> 정렬을 한 경우
    ```

7. **nlargest(n, iterable, key=None) /  nsmallest(n, iterable, key=None) :** n개의 가장 큰 요소(또는 작은 요소)로 구성된 리스트를 반환

    **⇒ 즉, 가장 크거나 작은 n개의 아이템을 찾을 때 사용한다.**

    - 단, n값에서 가장 잘 동작하며, 값이 크다면 sorted()를 사용하는 것이 더 효율적이다.

    ```python
    import heapq

    nums = [1, 8, 3, -5, 4, 99, -4, 0]

    print(heapq.nlargest(3, nums)) #-> [99, 8, 4]
    print(heapq.nsmallest(3, nums)) #-> [-5, -4, 0]
    ```

- **heapreplace와 heappushpop의 차이?**
    - 아래 예시를 보면 바로 알수 있듯이, heappushpop은 먼저 push를 하기 때문에 -1를 push하고 -1이 제일 작은 값이므로 -1이 다시 return된다.
    - heapreplace는 가장 작은 값인 0을 return하고 -1를 push한다.

    ```python
    from heapq import *

    a = [2,7,4,0,8,12,14,13,10,3,4]
    heapify(a)
    b = a[:]
    print(heappushpop(a, -1)) # 결과 -1
    print(heapreplace(b, -1)) # 결과 -0
    ```
