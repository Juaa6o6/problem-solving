# [Bronze V] X보다 작은 수 - 10871

[문제 링크](https://www.acmicpc.net/problem/10871)

### 성능 요약

메모리: 33432 KB, 시간: 40 ms

### 분류

구현

### 제출 일자

2025년 3월 11일 22:46:54

### 문제 설명

<p>정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)</p>

<p>둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.</p>

### 출력

 <p>X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.</p>

### 예제 입력

```
5
1 1
2 3
3 4
9 8
5 2
```

### 예제 출력

```
2
5
7
17
7
```

<br>

---

### 사용 언어

- python 3

### 제출

```python
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n) :
    if a[i] >= x :
        continue
    print(a[i], end = " ")
```

### 메모

- input을 여러번 받으면 for문 안에 넣어서 반복 실행하면 됨
- for문

  ```python
  for 변수 in iterable :
    실행할 코드
  ```

  - 지정된 횟수만큼 반복하는 횟수 제어 반복문

    - 반복해야 할 횟수, 반복할 대상이 정해져 있을 때 주로 사용

  - iterable(이터러블) : 반복 가능한 객체
  - 변수 : iterable 에서 꺼내온 첫 인덱스 값부터 마지막 인덱스 값까지 차례대로 정의됨
  - 실행할 코드 : for문이 반복될 때마다 실행할 코드 블록

  - 예시

    - for 변수 in 객체(문자열, 리스트, 튜플, 딕셔너리)
      - for문\_객체.ipynb 참고
    - for 변수 in range(정수)
    - 등등

<br>

---

### 다른 답

```python
import sys

N, X = map(int, sys.stdin.readline().split())
for num in map(int, sys.stdin.readline().split()):
    if num < X:
        sys.stdout.write(f'{num} ')
```

```python
n, x = map(int, input().split())
num_list = list(map(int, input().split()))
print(" ".join(str(a) for a in num_list if a < x))
```
