# [Bronze V] A+B - 4 - 10951

[문제 링크](https://www.acmicpc.net/problem/10951)

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2025년 3월 7일 23:31:32

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력

 <p>각 테스트 케이스마다 A+B를 출력한다.</p>

### 예제 입력

```
1 1
2 3
3 4
9 8
5 2
0 0
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
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
```

### 메모

- input을 여러번 받으면 for문 안에 넣어서 반복 실행하면 됨
- for문

  ```python
  for 변수 in iterable :
    실행할 코드
  ```

  - 반복문
    - 반복해야 할 횟수, 반복할 대상이 정해져 있을 때 주로 사용
  - iterable(이터러블) : 반복 가능한 객체
  - 변수 : iterable 에서 꺼내온 첫 인덱스 값부터 마지막 인덱스 값까지 차례대로 정의됨
  - 실행할 코드 : for문이 반복될 때마다 실행할 코드 블록
  - 2가지 형식

    - for 변수 in 객체(문자열, 리스트, 튜플, 딕셔너리)
    - for 변수 in range(정수)

<br>

---

### 다른 답

```python
[print(r) for r in [sum(map(int, input().split())) for _ in range(int(input()))]]

# for _ in range(int(input())):
#     print(sum(map(int, input().split())))
```
