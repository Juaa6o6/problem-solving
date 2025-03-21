# [Bronze V] 사칙연산 - 10869

[문제 링크](https://www.acmicpc.net/problem/10869)

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2025년 2월 27일 22:02:43

### 문제 설명

<p>두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. </p>

### 입력

 <p>두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)</p>

### 출력

 <p>첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.</p>

### 예제 입력 1

7 3

### 예제 출력 1

10
4
21
2
1

---

### 사용언어

- python 3

### 제출

```python
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))  # print(a//b)
print(a%b)
```

### 오답노트

- 7, 3 넣으면 10 4 21 2 1 으로 나오지만 오답 처리 됨
  - 이유 -> 문자열 포맷팅은 반올림으로 처리하기 때문인 듯
  - 7, 2 를 넣으면 9 5 14 _**4**_ 1 나옴

```python
a, b = map(int, input().split())
print(f"""{a+b}
{a-b}
{a*b}
{a/b:.0f}
{a%b}""")
```

### 메모

- f-string { 변수 : . (n)f }은 반올림으로 처리함~<br>
- 파이썬 산술연산자
  - 덧셈 (+)
    - 문자열도 가능
  - 뺄셈 (-)
    - 문자열은 불가능<br>
      (TypeError: unsupported operand type(s) for -: 'str' and 'str')
  - 곱셈 (\*)
    - 문자열도 정수와 곱셈 가능<br>
      (hi\*3 >>> hihihi)
    - 실수와는 곱셈 불가<br>
      (hi\*3.0 >>> TypeError: can't multiply sequence by non-int of type 'float')
  - 나눗셈 (/)
  - 거듭제곱 (\*\*)<br>
    - 3\*\*3 >>> 27
  - 몫 (//)
    - 7//2 >>> 3
  - 나머지 (%)
    - 2%4 >>> 2
- sep=' '
  - print()의 sep은 ' '(공백)
  - e.g., sep=', ' , sep='\n'(enter) 등..
- import sys
- sys.stdin.read()
  - 모든 입력을 한 번에 읽음
  - 여러 줄을 입력 후 Ctrl + D(Linux/macOS) 또는 Ctrl + Z + Enter(Windows)<br>
    -> 종료 -> 문자열로 반환됨
- sys.stdin.readline()
  - 한 줄씩 입력을 읽음
  - Enter를 입력하면 입력된 한 줄만 문자열로 반환됨
  - 반환된 문자열에는 \n(줄바꿈)이 포함되므로, 필요하면 strip()을 사용해서 제거 가능

---

### 다른 답

```python
A, B = map(int, input().split())
for i in [A+B, A-B, A*B, A//B, A%B]:
    print(i)
```

```python
import sys

a, b = map(int, sys.stdin.read().split())
print(a + b, a - b, a * b, a // b, a % b, sep='\n')
)
```
