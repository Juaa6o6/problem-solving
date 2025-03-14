# [Bronze III] 행렬 덧셈 - 2738

[문제 링크](https://www.acmicpc.net/problem/2738)

### 성능 요약

메모리: 32412 KB, 시간: 48 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2025년 3월 14일 23:56:07

### 문제 설명

<p>N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.</p>

### 출력

 <p>첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.</p>

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
import sys

N, M = map(int, sys.stdin.readline().split())

A = []

for a in range(N) :
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
for b in range(N) :
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    d = []
    a = A[i]
    b = B[i]
    for ii in range(M) :
        c = a[ii] + b[ii]
        d.append(c)
    print(" ".join(map(str, d)))
```

### 메모

- append()

  ```
  리스트.append(요소)
  ```

  - 리스트(list)의 끝에 새로운 요소를 추가할 때 사용하는 리스트 메서드

  - 리스트 → 요소를 추가할 리스트
  - 요소 → 리스트에 추가할 값 (숫자, 문자열, 리스트, 튜플 등 어떤 자료형도 가능)

  - e.g.,

    ```python
    data = [1, 2, 3]
    data.append([4, 5])
    print(data)  # 출력: [1, 2, 3, [4, 5]]
    ```

  - append() vs extend()

    ```python
    a = [1, 2, 3]

    a.append([4, 5])
    print(a)  # 출력: [1, 2, 3, [4, 5]]  (리스트 안에 리스트가 추가됨)

    b = [1, 2, 3]
    b.extend([4, 5])
    print(b)  # 출력: [1, 2, 3, 4, 5]  (리스트가 풀려서 개별 요소로 추가됨)
    ```

  - 활용 예시

    - 2차원 리스트 만들기

      ```python
      matrix = []
      for i in range(3):
          row = [i * 3 + j for j in range(1, 4)]
          matrix.append(row)

      print(matrix)
      # 출력: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      ```

    - 빈 리스트에 요소 추가

      ```python
      numbers = []
      for i in range(1, 6):
      numbers.append(i)

      print(numbers)  # 출력: [1, 2, 3, 4, 5]
      ```

    - 사용자 입력을 리스트에 추가

      ```python
      user_inputs = []
      for _ in range(3):
      data = input("입력하세요: ")
      user_inputs.append(data)

      print(user_inputs)
      >>>
      ['1 2 3','1,2,3','안녕']
      ```

- join()

  ```python
  '구분자'.join(반복가능한_객체)
  ```

  - 문자열과 반복 가능한(iterable) 객체의 요소들을 하나의 문자열로 합칠 때 사용하는 문자열 함수

  - 특정 구분자(delimiter)를 지정해서 붙일 수 있음

  - 숫자는 바로 사용할 수 없음, 문자열로 반환하여 사용

    - TypeError 발생 주의! (expected str instance, int found)

      ```python
        numbers = [1, 2, 3]
        result = ' '.join(map(str, numbers))  # map(str, numbers)로 변환
        print(result)  # 출력: 1 2 3
      ```

  - 활용 예시

    - 파일 경로 합치기

      ```python
      folders = ['home', 'user', 'documents']
      path = '/'.join(folders)
      print(path)  # 출력: home/user/documents
      ```

    - CSV 데이터 생성

      ```python
      data = ['Alice', '24', 'Developer']
      csv_line = ','.join(data)
      print(csv_line)  # 출력: Alice,24,Developer
      ```

  <br>

---

### 다른 답

```python
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

for row in result:
    print(*row)
```

```python
import sys

readline = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, readline().split())
for row1 in [list(map(int, readline().split())) for _ in range(n)]:
    row2 = map(int, readline().split())
    write(' '.join(map(str, map(sum, zip(row1, row2)))) + '\n')
```
