# [Bronze V] 개수 세기 - 10807

[문제 링크](https://www.acmicpc.net/problem/10807)

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

구현

### 제출 일자

2025년 3월 12일 23:58:03

### 문제 설명

<p>총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.</p>

### 출력

 <p>첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.</p>

### 예제 입력

```
11
1 4 1 2 4 2 4 2 3 4 4
2
```

### 예제 출력

```
3
```

<br>

---

### 사용 언어

- python 3

### 제출

```python
N = int(input())
N_list = list(map(int,input().split()))
v = int(input())

print(N_list.count(v))
```

```python
import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(N_list.count(v))
```

### 메모

- count()

  ```
  변수.count(찾는 요소)
  ```

  - 문자열, iterable 자료형(튜플, 리스트 등)에서 원하는 요소의 개수를 숫자로 반환하는 함수
    - dictionary, set iterable 자료형에서는 count 함수를 사용할 수 없음
  - e.g.,

    ```python
    a = [1, 1, 1, 2, 3]
    a.count(1)
    >>>
    3

    ['ox', 'o', 'x', 'oxoxox'].count('ox')
    >>>
    1
    ```

- \*

  - **가변 인자 함수 정의**

    - 함수를 정의할 때 `*args`를 사용하면 여러 개의 인자를 하나의 튜플로 받을 수 있음

      ```python
      def my_function(*args):
          print(args)

      my_function(1, 2, 3)  # 출력: (1, 2, 3)
      ```

  - **가변 키워드 인자 함수 정의**

    - `**kwargs`를 사용하면 키-값 쌍 형태의 가변 인자를 받을 수 있음

      ```python
      def my_function(**kwargs):
          print(kwargs)

      my_function(a=1, b=2)  # 출력: {'a': 1, 'b': 2}
      ```

  - **함수 호출 시 언패킹**

    - 리스트, 튜플, 딕셔너리를 언패킹하여 함수의 인자로 전달할 수 있음

      ```python
      def add(a, b, c):
          return a + b + c

      nums = [1, 2, 3]
      print(add(*nums))  # 출력: 6
      ```

  - **리스트 확장**

    - 리스트를 확장하거나 병합하는 데 사용됨

      ```python
      list1 = [1, 2]
      list2 = [*list1, 3, 4]  # [1, 2, 3, 4]
      ```

  - **튜플/리스트 언패킹**

    - `*`를 사용하여 나머지 값을 특정 변수에 묶을 수 있음
      ```python
      a, *b, c = [1, 2, 3, 4, 5]
      print(a)  # 출력: 1
      print(b)  # 출력: [2, 3, 4]
      print(c)  # 출력: 5
      ```

  - **집합(Set) 언패킹**

    - 집합을 언패킹하여 다른 컬렉션에 병합할 수 있음
      ```python
      set1 = {1, 2, 3}
      set2 = {4, *set1, 5}  # {1, 2, 3, 4, 5}
      ```

  - **키워드 인자 병합**
    - 딕셔너리를 병합할 때 `**`를 사용함
      ```python
      dict1 = {'a': 1, 'b': 2}
      dict2 = {'c': 3, **dict1}  # {'a': 1, 'b': 2, 'c': 3}
      ```

- sys.stdin.read() - 표준 입력으로 들어온 모든 데이터를 한꺼번에 읽음
  <br>

---

### 다른 답

```python
import sys
N, *arr, V = map(int, sys.sdtin.read().rstrip().split())
print(arr.count(V))
```
