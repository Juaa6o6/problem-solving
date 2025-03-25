# [Bronze V] 아스키 코드 - 11654

[문제 링크](https://www.acmicpc.net/problem/11654)

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2025년 3월 18일 18:08:12

### 문제 설명

<p>알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.</p>

### 출력

 <p>입력으로 주어진 글자의 아스키 코드 값을 출력한다.</p>

### 예제 입력

```
A
```

### 예제 출력

```
65
```

<br>

---

### 사용 언어

- python 3

### 제출

```python
print(ord(input()))
```

### 메모

- ord()

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
