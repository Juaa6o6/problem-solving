# [Bronze III] 팩토리얼 - 10872

[문제 링크](https://www.acmicpc.net/problem/10872)

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 수학

### 제출 일자

2025년 3월 5일 23:33:54

### 문제 설명

<p>0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.</p>

### 출력

 <p>첫째 줄에 N!을 출력한다.</p>

<br>

---

### 사용 언어

- python 3

### 제출

```python
n = int(input())
a = 1
for i in range(1, n+1) :  # n+1이어야 하는 이유 -> a = 1
    a *= i  # (a = 1) * 1 * 2 * 3 * 4 * 5
print(a)
```

### 메모

- 팩토리얼

  - 특정 정수에서 1까지의 수를 모두 곱하는 것
  - 기호 : 정수 !
  - e.g., 5! => 5 x 4 x 3 x 2 x 1 = 120

- range 함수

  - range(1, 1) 는 값이 존재하지 않음 <br>

    -> for문 실행 안 됨 -> a = 1 그대로 출력 됨

- 할당 연산자 : \*=

  - ( a = a _ i ) == ( a _= i )

- a 변수 선언이 꼭 필요한가? (다른 답 참고)

<br>

---

### 다른 답

```python
N = int(input())
if N == 0:
    print('1')
else:
    for num in range(1, N):
        N *= num    # 5 * 1 * 2 * 3 * 4
    print(N)
```
