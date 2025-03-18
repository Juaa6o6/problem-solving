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

- EOF Error 발생!

- EOF Error

  - End Of File Error의 약자
  - 입력 함수(input() 등)가 예상한 데이터를 받지 못하고 파일 끝(EOF: End Of File)에 도달했을 때 발생하는 에러

  - 발생 이유

    - 입력이 없는 경우
    - 터미널에서 입력 없이 종료한 경우 input()이 더 이상 데이터를 받을 수 없어서 발생

  - 해결 방법
    - 예외 처리 (try-except)
    - sys.stdin.readline() <br>
      (입력이 없으면 빈 문자열("")을 반환하기 때문에, EOFError가 발생하지 않음)

- 예외(Exception)

  - 프로그램 실행 중에 발생하는 예상하지 못한 오류를 의미
  - try-except 기본 구조

    ```python
    try:
      # 예외가 발생할 가능성이 있는 코드
    except 예외타입:
      # 예외 발생 시 실행할 코드
      # 예외타입 작성 X -> 모두 처리
    ```

  - 발생하는 예외마다 처리를 해줄 수 있음
    ```python
    try:
         예외1, 2, 3이 발생할 가능성이 있는 코드
     except 예외1:
         예외1이 발생할 경우 처리할 코드
     except 예외2:
         예외2가 발생할 경우 처리할 코드
    ```

<br>

---

### 다른 답

```python
import sys
while True:
    try:
        a, b = sys.stdin.readline().rstrip().split()
    except:
        break
    else:
        print(int(a) + int(b))
```
