# [Bronze V] X보다 작은 수 - 10871

[문제 링크](https://www.acmicpc.net/problem/10871)

### 성능 요약

메모리: 33432 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 3월 11일 23:30:32

### 문제 설명

<p>정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)</p>

<p>둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.</p>

### 출력

 <p>X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.</p>

### 예제 입력

```
10 5
1 10 4 9 2 3 8 5 7 6
```

### 예제 출력

```
1 4 2 3
```

<br>

---

### 사용 언어

- python 3

### 제출

```python
import sys

N, X = map(int, sys.stdin.readline().split())
for a in map(int, sys.stdin.readline().split()):
    if a < X:
        sys.stdout.write(f'{a} ')
```

```python
n, x = map(int, input().split())

for a in map(int, input().split()) :
    if a < x :
        print(a, end = " ")
```

```python
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n) :
    if a[i] >= x :
        continue
    print(a[i], end = " ")
```

### 메모

- input보다 sys.stdin.readline() 확실히 빠름
- int()는 하나의 숫자만 변환됨

  - ValueError
    - input()으로 받은 값이 '1 10 4 9 2 3 8 5 7 6'처럼 여러 개의 숫자가 한 줄에 들어왔는데, int()는 하나의 숫자만 변환할 수 있어서 오류가 남

- 순회 가능 = 이터러블
- set도 이터러블임

  - 집합인데 순서는 없지만 요소를 하나씩 볼 수 있어서 이터러블

- map도 이터러블임

  - map의 반환이 이터러블 객체임

  - 이터러블이라는 말은 **iter** 메소드를 가진 객체를 의미함

  ```python
      x = map(int, input().split())
      print(x)
      >>>
      <map object at 0x000001AB5F157340>
  ```

  - 위에 결과는 map(int, input().split())가 map 객체를 반환하기 때문에 저렇게 나오는 것

    <details>
    <summary>설명</summary>

    ### 코드 분석

    ```python
    x = map(int, input().split())
    print(x)
    ```

    1. `input().split()`

    - 사용자가 입력한 문자열을 공백 기준으로 나누고 리스트로 반환해.
    - 예를 들어 입력이 `"10 20 30"`이면 `['10', '20', '30']` 리스트가 됨.

    2. `map(int, input().split())`

    - 리스트의 각 요소(문자열)를 `int`로 변환하는 `map` 객체를 생성.
    - `map` 객체는 **이터레이터(iterator)**라서, 내부 데이터를 바로 볼 수 없고 `print(x)` 하면 메모리 주소가 출력됨.

    ### 해결 방법

    만약 `map` 객체의 값을 보고 싶다면, 리스트나 튜플로 변환해야 해.

    ```python
    print(list(x))  # [10, 20, 30]
    ```

    이렇게 하면 `map` 객체 내부 값이 리스트로 변환되어 출력돼! 😃
    </details>

<br>

---

### 다른 답

```python
n, x = map(int, input().split())
num_list = list(map(int, input().split()))
print(" ".join(str(a) for a in num_list if a < x))
```
