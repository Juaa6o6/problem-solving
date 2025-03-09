# [Bronze V] A+B - 5 - 10952

[문제 링크](https://www.acmicpc.net/problem/10952)

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2025년 3월 7일 22:57:48

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

<p>입력의 마지막에는 0 두 개가 들어온다.</p>

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
while True :
    a, b = map(int, input().split())
    i = a + b
    if a == 0 and b == 0 :
        break
    print(i)
```

### 메모

- 반복해야 할 횟수가 정해져 있지 않음 <br>
  -> 종결 조건이 주어짐(입력 마지막 0 두 개)
- while문

  ```python
  while 조건식 :
    실행할 코드
  ```

  - 조건에 따른 반복문
  - 조건식의 값이 참(True)일 동안 실행할 코드를 반복하고,<br>
    조건식의 값이 거짓(False)이 될 때 반복을 종료하고 빠져나감

  - break : 실행을 중단하고 반복문을 빠져나옴
  - continue :

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
